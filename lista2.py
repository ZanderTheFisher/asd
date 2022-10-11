import random
#lottó
def lottosorsol():
    szamok=[]
    for i in range(5):
        while True:
            x=random.randint(1,95)
            if x not in szamok:
                break
        szamok.append(x)
    return szamok

def main():
    for i in range(52):
        s1=lottosorsol()
        s1.sort()
        print((i+1),". hét: ",end="")
        print(*s1)

def f2():
    logikaiak=[]
    for i in range(7):
        if random.randint(1,2)==1:
            logikaiak.append(True)
        else:
            logikaiak.append(False)
    print(*logikaiak)

def kiírtartalom(l):
    for i in l:
        print(i)

def kiírrange(l):
    for i in range(len(l)):
        print(l[i])

def kiírstring(l):
    for c in l:
        print(c)
main()