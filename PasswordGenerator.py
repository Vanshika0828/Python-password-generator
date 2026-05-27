import random
import string


length=int(input("Enter password length:"))

chars=string.ascii_letters + string.digits + string.punctuation

Password=""
for i in range(length):
    Password+=random.choice(chars)

print(Password)


