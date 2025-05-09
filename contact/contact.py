Contact = {}


def showFunction():
    print(Contact.items())
    print("Name \t Contact")
    for key in Contact:
        print("{} \t {}".format(key, Contact.get(key)))


while True:
    chocie = input(
        "1.Add new Contact \n"
        "2. Serach new contact\n"
        "3. Display The Contact\n"
        "4. Edit the contact \n"
        "5. Delete the contact\n"
        "6. Exit \n"
        "Please write number between 1 to : "
    )
    if chocie == 1:
        name = input("Add your contact name : ")
        phone = input("Add your number")
        Contact[name] = phone

    elif chocie == 2:
        Cname = input("Search the contact")
        if Cname in Contact:
            print(Cname, "Contact number is ", Contact[Cname])
        else:
            print("Not found contact")

    elif chocie == 3:
        if not Contact:
            print("Contact book is empty")
        else:
            showFunction()
