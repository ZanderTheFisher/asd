#metódusok: minden metódus a def kulcsszóval vezetünk be.
#minden, ami a metódusokba kerülm egy tab-al bentebb kerül.

#def nev():
# utasítások

#metódusok meghívása a metódusok nevével történik + ()
#a metódusok csak akkor fut le, ha meghívjuk.

karakter = input("karakter: ")
if karakter >='a' and karakter<='z':
    print("Ez egy kisbetű")
    print("Nagybetűvel: ", (karakter+"").upper())
    print(ord(karakter))

def f25():
    karakter= input("karakter: ")
    if karakter >='a' and karakter<= 'z':
        print("ez egy kisbetű")
        print("Nagybetűvel: ", (karakter+"").upper())
        print(ord(karakter))
f25
#main metódus arra szolgál, hogy ebben legyen mindaz a metódus, amit futtatni akarunk.
def main():
    f25()

#
#
#a legvégén a maint hívjuk meg.
#kérjünk be a fizetést. Ha a fizu nagyobb, mint fél millio, kapjon 20%-os béremelést + írjuk ki az új fizut
#ha kisebb, mint flk millió, akkor 30%-os béremelést adjunk neki.



main()

def fizetésemelés():
    fizetés= (int(input("fizetése: ")))
    if fizetés< 500000:
        újfizu=fizetés*1.3
        print(f"új fizetés: {újfizu}")
    else:
        újfizu=fizetés*1.2
        print(f"új fizetés: {újfizu}")

def fizetésemelés():
    main()
main()

def main():
    döglötthöri=int(input("fizu: ")) #a döglötthöti értéke bekerül a fizu változóba, és azzal az értékkel
    fizetésemelés(döglötthöri)
    #metódus hívásakor a változó értéke kerül be ametódusba
main()

def téglalapterület(aoldal, boldal):
    terület= aoldal + boldal
    print(f"{aoldal} és {boldal}-oldalú téglalap területe: {terület}")

def main():
    téglalapterület(5,6)
    téglalapterület(8,10)
main()
    











