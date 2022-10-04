"""
paraméterlista: milyen értékeket várunk kivülről, 
def metodusnev(paraméterlista):


"""


def teglalapTerulet(aOldal, bOldal):
    terulet=aOldal*bOldal
    return terulet

def teglalapKerulet(aOldal,bOldal):
    return 2*(aOldal+bOldal)

def Csenge(szam):
    #ha csenge eljárás, akkor nem tér viissza értékkel, csak kiirja.
    print(szam*2)
    #ha Csenge függvény, akkor visszatér a szám kétszeresével.
    return szam*2

def faktorialis(szam):
    fakt=1
    for i in range(2,szam+1):
        fakt *= i
    return fakt    

def main():

    print("Fakt: ",faktorialis(5))
    ossz=0
    for i in range(1,100):
        print(f"{i} faktorálisa: {faktorialis(i)}")
        ossz += faktorialis(i)
    print("Összegük: ",ossz)    
    a=10
    b=12


    print("terület: ",teglalapTerulet(a,b))
    print(teglalapTerulet(5,8))

    print(teglalapKerulet(a,b))    
    ter= teglalapTerulet(10,20)
    print(ter)


main()