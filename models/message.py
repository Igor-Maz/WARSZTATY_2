from password_utils import password_hash
from db_conection import create_db_connection

class message(object):
    _id = None
    from_id = None
    to_id = None
    text = None
    creation_time = None

    def __init__(self):
        self._id = -1
        self.from_id = ''
        self.to_id = ''
        self.text = ''
        self.creation_time = ''

    @property
    def id(self):
        return self._id

    def save_to_db(self, cursor):
        if self._id == -1:
            sql = 'INSERT INTO message (from_id, to_id, text, creation_time) VALUES (%s, %s, %s, %s) RETURNING id;'
            cursor.execute(sql, (self.from_id, self.to_id, self.text, self.creation_time))
            self._id = cursor.fetchone()[0]
            return True
        else:
            sql = """UPDATE message SET from_id=%s, to_id=%s, text=%s, creation_time=%s
                      WHERE id=%s"""
            values = (self.from_id, self.to_id, self.text, self.creation_time, self.id)
            cursor.execute(sql, values)
            return True

    def delete(self, cursor):
        sql = "DELETE FROM message WHERE id=%s"
        cursor.execute(sql, (self.id,))
        self._id = -1
        return True

    @staticmethod
    def load_message_by_id(cursor, message_id):
        sql = "SELECT id, from_id, to_id, text, creation_time FROM message WHERE id=%s"
        cursor.execute(sql, (message_id,))  # (user_id, ) - bo tworzymy krotkę
        data = cursor.fetchone()
        if data:
            loaded_message = message()
            loaded_message._id = data[0]
            loaded_message.from_id = data[1]
            loaded_message.to_id = data[2]
            loaded_message.text = data[3]
            loaded_message.creation_time = data[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def load_all_message_for_user(cursor, to_id):
        sql = "SELECT id, from_id, to_id, text, creation_time FROM message WHERE to_id=%s"
        ret = []
        cursor.execute(sql, (to_id,))  # (user_id, ) - bo tworzymy krotkę
        for row in cursor.fetchall():
            loaded_message = message()
            loaded_message._id = data[0]
            loaded_message.from_id = data[1]
            loaded_message.to_id = data[2]
            loaded_message.text = data[3]
            loaded_message.creation_time = data[4]
            return loaded_message
        else:
            return None

    @staticmethod
    def load_all_message(cursor):
        sql = "SELECT id, from_id, to_id, text, creation_time FROM message"
        ret = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            loaded_message = message()
            loaded_message._id = data[0]
            loaded_message.from_id = data[1]
            loaded_message.to_id = data[2]
            loaded_message.text = data[3]
            loaded_message.creation_time = data[4]
            ret.append(loaded_message)
        return ret

