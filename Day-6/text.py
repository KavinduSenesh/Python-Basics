# by this code we can read the file content
# file_1 = open("Day-6/file.txt")
# content = file_1.read()
# print(content, type(content))
# file_1.close()

#by this code we can read the file content line by line
# file_1 = open("Day-6/file.txt")
# content = file_1.readline()
# print(content, type(content))
# file_1.close()

#by this code we can read the file content line by line
# file_1 = open("Day-6/file.txt")
# content = file_1.readlines()
# print(content, type(content))
# file_1.close()

# file_1 = open("Day-6/333file.txt")
# content = file_1.readlines()
# print(content, type(content))
# file_1.close()

#different modes to open a file
# r - read mode
# w - write mode(create a file if it does not exist. truncate the file if it exists)
# a - append mode(append at the end of the file without truncating it. create a file if it does not exist)
# x - create mode(open a file for exclusive creation. if the file already exists, the operation fails)
# t - text mode(open file in text mode)

# with open("Day-6/file.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("Day-6/new.txt", "w") as file:
#     file.write("This is Awesome.\n")
#     file.write("programming is fun.\n")

# with open("Day-6/file.txt", "w") as file:
#     file.writelines(["Tank.\n", "is fun.\n"])



#simple contact management system

# 1. create a programme that store and manage contacts in a file name "contacts.txt"
# 2. each contact entry sholud have name, phone number and email address

# >> feature to implement - 
# view call contacts
# read and display al contacts from the file
# append the contact to the file
# exit from the programme

#exmple file - Jhon Doe, 1234567890, John@gmail.com
            #  Kate fery, 1234567890, kate@gmail.com


def viewContact() :
    with open("Day-6/contacts.txt", "r") as file:
        contacts = file.read()
    print(contacts)

def addNewContacts(contact) :
    with open("Day-6/contacts.txt", "a") as file:
        file.write(contact)

while(True):
    print("Enter 1 to View All Contacts")
    print("Enter 2 to Add New Contact")
    print("Enter 3 to Exit the Program")
    user_input = int(input("Enter the Number: "))

    if(user_input == 1):
        viewContact()
    elif(user_input == 2):
        contact_name = input("Enter Contact Name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        contact = "Name: " + contact_name + ", " + "Number: " + phone_number + ", " + "Email: " + email
        addNewContacts(contact)
    elif(user_input == 3):
        break
    else:
        print("Invalid Input. Please Try Again.")
        break





    




