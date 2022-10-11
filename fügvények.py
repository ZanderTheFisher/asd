def maxi(a,b):
    if a>b:
        return a
    else:
        return b





def faktorialis(n):
    fakt=1
    for i in range(1,n+1):
        fakt=fakt*i
    return fakt

def main():
    x=int(input("Add meg az első számot: "))
    y=int(input("Add meg a második számot: "))
    print(maxi(x,y))
    print(faktorialis(6))

main()