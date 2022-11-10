class Tanar:
    nev=""
    targy=""
    osztaly=""
    oraszam=0

def beolvas():
    global tanarok
    tanarok=[]
    f=open("beosztas.txt", encoding="UTF8")
    while True:
        sor= f.readline().strip()
        if not sor:
            break
        else:
            ember=Tanar
            ember.nev=sor
            ember.targy=f.readline().strip()
            ember.osztaly=f.readline().strip()
            ember.oraszam=int(f.readline().strip())
            tanarok.append(ember)
    f.close
def f1():
    print(len(tanarok))

def f2():
    osszesen=0
    for item in tanarok:
        osszesen+=item.oraszam
    return osszesen

def f3():
    osszesen=0
    tanarnev=input("Add meg a tanár nevét: ")
    for item in tanarok:
        if item.nev==tanarnev:
            osszesen+=item.oraszam
    return osszesen

def main():
    beolvas()
    f1()
    print(f2())
    print(f3())




main()