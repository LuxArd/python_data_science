
x = 5
print(x)
print(type(x))

y = 3.0
print(y)
print(type(y))

x = float(x)
print(x)
print(type(x))

a = 5
b = 9
total = a + b
total = float(total)
print(total)
print(type(total))

print(8 / 3)
print(8 // 3)
print(2**5)
print(2+3*(1+1))

print(help(abs))
print(abs(-10))
abs_value = abs(-10)
print(abs_value)

print(help(round))
print(round(3.90,9))

print(help(pow))
print(pow(2,5))

print(help(min))
print(min(2,8,9,1,0,77))
print(max(1,22,20))

x = 20
f = 11
print(type(x) == type(f))

t = 21
j = ('mg')
print(type(t) != type(j))

import math

x = math.sqrt(36)
print(x)
print(type(x))
print(int(x))
print(float(x))

x = math.pow(3, 2)
print(x)


f = input("scrie cifra dorita: ")
print(f)
print(type(f))
if f == 2.0:
    print("corect")
else:
    print("asa cum este")

#exercitiu ( calcul parametri triunghiului)

import math

a = int(input("scrie prima latura: "))
b = int(input("scrie a doua latura: "))
c = int(input("scrie a treia latura: "))
perimetrul = a + b + c
print("perimetrul este: ", perimetrul)
p = (a +b + c)/2
aria = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("aria este: ", aria)
h = 2 * aria/b
print("inaltimea este: ", h)









