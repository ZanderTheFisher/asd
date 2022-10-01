#ciklusok: ismétlik, ameddig szeretnénk.
#for range: előírt lépésszámú, számolós ciklus. Annyiszor fut le amennyiszer szeretnénk.



def egyparaméteres():
    # "i" a ciklusváltozó: ez számolja, hogy hol tart a számolásban.
    for i in range(10): #az "i" értéke 0-tól 9-ig fog változni
        print(i) #ciklusmag , ez ismétlődik.
    for i in range(100):
        print(i, end= ". ")
        print("Süss fel nap")


def main():
    egyparaméteres()

main()

def második():
    #ha a rengeben 2 paraméter va, akkor az elsőtől indul a másodikig fut. A felső érték márnem
    for i in range(10,20):
        print(i)
def main():
    második()

def harmadik():
    #1. mettől 2. meddig 3. milyen lépésközzel
    for i in range(12,20,2):
        print(i)
def main():
    harmadik()






