import bcrypt
password = 'password'
encrypted_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(encrypted_password)
# bytes-string
# b'$2b$12$XogNfKx3qIowAk9KHhdJ7e30i7fxDZNcT37DsxFqplE.95K96xX7K'
print(encrypted_password.decode("utf-8"))
# str object
# $2b$12$XogNfKx3qIowAk9KHhdJ7e30i7fxDZNcT37DsxFqplE.95K96xX7K

print(bcrypt.checkpw(password.encode('utf-8'), encrypted_password))
# True
print(bcrypt.checkpw((password + "1").encode('utf-8'), encrypted_password))
# False
