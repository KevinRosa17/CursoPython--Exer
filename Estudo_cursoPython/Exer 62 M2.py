a1=int(input("Digite um valor: "))
r=int(input("Digite o valor da razão: "))
c=termos=0
escolha=10
while escolha!=0:
    termos = termos + escolha
    while c<termos:
        an = (a1 + c * r)
        c+=1
        print(an,"-> " if c<termos else"FIM",end="")
    print()
    escolha=int(input("Quantos termos você quer mostrar a mais? "))
print(" O progresso foi finalizado com {} termos mostrados".format(termos))








