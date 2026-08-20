num=k=soma=0
num = (int(input("Digite um número:")))
while num !=999:
    k+=1
    soma+=num
    num = (int(input("Digite um número:")))
print("Foram digitados {} números".format(k))
print("A soma de todos os números foram {}".format(soma))
