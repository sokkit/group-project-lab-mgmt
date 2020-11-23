import bcrypt

print("Added this as it may come in handy in the future (e.g. Changing password)")
password = input("Enter the password you would like to encrypt: ")
user_input = input("\n1: Static salt (Same as admin password) \n2: Random salt\n")
if user_input == "1":
    password_encrypted = bcrypt.hashpw(password.encode(),b'$2b$12$5nU0TVBvc2ZD2mLE6PztrO')
elif user_input == "2":
    password_encrypted = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
else:
    pass
print(password_encrypted)
