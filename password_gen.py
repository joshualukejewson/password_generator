import random
import string

def pass_gen():
    name = input("What is the name of the site for the password?: ")
    username = input("What is the username?: ")
    diff = input("Do you want a complex (c) or simple (s) password?: ")
    chars = int(input("How many characters does it need to be?: "))
    
    if diff == 'c':
        password = random.sample(string.ascii_letters + string.digits + '!@#$%&*',chars)
        print(password)

    if diff == 's':
        password = random.sample(string.ascii_letters + string.digits,chars)
        print(password)
    password = ''.join(password)
    with open('passwords.txt', 'a') as f:
            f.write("%s | Username: %s & Password: %s" % (name, username, password))
            f.write("\n")

def main():
    pass_gen()

if __name__ == '__main__':
    main()

