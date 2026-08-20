import random
user=0
pc=(random.randint(0,10))
tentativas=0
while user!=pc:
    user=int(input("Digite um número de 0 a 10:"))
    if user<0 or user>10:
        print("TENTATIVA INVÁLIDA.Digite apenas números entre 0 e 10")
        continue
    tentativas+=1
print("Números Iguais {}={}".format(pc,user))
print("Foram necessárias {}".format(tentativas))
