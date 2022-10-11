lista=[2,5,18,91,23,5] #van első, második, stb eleme
print(lista)
print(*lista,sep="; ")
print(lista[2])
x=int(input("Hanyadik számot szeretnéd látni"))
if x>len(lista):
    print("Nincs ennyi elem!")
else:
    print(lista[x-1])

lista4 = [1,2, "alma", True, 1.2, "körte"]
sumlist = lista+lista4
print(*sumlist)
multlist=lista*3
print(*multlist)
print(2 in lista)
if 2 in lista:
    print("A 2 benne van a listában")

print(2 not in lista)
print(*lista)
print(lista[2:4])
print(lista[2:])
print(lista[:3])
lista[2]=100
print(*lista)
lista.append(500) #hozzáűzni
print(*lista)

def feltolt():
    nevek=[]
    n=int(input("Hány név van a listában?"))
    for i in range(n):
        nevek.append(input("Add meg a kövi nevet"))

def kiír(l):
    for item in l:
        print(item,end=" ")
nevek=[]
feltolt(nevek)
kiír(nevek)

nevekb=[]
feltolt(nevekb)
kiír(nevekb)
nevekb.insert(2, "Kázmér")
kiír(nevekb)
nevekb.pop(2)
kiír(nevekb)
nevekb.remove("Kázmér")
kiír(nevekb)
print(nevekb[-1])
print(nevekb[len(nevekb)-1])
