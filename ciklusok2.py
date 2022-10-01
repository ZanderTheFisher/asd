import random

#ha a forban egy adaton megyek végig, akkor a forban lévő ciklusváltozó mindig az adott karakter
szoveg= "aranyalma"
for betu in szoveg:
    print(betu)

#elöltesztelős ciklus
#

oldjelszo= "majom"
jelszo= input("Kérem a jelszót: ")

while oldjelszo != jelszo:
    jelszo = input("Rossz jelszó! Kérem a jelszót: ")

print("Sikeres belépés: ")
#végtelen ciklus: figyeljünk rá, hogy legyen kilépési lehetőség a cilusból. Ctrl+c-vel meg tudjuk állítani a végtelen ciklust.

"""
Hátultesztelős ciklus:
True-ra örökké fut. If-fel megnézem, hogy teljesül-e a feltétel. Ha igen, kilépek break-kel.
while True:
    utasitas
    if feltétel: - kilépési feltétel
    break 

"""
while True:
    jelszo= input("Kérem a jelszót: ")
    if jelszo == oldjelszo:
        break

print("Sikeres belépés!")

megfelelo= False
while not megfelelo:
    jelszo= input("Kérem a jelszót: ")
    if jelszo == oldjelszo:
        megfelelo= True

#írjunk egy játék programot. Találjunk ki egy számot 1 és 1000 között, és találjuk ki.
 
gondoltszam= random.randint(1,1000)
tipp = int(input("Kérem a tippet: "))
tippekszama = 1
while tipp != gondoltszam:
    if tipp<gondoltszam:
        print("nagyobb számra gondoltam")
    else:
        print("kisebb számra gondoltam")
    tipp = int(input("Kérem a tippet: "))
    tippekszama += 1

print(f"Gratulálok, eltalálta!  A tippek száma: {tippekszama}")


tippekszama=0
gondoltszam= random.randint(1,1000)
while True:
    tippekszama+=1
    tipp=int(input("Kérem a tippet: "))
    if tipp == gondoltszam:
        break
print(f"Gratulálok, eltalálta! Tippek száma: {tippekszama}")
