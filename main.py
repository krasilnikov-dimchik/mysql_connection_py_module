# Reference to module documentation https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html
import mysql.connector
from getpass import getpass
from mysql.connector.errors import Error


def connection():
    # Create a new connection to MySQL server
    print("Connect to a mysql server ...")
    try:
        user = input("Enter a username:\n")
        connect = mysql.connector.connect(user=user, host="localhost", password=getpass(prompt="Enter a password:\n",))
        if connect.is_connected():
            print("Connect to a mysql server: OK")
    except Error as err:
        raise err
    return connect


if __name__ == "__main__":
    conn = connection()
