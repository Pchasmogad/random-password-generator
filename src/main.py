# Source - https://stackoverflow.com/a/39596292
# Posted by gerrit, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-10, License - CC BY-SA 4.0
# using hashlib.py by Copyright (C) 2005-2010   Gregory P. Smith (greg@krypto.org)
import hashlib, sys
import secrets
import string
alphabet = string.ascii_letters + string.digits
def make_password():
    password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
    my_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(my_hash)
    return my_hash

def save_to_file(my_hash, service):
    service = str(input('What service is the password for?: '))
    with open("hashed_password", "a") as f:
        f.write(f'{service}: {my_hash}\n')

def rm_password():
    service_to_remove = input("Which password to remove?: ")

    with open("hashed_password", "r") as f:
        lines = f.readlines()

    with open("hashed_password", "w") as f:
        for line in lines:
            service = line.split(":")[0]

            if service != service_to_remove:
                f.write(line)
