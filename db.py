import mysql
import sys
from mysql.connector import MySQLConnection, Error, errorcode, FieldType
import getpass
from dbconfig import read_db_config

class DB:
    def __init__(self):
        dbconfig = read_db_config()
        if dbconfig['password'] == "":
            dbconfig['password'] = getpass.getpass("database password ? :")

        print(dbconfig)
        self.cursor = None

        # Connect to the database
        try:
            print('Connecting to MySQL database...')
            self.conn = MySQLConnection(**dbconfig)
            if self.conn.is_connected():
                print('connection established.')
                self.cursor = self.conn.cursor(buffered=True)
            else:
                print('connection failed.')

        except mysql.connector.Error as err:
            print('connection failed somehow')
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print("Unexpected error")
                print(err)
                sys.exit(1)

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    db = DB()
    db.close_connection()