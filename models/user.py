from password_utils import password_hash
from db_conection import create_db_connection
class user(object):
    _id = None
    username = None
    _hashed_password = None
    email = None

    def __init__(self):
        self._id = -1
        self.username = ''
        self.email = ''
        self._hashed_password = ''

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password
    def set_password(self, password, salt):
        self._hashed_password = password_hash(password, salt)

    def save_to_db(self, cursor):
        if self._id == -1:
            sql = 'INSERT INTO users (email, username, hashed_password) VALUES (%s, %s, %s) RETURNING id;'
            cursor.execute(sql,(self.email, self.username, self._hashed_password))
            self._id = cursor.fetchone()[0]
            return True
        else:
            sql = """UPDATE Users SET username=%s, email=%s, hashed_password=%s
                     WHERE id=%s"""
            values = (self.username, self.email, self.hashed_password, self.id)
            cursor.execute(sql, values)
            return True

    def delete(self, cursor):
        sql = "DELETE FROM Users WHERE id=%s"
        cursor.execute(sql, (self.id, ))
        self._id = -1
        return True

    @staticmethod
    def load_user_by_id(cursor, user_id):
        sql = "SELECT id, username, email, hashed_password FROM users WHERE id=%s"
        cursor.execute(sql, (user_id,))  # (user_id, ) - bo tworzymy krotkę
        data = cursor.fetchone()
        if data:
            loaded_user = user()
            loaded_user._id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user._hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_user_by_email(cursor, email):
        sql = "SELECT id, username, email, hashed_password FROM users WHERE email=%s"
        cursor.execute(sql, (email,))  # (user_id, ) - bo tworzymy krotkę
        data = cursor.fetchone()
        if data:
            loaded_user = user()
            loaded_user._id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user._hashed_password = data[3]
            return loaded_user
        else:
            return None

    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT id, username, email, hashed_password FROM Users"
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_user = user()
            loaded_user._id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user._hashed_password = row[3]
            ret.append(loaded_user)
        return ret

