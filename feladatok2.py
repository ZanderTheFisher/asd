import random
from re import T


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


"Második feladat"

print("---------------------")

print("0: Fej")
print("1: Írás")

tipp = int(input("Fej vagy írás: "))
fejvagyiras = random.randint(0,1)
while (tipp != fejvagyiras):
    fejvagyiras=random.randint(0,1)
    tipp=int(input="Nem talált. Adjon meg egy új számot: ")
    print("Gratulálok! Eltaláltad!")


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


while True:
    n=int(input("Kérek egy számot: "))
    if(n%2==0):
        print("A megadott szám megfelelő")
        break


while True:
    n=int(input("Kérek egy számot: "))
    if(n>0):
        print(n%5)
        break



while True:
    n=int(input("Kérek egy számot 1-7 között: "))
    if(1<=n<=7):
        if(n==1):
            print("hétfő")
        elif(n==2):
            print("kedd")
        elif(n==3):
            print("szerda")
        elif(n==4):
            print("csütörtök")
        elif(n==5):
            print("péntek")
        elif(n==6):
            print("szombat")
        else:
            print("vasárnap")
        break


while True:
    n=int(input("Kérek egy számot: "))
    if(n>0 or n%2==0):
        print("Hiba!")
    else:
        break

while True:
    n=int(input("Kérek egy számot: "))
    if(n%3==0 and n%5==0):
        print(n/3, n/5, sep=' ')
        break

while True:
    n=int(input("Kérek egy számot: "))
    if(n==0):
        break
    else:
        print(n%5)




while True:
    a=int(input("a: "))
    b=int(input("b: "))
    if(a==b):
        break
    elif(a>b):
        print("a nagyobb mint b")
    else:
        print("b nagyobb mint a")


while True:
    n=random.randint(1,12)
    print(n, n%3, sep=' ')
    m=chr(ord(input("Új szám? (i/n) ")))
    if m=='n':
        break

n=random.randint(1,50)


while True:
    tipp=int(input("Tipp: "))
    if(tipp==n):
        break
    elif(tipp<n):
        print("A gondolt szám nagyobb")
    else:
        print("A gondolt szám kissebb")