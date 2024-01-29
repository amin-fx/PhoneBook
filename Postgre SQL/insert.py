import argparse
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def insert(data):
    try:
        # Cursor
        cursor = con.cursor()

        # Insert query
        columnsStr = ", ".join(data.keys())
        valuesStr = ", ".join([f"'{value}'"
                                for value in data.values()])
        inserQuery = f"INSERT INTO contacts\
              ({columnsStr}) VALUES ({valuesStr});"

        # executing the query
        cursor.execute(inserQuery)

        # closing the cursor
        cursor.close()

    except Exception as e:
        print("Error inserting new instance': {e}")


if __name__ == '__main__':
    # defining the parser
    parser = argparse.ArgumentParser()

    # adding args
    parser.add_argument('-contact_name', help="contact's first name")
    parser.add_argument('-contact_last_name', help="contact's last name")
    parser.add_argument('-contact_phone_number', help="contact's phone number")
    parser.add_argument('-contact_address', help="contact's address ")

    # parsing the arguments
    args = parser.parse_args()

    if not args.contact_phone_number.isdigit():
        print("the phone number should be a numeric value")
        exit()

    # Connect to db
    con = psycopg2.connect(host="localhost", user="postgres",
                           password="****", port="****", database='PhoneBook')

    '''Set isolation level to AUTOCOMMIT to ensure immediate execution and
    auto-commit of each SQL statement without the need for explicit commits.'''
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    contactData = {
        "name": args.contact_name.title(),
        "last_name": args.contact_last_name.title(),
        "phone_number": args.contact_phone_number,
        "address": args.contact_address.title()
    }
    insert(contactData)

    # closing the connection
    con.close()
