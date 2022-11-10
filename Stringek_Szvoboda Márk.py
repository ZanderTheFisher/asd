import string
import random


def f1():
    w=input("írd be a szót: ")
    for i in w:
        print(i)

def f2():
    email=(input("Kérek egy email címet: "))
    ok=True
    if email[0]==".":
        ok=False
        print(".-tal nem kezdődhet!")
    if len(email)- email.find("@")<2:
        ok=False

    if " " in email:
        ok=False
    ook=False
    for i in range(email.find("@"),len(email)):
        if email[i]==".":
            if i+3==len(email) or i+4==len(email):
                ook=True
    if ook and ok:
        print("helyes")
    else:
        print("rossz")

def f3(szo):
    mgh="aáeéiíuúüűoóöő"
    db=0
    for betü in szo:
        if betü in mgh:
            db+=1
    return db

#def f4():


def f5():
    szamok=[]
    for i in range(10):
        szamok.append(random.randint(-100,100))
    print(szamok)


def f6():
    lista=[]
    for i in range(5):
        lista.append(input("Kérek egy szót: "))
    print(*lista)
    for item in lista:
        db=f3(item)
        print(item,"db: ", db)

def f7():
    nevek=[]
    



def main():
    #db=f3("alma")
    #print("magánhangzók száma", db)
    #f6()
    f5()
    f7("Kovács Krisztián, Ayanami Kasumi, Kenji Kotaro, Hataraku Miho, Nakamura Reiji")
    

main()