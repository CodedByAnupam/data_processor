

import re


def check_name(name):
    name = name.strip()

    if not name:
        return False
    
    if len(name) < 2 or len(name) > 50:
        print("Name length should be between 2 and 50.")
        return False
    if not re.match("^[A-Za-z ]+$", name):
        print("Name must contain spaces and alphabets only.")
        return False
    return True


def check_email(email):
    email = email.strip()

    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email): 
        print("Invalid email format")
        return False
    return True


def check_age(age):

    try:
        age = int(age)

        if age < 18 or age > 120:
            print("Age must be between 18-120")
            return False
        return True

    except ValueError:
        print("Enter valid age")
        return False

    


def check_input(prompt, validation_func):
    
    while True:

        name = input(prompt)
        if (validation_func(name)):
            return name

def main():

    print("Welcome to data processor!\n")

    name = check_input("Enter name: ",check_name)

    email = check_input("Enter email: ", check_email)

    age = check_input("Enter age: ", check_age)


    print("\nSuccess! Record processed:")
    print(f"\nName: {name}\nEmail: {email}\nAge: {age}\n")


if __name__ == "__main__":
    main()
