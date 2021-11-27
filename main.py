# Reference to module documentation https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html
import mysql.connector
from getpass import getpass

from mysql.connector.errors import Error
auth_plugin = "plugin_name"
def connection():
    print("Connect to a mysql server ...")
    try:
        # getpass.unix_getpass()
        conn = mysql.connector.connect(user= "dimchik", host="localhost", password= getpass(prompt="Enter a password:\n",))
        # Reports whether the connection to MySQL Server is available
        if conn.is_connected():
            print("Connect to a mysql server: OK")
    except Error as err:
        raise err
    return conn

if __name__ == "__main__":
    conn = connection()