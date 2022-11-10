def beolvasKetlista():
    global nevek
    global fizu
    f=open("emberek.txt", encoding="UTF8")
    nevek=[]
    fizu=[]
    for sor in f:
        nev=sor.split(";")[0]
        nevek.append(nev)
        fizu.append(int(sor.split(";")[1]))


def kiirKetlista(lista):
    for item in lista:
        print(item)

def kiirKetlista2():
    for i in range(len(nevek)):
        print(f"név: {nevek[i]}, fizu: {fizu[i]}")


def fajlbair():
    f=open("fizetesek.txt", "w", encoding="UTF8")
    for i in range(len(nevek)):
        f.write(f"név: {nevek[i]}, fizu: {fizu[i]}\n")


def main():
    beolvasKetlista()



main()