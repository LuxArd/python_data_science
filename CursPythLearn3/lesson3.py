"""

user = "l"
password = 1
user_name = input("introdu user_name: ")
user_password = input("introdu parola: ")

if user_name == user and user_password == password:
    print("date corecte")
else:
    print("date eronate")



numar = int(input("introdu o cifra: "))
if numar > 0:
    print("este mai mare")
elif numar == 0:
    print("cifra egala")
else:
    print("cifra mai mica")


number = int(input("write one number: "))
if number == 1 or number >= 2:
    print("it's ok")
elif number < 0:
    print("write new number")
else:
    print("total resume correct")


s = "learn Python"
if "Python" in s:
    print("corrected write")
else:
    print("diferent")


abs = "learn  Python"
if "more" not in abs:
    print(abs)
    abs = abs + " more "
    print(abs)

text = input("scrie un sir de caractere: ")
for c in text:
    print(c)


for tmt in "Car":
    print(tmt)
    print("industrie")


for america in "state":
    print(america)
    for usa in "012345":
        print(america + usa)
        for football in "sport":
            print(america + ' ' + usa + ' ' + football)
            for ronaldo in "psj":
                print(america + usa + football + ronaldo)

for football in range(0, 10, 2):
    print(football)
for campions in range(1, 5):
    print(campions)



write = input("write a text: ")
for lesson in write:
    print(lesson)
for car in range(0, len(write)):
    print(write[car])

for tema in range(0, 10):
    if tema == 5:
        break
    print(tema)
for gig in range(0, 11):
    if gig == 3:
        continue
    print(gig)


andrei = 20
ioana = 18
while andrei >= ioana:
    print("love")
"""
y = int(input("scrie un numar: "))
while y <= 5:
    y = int(input("scrie un numar: "))
print("numarul este mai >5")








