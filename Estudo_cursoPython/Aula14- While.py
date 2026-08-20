"""n=1
while n !=0:
 n=int(input("Digite um valor:"))
print("fim")"""

'''r="S"
while r=="S":
    n=int(input("Digite um valor:"))
    r=str(input("quer continuar S/N:")).upper()
print("fim")'''

n=1
aux=impar=0
while n!=0:
    n=int(input("Digite um valor:"))
    if(n%2==0):
        aux+=1
    else:
        impar+=1
print("Quantidade de números pares são de:{} e de números ímpares são de {}".format(aux,impar))


