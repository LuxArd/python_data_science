print("binea ai venit")
text = "bine ai venit"
print(type(text))
print(text)

message = "that's my car"
print(message)

message1 = """bine ai venit in ospetie
am gatit ceva gustos
niste costite in cuptor)"""
print(message1)

message2 = "python learn"
print(len(message2))
print(message2[0:6])

message3 = "data science"
lungimea = len(message3)
print(message3[lungimea -1])
print(message3[-1])
print(message3[0:7])

message4 = 'cine stie carte are patru ochi'
print(len(message4))
print(message4[:5])
print(message4[-15:-1])

nume1 = "Andrei"
nume2 = "Victor"
cuvint3 = "sunt frati"
print(nume1 + ' si ' + nume2 + ' ' + cuvint3)
mesaj_total = f'{nume1} si {nume2} {cuvint3} adevarati'
print(mesaj_total)
print(mesaj_total.count(" "))
print(mesaj_total.count("a"))
print(mesaj_total.upper())
print(mesaj_total.lower())
print(len(mesaj_total))
print(mesaj_total.find("i"))

cuv1 = mesaj_total.find("A")
cuv2 = mesaj_total.find("i")
print(cuv1, cuv2)
print(mesaj_total[cuv1:cuv2 + 1])

lever1 = mesaj_total.find("V")
lever2 = mesaj_total.find("o")
print(lever1, lever2)
print(mesaj_total[lever1:lever2 + 1])



