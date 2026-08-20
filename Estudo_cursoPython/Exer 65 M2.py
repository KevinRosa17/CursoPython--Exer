controle=''
aux=contador=comparador=0
while controle != "N":
    num=int(input(("Digite um número inteiro:")))
    aux+=num
    contador+=1
    if contador ==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num< menor:
            menor=num
    controle=(input("Deseja continuar S/N")).upper()
print("A média dos números digitados é de {}".format(aux/contador))
print("O maior número é {}".format(maior))
print("O menor número é {}".format(menor))
