szöveg = "Ez egy hosszú szöveg a gyakorlás"

def f1(dec):
    bin = ""
    while dec > 0:
        maradek = dec % 2
        bin = str(maradek)+ bin
        dec = int(dec / 2)
    return bin
print(f1(4))