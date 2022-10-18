import random

def lista():
    lista=[]
    for i in range(5):
        lista.append(int(input("Kérek egy számot: ")))
    print(lista)

    lista2=[]
    for i in range(7):
        while True:
            x=random.randint(1,95)
            if x not in lista2:
                break
        lista2.append(x)
    return lista2

    

def main():
    lista()
main()