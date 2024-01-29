# Import essentiall modules
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# Create data base fucntion
def createDB(dbName, connection):
    
    #Create a database with the given name using the provided connection.

    '''Parameters :
        name (str): The name of the database to be created.
        connection (psycopg2.extensions.connection) The connection to perform the query.
    '''

    try:
        # Cursor to do the query
        cursor = connection.cursor()

        # Creatig database with the given name
        creatDB = "CREATE DATABASE " + dbName + ';'

        # executing the query
        cursor.execute(creatDB)

        # closing the cursor
        cursor.close()
        print(f"{dbName} database has been created successfully !")

    except Exception as e:
        print(f"Error creating database '{dbName}': {e}")


# Create table fucntion
def createTable(dbName, tableName, columns):

    # Connect directly to the "PhoneBook" database
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="5560",
        port="5432",
        database="PhoneBook"
    )

    # Cursor to do the query
    cursor = connection.cursor()

    # Creatong the table
    createTableQuery = f"CREATE TABLE IF NOT EXISTS {tableName} ("

    # Adding columns
    columnsStr = ", ".join([f"{columnName} {columnDetails}"
                             for columnName, columnDetails in columns.items()])
    createTableQuery += columnsStr

    createTableQuery += ");"

    # executing the query
    cursor.execute(createTableQuery)

    # commit the changes
    connection.commit()

    # closing the cursor
    cursor.close()


# Connect to data pSQL with defined parameters
con = psycopg2.connect(host="localhost", user="postgres",
                       password="5560", port="5432")

'''Setting isolation level to AUTOCOMMIT to ensure immediate execution and
 auto-commit of each SQL statement without the need for explicit commits.'''
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# creating Phonebook database
createDB("PhoneBook", con)

# Define columns
columns = {
    "name": 'VARCHAR(255)',
    "last_name": "VARCHAR(255)",
    "phone_number": "CHAR(11) PRIMARY KEY",
    "address": "TEXT"
}

# creating contacts table to store people information
createTable(dbName="PhoneBook", tableName="Contacts",
             columns=columns)


# closing the connection
con.close()
