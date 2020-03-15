from models.user import user
from models.password_utils import generate_salt
from models.db_conection import create_db_connection


cnx = create_db_connection('warsztaty_db')
cursor = cnx.cursor()
cnx.autocommit = True


# print(salt)
# print(u.hashed_password)

#zapisywanie usera:

# u = user()
# u.username = 'Ola3'
# u.email = 'ola3@pl'
# salt = generate_salt()
# u.set_password('abc', salt)
# u.save_to_db(cursor)
# cursor.close()
# cnx.close()

#wczytywanie usera:

# id = 1
# u = user.load_user_by_id(cursor, id)
# print(u.username)
# cursor.close()
# cnx.close()

#wczytywanie wielu userow:

# users = user.load_all_users(cursor)
# for u in users:
#     print(u.username, u.email)
# cursor.close()
# cnx.close()

#modyfikacja obiektu

# id = 1
# u = user.load_user_by_id(cursor, id)
# print(u.email)
# u.email = 'nowy email'
# u.save_to_db(cursor)
# print(u.email)
# cursor.close()
# cnx.close()

#usuwanie usera:

# id = 3
# u = user.load_user_by_id(cursor, id)
# print(u.username, u.id) #3
# u.delete(cursor)
# print(u.username, u.id) #-1 bo z bazy zniknal a obiekt w pythonie ma przypisany -1 zgodnie z funkcja
