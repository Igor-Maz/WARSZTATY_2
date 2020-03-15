from models.user import user
from models.password_utils import generate_salt
from models.db_conection import create_db_connection


cnx = create_db_connection('warsztaty_db')
cursor = cnx.cursor()
cnx.autocommit = True


u = user()
print(u.id)
u.username = 'Ola3'
u.email = 'ola3@pl'
salt = generate_salt()
u.set_password('abc', salt)
# print(salt)
# print(u.hashed_password)

u.save_to_db(cursor)
cursor.close()
cnx.close()