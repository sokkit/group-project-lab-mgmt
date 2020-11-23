import bcrypt

print("Added this as it may come in handy in the future (e.g. Changing password)")
password = input("Enter the password you would like to encrypt: ")

password_encrypted = bcrypt.hashpw(password.encode(),b'$2b$12$5nU0TVBvc2ZD2mLE6PztrO')
#Uses same salt as main password, use bcrypt.gensalt() for a random one
print(password_encrypted)
