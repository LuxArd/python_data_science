
"""
maria = input("introdu familia: ")
ion = input("scrie familia: ")
if len(maria) == len(ion):
    print("sunt frati")
else:
    print("coincidenta nu este")

print(len("@icloud.com"))
print(len("@icloud.lu"))
"""

#print(len("@icloud.com"))
import string
inc = 0
icloud = input("users need to verified: ")
cara_special = string.punctuation
if icloud[-11:] == '@icloud.com':
    name_email = icloud[:-11]
    print(name_email)
    for char in cara_special:
        if char in name_email and char != "!" and char != "?" and char != "$":
            print("user has been verified")
            break
        else:
            inc += 1
        if inc == len(cara_special):
            print("user verified")
else:
    print("user not verified!")






