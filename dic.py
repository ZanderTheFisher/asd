class Ember:
    nev=""
    fizu=0

def beolvas():
    f=open("emberek.txt",encoding="UTF8")
    global emberek
    emberek=[]

    for sor in f:
        emb=Ember()
        emb.nev=sor.split(";")[0]
        emb.fizu=int(sor.split(";")[1])
        print(emb.nev, emb.fizu)
        emberek.append(emb)
def kiir(emberek):
    for item in emberek:
        print(item.nev,item.fizu)

def ossz(emberek):
    osszeg=0
    for item in emberek:
        osszeg+=item.fizu
    return osszeg


beolvas()
print("_________________")
kiir(emberek)
print("_________________")
print(emberek[3].nev)
print(ossz(emberek))