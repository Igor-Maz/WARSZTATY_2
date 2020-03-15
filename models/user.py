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
        return False