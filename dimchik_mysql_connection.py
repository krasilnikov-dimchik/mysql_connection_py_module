# Mysql.connection module documentation https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html
import mysql.connector
from getpass import getpass
from mysql.connector.errors import Error

class DimchikMysqlConnection:

    def __init__(self):
        self.conn = self.connection()
        self.cursor = self.conn.cursor()
    def connection(self):

        print("Connect to a mysql server ...")
        try:
            self.user = input("Enter a username:\n")
            self.connect = mysql.connector.connect(user=self.user, host="localhost", password=getpass(prompt="Enter a password:\n",)
                                              )
            if self.connect.is_connected():
                print("Connect to a mysql server: OK")
        except Error as err:
            raise err
        return self.connect


    def print_func(self, rows):
        # Print list of rows
        self.list_row = []
        for self.row in rows:
            self.list_row = []
            for self.item in self.row:
                self.list_row.append(str(self.item))
            print("\t" + "\t".join(self.list_row))
        return self.list_row


    def create_database(self, database_name):
        # Create a database
        print(f"Creating the database {database_name} ...")
        self.cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Creating the database {database_name}: OK")


    def use_database(self, database_name):
        # Change a current database
        self.conn.cmd_init_db(database_name)
        # Trying to use the current database
        print("Used database:", self.conn.database)


    def create_table(self, table_name, query):
        # Create a table
        print(f"Creating the table {table_name} ...")
        self.cursor.execute(f"CREATE TABLE {table_name} {query}")
        print(f"Creating the table {table_name}: OK")


    def insert_to_table(self, table_name, columns, query):
        # Insert to a table
        print(f"Inserting into the table {table_name} ...")
        self.cursor.execute(f"INSERT INTO {table_name} {columns} VALUES {query}")
        print(f"Inserting into the table {table_name}: OK")
        self.conn.commit()


    def show_databases(self, ):
        # Print a list of a databases
        print("List of the databases:")
        self.cursor.execute("SHOW DATABASES")
        self.rows = self.cursor.fetchall()
        self.print_func(self.rows)
        return self.rows


    def describe_table(self, database_name, table_name):
        # Describing a table
        self.cursor.execute(f"USE {database_name}")
        self.cursor.execute(f"DESCRIBE {table_name}")
        print(f"Columns of table {table_name}:")
        self.rows = self.cursor.fetchall()
        self.print_func(self.rows)


    def show_table_in_database(self, database_name, table_name=''):
        # Print a rows of all the databases
        self.cursor.execute(f"USE {database_name}")
        self.cursor.execute(f"SHOW TABLES")
        self.rows = self.cursor.fetchall()
        if not table_name:
            for self.table in self.rows:
                print(f"Rows of table {self.table[0]}:")
                self.cursor.execute(f"SELECT * FROM {self.table[0]}")
                self.items = self.cursor.fetchall()
                self.print_func(self.items)
        else:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            self.rows = self.cursor.fetchall()
            self.print_func(self.rows)


    def update(self, table_name, set_condition, where_condition):
        # Update a row
        print(f"Trying to update a row in table {table_name} ...")
        self.cursor.execute(f"UPDATE {table_name} SET {set_condition} WHERE {where_condition}")


    def delete_table_row(self, database_name, table_name, condition):
        # Delete a row
        self.cursor.execute(f"USE {database_name}")
        self.cursor.execute(f"SHOW TABLES")
        self.items = self.cursor.fetchall()

        for self.item in self.items:
            if (table_name == self.item[0]):
                self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")


    def join_tables(self, table_left_name, table_right_name, join_type, condition_left, condition_right):
        # Join two databases
        print(f"Trying to {join_type} tables ...")
        self.cursor.execute(f"SELECT * FROM {table_left_name} {join_type} {table_right_name} on {condition_left} = {condition_right} ")
        self.rows = self.cursor.fetchall()
        self.print_func(self.rows)


    def drop_table(self, database_name,table_name):
        # Drop a table
        print(f"Trying to drop a table {table_name} ...")
        self.cursor.execute(f"USE {database_name}")
        self.cursor.execute(f"DROP table {table_name}")

    def is_table_exist(self, database_name, table_name):
        # Check for a table exist
        print(f"Check if table {table_name} exist ...")
        self.cursor.execute(f"USE {database_name}")
        self.cursor.execute(f"SHOW TABLES")
        self.tables = self.cursor.fetchall()
        self.res = False
        for self.table in self.tables:
            if self.table[0] == table_name:
                self.res = True
        return self.res


    def drop_database(self, database_name):
        # Drop a database
        print(f"Trying to drop a database {database_name} ...")
        self.cursor.execute(f"DROP DATABASE {database_name}")


    def is_database_exist(self, database_name):
        # Check for a database exist
        print(f"Check if database {database_name} exist ...")
        self.cursor.execute(f"SHOW DATABASES")
        self.databases = self.cursor.fetchall()
        self.res = False
        for self.database in self.databases:
            if self.database[0] == database_name:
                self.res = True
        return self.res


