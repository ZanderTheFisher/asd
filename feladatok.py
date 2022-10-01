def f1():
    for i in range(0,51,1):
        print(i)

    print("-------------------")

    for i in range(182,213):
        print(i)

    print("-------------------")
    
    for i in range(100,202,2):
        print(i)

    print("-------------------")

    for i in range(89,58,-2):
        print(i)

    print("-------------------")

    for i in range(1,21,1):
        print(i)
        print(i**2)
    
    print("-------------------")

    for i in range(99,0,-3):
        print(i)

    print("-------------------")

    for i in range(100,49,-5):
        print(i)
    
    print("-------------------")

    for i in range(1,1001,1):
        print(i, end=", ")

    print("-------------------")

    for i in range(1000,0,-3):
        print(i)

    print("-------------------")



def f2():

    for i in range(100):
        print("*", end=" ")
    
    print("------------------")

    bekert = input("kérek egy karakter: ")
    n=int(input("háynszor: "))
    for i in range(n):
        print(bekert)

    print("------------------")

    szoveg= input("szöveg: ")
    for i in range(len(szoveg)+2):
        print("*", end="")
    print("\n*"+szoveg+"*")
    
    for i in range(len(szoveg)+2):
        print("*", end="")

    print("-----------------")

    col = 8
    row = 8



def f9():
    #készíts programot, amely kiírja az N-nél nem nagyobb páratlan számok összegét.

    beszamn=int(input("páratlan szám: "))
    sum=0
    aktualisparatlanszam=1
    for aktualisparatlanszam in range(aktualisparatlanszam, beszamn, 2):
        sum=sum+aktualisparatlanszam
    print(sum)

def f10():

    #10. feladat
    beszamn = int(input("kérem a számot: "))
    sum = 0
    for aktszam in range(beszamn, 1, -1):
        sum = sum + aktszam* (aktszam + 1)
    
    print(sum)

def main():
    f9()
main

import math








terulet=a*b
fumag=terulet/5
print(f"{math.ceil(fumag)} csomag fűmagra van szükség.")

szam = int(input("Szam: "))
if szam > 0 and szam%2 !=0:
    print("negatív páratlan a szám")
