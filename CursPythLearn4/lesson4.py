
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
import string

# cod gresit , necesita corectari

icloud = input("user, write your email?: ")
caracter_special = string.punctuation
if icloud[-11:] == "@icloud.com" or icloud[-10:] == "@icloud.lu":
    name_user = icloud[:-11] or icloud[:-10]
    domen_user = icloud[-11:] or icloud[-10:]
    print(name_user, domen_user)
    for char in caracter_special:
        if char in name_user and char != "!" and char != "?" and char != "$" and char != "_":
            print("user verified")

else:
    print("user not verified")





