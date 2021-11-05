# exercise 2
def email_check(string):
    for letter in string:
        if '@' and '.' in string:
            return True
        else:
            return False

email=input("Enter your e-mail: ")
print("This email is",email_check(email))
