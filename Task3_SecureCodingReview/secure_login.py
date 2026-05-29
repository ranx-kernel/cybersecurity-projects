import hashlib
import getpass

stored_username = "admin"
stored_password_hash = hashlib.sha256("admin123".encode()).hexdigest()

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

password_hash = hashlib.sha256(password.encode()).hexdigest()

if username == stored_username and password_hash == stored_password_hash:
    print("Secure Login Successful")
else:
    print("Invalid Credentials")