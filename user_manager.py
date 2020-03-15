# from models.user import user
# from models.password_utils import generate_salt
# from models.db_conection import create_db_connection
import argparse

# cnx = create_db_connection('warsztaty_db')
# cursor = cnx.cursor()
# cnx.autocommit = True

def main():
    parser = argparse.ArgumentParser(description='User Manager')
    parser.add_argument('-u', help='user login')
    parser.add_argument('-p', help='user password')
    parser.add_argument('-n', help='user password for user')
    parser.add_argument('-l', help='list of all users') #tu nie powinno przyjmowac zadnego argumentu)
    parser.add_argument('-d', help='delete user')
    parser.add_argument('-e', help='edit user login')

    args = parser.parse_args()

    if args.l:
        print('lista uzytkownikow')

    if args.u and args.p and args.e is None and args.d is None:
        print(args.u, args.p)
    else:
        print('zly argument')


if __name__ == "__main__":
    main()
