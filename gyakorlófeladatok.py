import random
import math

def f1():
    
    a = int(input("Kérek egy magasságot: "))
    b = int(input("Kérek egy oldalt: "))
    print(a*b)

def f2():

    a = int(input("Kérek egy számot: "))
    b = int(input("Kérek egy másik számot: "))
    c = int(input("Kérek egy harmadik számot: "))
 

def f3():

    a = int(input("Kérem a háromszög egyik oldalát: "))
    b = int(input("Kérem a háromszög egyik oldalát: "))
    c = int(input("Kérem a háromszög egyik oldalát: "))
    
    if a == b or a == c or b == c:
        print("A háromszög egyenlőszárú!")
    else:
        print("A háromszög nem egyenlőszárú!")

def f4():

    beosztas = input("Kérem a beosztását: ")
    fizetes = int(input("Kérem a fizetését: "))
    if beosztas == "vezető":
        ujfizetes= fizetes*1.25
        print(ujfizetes)
    else:
        ujfizetes= fizetes*1.15
        print(ujfizetes)


def f5():
    
    beosztas = input("Kérem a beosztását: ")
    fizetes = int(input("Kérem a fizetését: "))
    if beosztas == "vezető":
        ujfizetes= fizetes*1.25
        print(ujfizetes)
    else:
        ujfizetes= fizetes*1.15
        print(ujfizetes)
    while (beosztas or fizetes != ""):
        beosztas = input("Kérem a beosztását: ")
        fizetes = int(input("Kérem a fizetését: "))
        if beosztas=="vezető":
            ujfizetes= fizetes*1.25
            print(ujfizetes)
        else:
            ujfizetes= fizetes*1.15
            print(ujfizetes)

def f6():

    a = int(input("Kérek egy természetes számot: "))
    for i in range(a,0,-1):
        print(i)

def f7():

    a = int(input("Kérek egy természetes számot: "))
    if a<0:
        print("A feladat nem megoldható!")

def f9():

    elsobekert = float(input("Bekért szám: "))
    masodikbekert = float(input("Bekért szám: "))
    if elsobekert < masodikbekert:
        for i in range (elsobekert,masodikbekert+1):
            print (i**3)
    elif masodikbekert < elsobekert:
        for i in range (masodikbekert,elsobekert):
            print (i**3)

def f10a():
    a= int(input("Bekért sám: "))
    ered=1
    for i in range (1,a+1):
        ered=ered*i
    print(ered)

def f10b():
    a= int(input("Bekért sám: "))
    ered=1
    while a!=0:
        for i in range (1,a+1):
            ered=ered*i
        print(ered)
        break

def f10c():
    a= int(input("Bekért sám: "))
    ered=1
    while True:
        for i in range (1,a+1):
            ered=ered*i
        print(ered)
        break

def f11():
    
    n=int(input("Válasszon egy számot 1-4 között: "))
    for i in range(0,4):
        print()

def f12():
    n = int(input("Kérem a jegyet: "))
    jegy = (n+n)
    while n != 0:
        n = int(input("Kérem a jegyet: "))
        if n == 0:
            print(jegy)

def main():
    #f1()
    #f2()    
    #f3()
    #f4()
    #f5()
    #f6()
    #f7()
    #f8()
    #f9()
    #f10a()
    #f10b()
    #f10c()
    f12()

main()