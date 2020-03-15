from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

username = 'postgres'
passwd = 'coderslab'
hostname = 'localhost'
db = 'warsztaty_db'

def create_db_connection(db):
    return connect(user=username, password=passwd, host=hostname, database=db)

def create_db(db):
    try:
        cnx = connect(user=username, password=passwd, host=hostname)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute('CREATE DATABASE {}'.format(db))
        print('Baza danych zalozona')
    except OperationalError:
        print('Error')
    except DuplicateDatabase:
        print('Baza juz istnieje')
    cursor.close()
    cnx.close()



# create_db('warsztaty_db')
# def create_table(table_name, )