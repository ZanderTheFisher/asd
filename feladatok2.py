import random
from re import S
from socket import INADDR_ALLHOSTS_GROUP
"""
veletlenszam= random.randint(0,10)
print(veletlenszam)

veletlenszam= random.randint(10,15)
print(veletlenszam)

veletlenszam= random.randint(0,100)
print(veletlenszam)

veletlenszam= random.randint(-100,100)
print(veletlenszam)

for i in range(10):
    veletlenszam= random.randint(0,1)
    print(veletlenszam)

for i in range(4):
    veletlenszam= random.randint(-10,30)
    print(veletlenszam)


Második feladat

print("---------------------")

print("0: Fej")
print("1: Írás")

tipp = int(input("Fej vagy írás: "))
fejvagyiras = random.randint(0,1)
while (tipp != fejvagyiras):
    fejvagyiras=random.randint(0,1)
    tipp=int(input="Nem talált. Adjon meg egy új számot: ")
    print("Gratulálok! Eltaláltad!")

for a in szoveg or betu:
    print(szoveg+betu)



szam= int(input("szám: "))
eredmeny= szam
while (szam!=0):
    szam=int(input("új szám: "))
    eredmeny=eredmeny*szam
    print(eredmeny)
print("Kész")

szavak="alma"
ujszo=input("új szó: ")
while (ujszo!=""):
    szavak=szavak + " "+ujszo
    print(szavak)
    ujszo=input("új szó: ")



i= int(input("darabszám: "))
k= input("karakter: ")
s=""
while(i!=0):
    s=s+k
    i=i-1
print(s)

"""

a=int(input("a= "))
b=int(input("b= "))
i=int(input("lépésköz: "))

s=""

if(a>b):
    i=-i

s+=str(a)
while a!=b:
    a+=1
    s+=", "+str(a)

print(s)

i=1
while(i<1000):
    if(i%3==0):
        if(i%5==0):
            print(i)
    i=i+1

s=int(input("összeg: "))
c=0
while s>=200:
    s-=200
    c+=1
print(f"{c}db 200Ft")
while s>=100:
    s-=100
    c+=1
print(f"{c}db 100Ft")
while s>=50:
    s-=50
    c+=1
print(f"{c}db 50Ft")
while s>=20:
    s-=20
    c+=1
print(f"{c}db 20Ft")
while s>=10:
    s-=10
    c+=1
print(f"{c}db 10Ft")
while s>=5:
    s-=5
    c+=1
print(f"{c}db 5Ft")