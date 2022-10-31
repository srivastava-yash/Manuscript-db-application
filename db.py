import mysql
import sys
from mysql.connector import MySQLConnection, Error, errorcode, FieldType
import getpass
from dbconfig import read_db_config
import db_utility
import constants

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

    # Utility function to close the connection to database
    def close_connection(self):
        self.conn.close()

    """
    function to insert data into a given table
    params: 
        table_name - name of the table
        value_list - name of columns to insert data to
        values - tuple of values to be inserted
    """
    def insert_if_not_exists(self, table_name, value_list, values):
        num_of_entities = len(value_list.split(','))
        select_query = db_utility.get_where_query(table_name, value_list, values)
        results  = self.fetchAll(select_query)
        if len(results) == 0:
            query = f"INSERT INTO {table_name} ( {value_list} ) VALUES ("
            for i in range(num_of_entities):
                query += "%s,"
            query = query[:-1]
            query += ")"
            try:
                self.cursor.execute(query, values)
                self.conn.commit()
            except mysql.connector.Error as err:
                print(err)
                return None
            return self.cursor.getlastrowid()

        print(results)
        return results[0][0]

    """
    function to fetch results from the database
    params: 
        query - select query to get the results
    """
    def fetchAll(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(err)
            return list()
        return results

if __name__ == "__main__":
    db = DB()
    print(db.insert_if_not_exists("Person", constants.PERSON_VALUE_LIST, ("Cardi", "B", "cardi.b@gmail.com")))
    #print(db.fetchAll("SELECT * from Person"))
    db.close_connection()