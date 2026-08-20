a1=int(input("Digite um valor: "))
r=int(input("Digite o valor da razão: "))
c=0
while c<10:
    an = (a1 + c * r)
    c+=1
    print(an,"-> " if c <10 else "FIM", end="")
