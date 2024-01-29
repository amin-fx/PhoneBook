import argparse
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def see_contacts():
    try:
        # defining a cursor to do queries
        cursor = con.cursor()

        # writing the insert an instance to contacts table
        sql_select_contact = "SELECT * FROM contacts;"

        # executing the query
        cursor.execute(sql_select_contact)

        # getting the result
        res = cursor.fetchall()

        # closing the cursor
        cursor.close()

        return res

    except Exception as e:
        print("Error searching ': {e}")


def search_contact(search_word):
    try:
        # defining a cursor to do queries
        cursor = con.cursor()

        res = []

        # a loop to search all columns
        for column in ["name", "last_name", "phone_number", "address"]:
            # writing the insert an instance to contacts table
            sql_select_contact = f"SELECT * FROM contacts\
                    where LOWER({column}) = '{search_word.lower()}';"

            # executing the query
            cursor.execute(sql_select_contact)

            # getting the result
            res.extend(cursor.fetchall())
        # closing the cursor
        cursor.close()

        return res

    except Exception as e:
        print("Error searching ': {e}")


if __name__ == '__main__':
    # defining the parser
    parser = argparse.ArgumentParser()

    # defining the arguments
    parser.add_argument('-search',
                        help="the word you want to search it could be a name a lastname and address or\
                              some of them with white space between them")

    # parsing the arguments
    args = parser.parse_args()

    # Establish a connection to the PostgreSQL database with the provided parameters.
    con = psycopg2.connect(host="localhost", user="postgres",
                           password="****", port="****", database='PhoneBook')

    # Set isolation level to AUTOCOMMIT to ensure immediate execution and
    # auto-commit of each SQL statement without the need for explicit commits.
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    if args.search:
        result = search_contact(args.search)
    else:
        result = see_contacts()

    for contact in result:
        print('name:', contact[0])
        print('last name:', contact[1])
        print('phone number:', contact[2])
        print('text:', contact[3])
        print()

    # closing the connection
    con.close()
