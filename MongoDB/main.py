# Import essential modules
import argparse
import pymongo

# Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Set db name
dbName = "phonebook"

# set collection name
collectionName = "contacts"

# create database if not exist
if dbName not in client.list_database_names():
    db = client[dbName]
    print(f"Database '{dbName}' created.")

# use the database
database = client[dbName]

# create the collection if not exist
if collectionName not in database.list_collection_names():
    collection = database.create_collection(collectionName)
    print(f"Collection '{collectionName}' created.")

# use the collection
collection = database[collectionName]


# Insert new contact
def newContact(data):
    collection.insert_one(data)


# Search contacts
def searchContact(data):
    temp = list()
    for att in ["first_name", "last_name", "phone_number", "address"]:
        contact = collection.find({att: data.title()})
        temp.extend(contact)
    return temp


# List all contacts
def allContact():
    contacts = collection.find()
    return contacts


def deleteContact(data):
    contact = collection.delete_one({"phone_number" : data})
    return contact


if __name__ == '__main__':
    
    # Parser
    parser = argparse.ArgumentParser()

    # args
    parser.add_argument('action', help="enter the action",
                        choices=['new_contact', 'search_contact', 'all_contact', 'delete_contact'])

    # pass args
    args = parser.parse_args()

    # parsing action
    action = args.action

    if action == 'new_contact':
        contactInfo = {
            "first_name": input('Enter first name =\t').title(),
            "last_name": input('Enter last name =\t').title(),
            "phone_number": input('Enter phoone number =\t'),
            "address": input('Enter address =\t'.title())
        }

        while not contactInfo['phone_number'].isdigit:
            print("This is not a number")
            contactInfo['phone_number'] = input('Enter phoone number =\t')

        newContact(contactInfo)

    elif action == 'search_contact':

        searchText = input("Enter who you are looking for =\t")
        searchContacts = searchContact(searchText)

        if searchContacts:
            print("This contact(s) found :")
            for contact in searchContacts:
                print(contact)
        else:
            print('Not found !')

    elif action == 'all_contact':
        print("All contacts :")
        contacts = allContact()

        for contact in contacts:
            print(contact)

    elif action == 'delete_contact':
        
        try:
            contactPhoneNumber = input('Enter phone number you want to delete =\t')
            
            while not contactPhoneNumber.isdigit:
                print('This is not a number. Please enrer a valid phone number')
                contactPhoneNumber = input('Enter phone number you want to delete =\t')
            
            deleteContactInfo = deleteContact(contactPhoneNumber)
            
            if deleteContactInfo:
                print("The contace has been removed from phonebook successfully")

            else:
                print("The contact not found")
        
        except Exception as e:
            print(e)

        