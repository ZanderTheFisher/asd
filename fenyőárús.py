def beolvas():
    f = open("fenyoarus.csv","r",encoding="UTF-8")
    lista = []
    for item in f:
        lista.append(item.strip())
    return lista

def osszead(lista):
    szum = 0
    for item in lista:
        sor = item.split(";")
        szum+=int(sor[2])
    print("2.: ",szum/len(lista))
    return szum


def kiir(lista):
    for item in lista:
        print(item)

def main():
    lista=beolvas()
    kiir(lista)
    print("1.: " , len(lista))
    osszead(lista)
main()