# Mysql.connection module documentation https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html
import mysql.connector
from getpass import getpass
from mysql.connector.errors import Error

def connection():

    print("Connect to a mysql server ...")
    try:
        user = input("Enter a username:\n")
        connect = mysql.connector.connect(user=user, host="localhost", password=getpass(prompt="Enter a password:\n",)
                                          )
        if connect.is_connected():
            print("Connect to a mysql server: OK")
    except Error as err:
        raise err
    return connect


def print_func(rows):
    # Print list of rows
    list_row = []
    for row in rows:
        list_row = []
        for item in row:
            list_row.append(str(item))
        print("\t" + "\t".join(list_row))
    return list_row


def create_database(database_name):
    # Create a database
    print(f"Creating the database {database_name} ...")
    cursor.execute(f"CREATE DATABASE {database_name}")
    print(f"Creating the database {database_name}: OK")


def use_database(database_name):
    # Change a current database
    conn.cmd_init_db(database_name)
    # Trying to use the current database
    print("Used database:", conn.database)


def create_table(table_name, query):
    # Create a table
    print(f"Creating the table {table_name} ...")
    cursor.execute(f"CREATE TABLE {table_name} {query}")
    print(f"Creating the table {table_name}: OK")


def insert_to_table(table_name, columns, query):
    # Insert to a table
    print(f"Inserting into the table {table_name} ...")
    cursor.execute(f"INSERT INTO {table_name} {columns} VALUES {query}")
    print(f"Inserting into the table {table_name}: OK")
    conn.commit()


def show_databases():
    # Print a list of a databases
    print("List of the databases:")
    cursor.execute("SHOW DATABASES")
    rows = cursor.fetchall()
    print_func(rows)
    return rows


def describe_table(database_name, table_name):
    # Describing a table
    cursor.execute(f"USE {database_name}")
    cursor.execute(f"DESCRIBE {table_name}")
    print(f"Columns of table {table_name}:")
    rows = cursor.fetchall()
    print_func(rows)


def show_table_in_database(database_name, table_name=''):
    # Print a rows of all the databases
    cursor.execute(f"USE {database_name}")
    cursor.execute(f"SHOW TABLES")
    rows = cursor.fetchall()
    if not table_name:
        for table in rows:
            print(f"Rows of table {table[0]}:")
            cursor.execute(f"SELECT * FROM {table[0]}")
            items = cursor.fetchall()
            print_func(items)
    else:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print_func(rows)


def update(table_name, set_condition, where_condition):
    # Update a row
    print(f"Trying to update a row in table {table_name} ...")
    cursor.execute(f"UPDATE {table_name} SET {set_condition} WHERE {where_condition}")


def delete_table_row(database_name, table_name, condition):
    # Delete a row
    cursor.execute(f"USE {database_name}")
    cursor.execute(f"SHOW TABLES")
    items = cursor.fetchall()

    for item in items:
        if (table_name == item[0]):
            cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")


def join_tables(table_left_name, table_right_name, join_type, condition_left, condition_right):
    # Join two databases
    print(f"Trying to {join_type} tables ...")
    cursor.execute(f"SELECT * FROM {table_left_name} {join_type} {table_right_name} on {condition_left} = {condition_right} ")
    rows = cursor.fetchall()
    print_func(rows)


def drop_table(database_name,table_name):
    # Drop a table
    print(f"Trying to drop a table {table_name} ...")
    cursor.execute(f"USE {database_name}")
    cursor.execute(f"DROP table {table_name}")

def is_table_exist(database_name, table_name):
    # Check for a table exist
    print(f"Check if table {table_name} exist ...")
    cursor.execute(f"USE {database_name}")
    cursor.execute(f"SHOW TABLES")
    tables = cursor.fetchall()
    res = False
    for table in tables:
        if table[0] == table_name:
            res = True
    return res


def drop_database(database_name):
    # Drop a database
    print(f"Trying to drop a database {database_name} ...")
    cursor.execute(f"DROP DATABASE {database_name}")


def is_database_exist(database_name):
    # Check for a database exist
    print(f"Check if database {database_name} exist ...")
    cursor.execute(f"SHOW DATABASES")
    databases = cursor.fetchall()
    res = False
    for database in databases:
        if database[0] == database_name:
            res = True
    return res

conn = connection()
cursor = conn.cursor()
