
# tema seturi

#'add', 'clear', 'copy'  'remove''discard' 'intersection''difference'

# s = set()
# print(dir(s))

# s = [1, 2, 3, 3, 5, 1, 3, 9]
# s = set(s)
# print(type(s))
# print(s)
# new_list = list(s)
# print(new_list)
#print(help(set.add))

# set_1 = {1, 2, 3, 4, 4, (1, 2), 'rar'}
# s = {1, 2, 3, 3, 5, 4, 1, 3, 9}
# diferenta = set_1.difference(s)
# print(diferenta)

# angajati = ['ana', 'maria', 'dima', 'ion']
# card = ['ana', 'ion']
# abonament = ['dima', 'ana', 'ion']
#
# rezult_card = set(angajati).intersection(card)
# rezultat_abonament = set(angajati).intersection(abonament)
# rezu_card_abon = set(card).intersection(abonament)
# cine_nare_card = set(angajati).difference(card)
# print('carduri nu au >>>', cine_nare_card )
# print(f'carduri au >>> {rezult_card}, abonamente au >>> {rezultat_abonament}, card si abonament are >>> {rezu_card_abon}')

# ------------------------------------------------------------------------------------------------------

# Exercițiu 1: Eliminarea duplicatelor
# Scrie un program care primește o listă de numere de la tastatură și afișează aceași listă,
# dar fără duplicat. Utilizează seturile pentru a elimina duplicatelor.

# lista = [1, 2, 600, 101, 201, 101, 2, 601, 600]
# set_lista = set(lista)
# print(f'lista fara duplicate: {set_lista}')
# ------------------------------------------------------------------------------------------------------

# Exercițiu 2: Intersecția a două seturi
# Scrie un program care primește două seturi de la tastatură și afișează intersecția lor (elementele comune).

# set_1 = {1, 3, 909, 15600, 0, 15600, 5}
# set_2 = {1, 3, 99, 909, 5, 15600, 0, 75, 15600, 5}
# rezultat_inter = set(set_1).intersection(set_2)
# rezultat_difer = set(set_2).difference(set_1)
# print(f'rezultat intersectie a 2 seturi e: {rezultat_inter} si diferenta lor e : {rezultat_difer}')
# ------------------------------------------------------------------------------------------------------

# Exercițiu 3: Unirea a două seturi
# Scrie un program care primește două seturi de la tastatură și afișează un set
# care conține toate elementele din ambele seturi (unirea lor).

# set_1 = {1, 3, 909, 15600, 0, 15600, 5}
# set_2 = {1, 3, 99, 909, 5, 15600, 'rar', 0, 75, 15600, 5}
# set_1.update(set_2)  # sau set_3 = set(set_1).union(set_2) , print(set_3)
# print(set_1)
# ------------------------------------------------------------------------------------------------------
# Exercițiu 4: Verificarea submultimilor
# Scrie un program care primește două seturi de la tastatură și verifică dacă primul
# set este o submulțime a celui de-al doilea set.

# set_1 = {1, 3, 909, 15600, 0, 15600, 5}
# set_2 = {1, 3, 99, 909, 5, 15600, 'rar', 0, 75, 15600, 5}
# print(set_1 <= set_2)
# set_3 = set(set_1).issubset(set_2)
# print(set_3)
# ------------------------------------------------------------------------------------------------------

#  Verificare unicitate
# Scrie un program care primește o listă de la tastatură și verifică dacă
# toate elementele din listă sunt unice (nu se repetă).

# list_exe = [1,2,3,8,7,9,99,1,0,1]
# lista = set(list_exe)
# print(lista)
# lista = list(lista)
# print(lista)

# ------------------------------------------------------------------------------------------------------

# Exercițiu 2: Diferența dintre două seturi
# Scrie un program care primește două seturi de la tastatură și afișează
# elementele care sunt prezente în primul set, dar nu sunt prezente în al doilea set.

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# print(set1 >= set2)
# print(set(set2).issubset(set1))
# print(set(set1).difference(set2))
# ------------------------------------------------------------------------------------------------------

# Exercițiu 3: Eliminare elemente comune
# Scrie un program care primește două seturi de la tastatură și elimină elementele comune din primul set.

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# set1.difference_update(set2)
# print(set1)
# ------------------------------------------------------------------------------------------------------

# Exercițiu 4: Verificare disjuncție
# Scrie un program care primește două seturi de la tastatură
# și verifică dacă cele două seturi sunt disjuncte (nu au elemente comune).

# set1 = {1, 2, 3, 4, 5}
# set2 = {1, 2, 3}
# print(set2.isdisjoint(set1))

# ------------------------------------------------------------------------------------------------------

# Exercițiu 5: Concatenare de seturi
# Scrie un program care primește mai multe seturi de la
# tastatură și creează un set nou care conține toate elementele din seturile inițiale.


# num_sets = int(input("Introdu numărul de seturi: "))
# result_set = set()
#
# for i in range(num_sets):
#     set_input = input(f"Introdu setul {i + 1} (elemente separate prin spațiu): ")
#     set_elements = set_input.split()
#     result_set = result_set.union(set_elements)
#
# print("Setul rezultat:", result_set)

