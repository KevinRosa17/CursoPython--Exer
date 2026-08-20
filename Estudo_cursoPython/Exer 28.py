import random
num= random.randint(1,5)
nm2=int(input("Digite um número:"))
if nm2==num:
    print("Número escolhido pelo computador {}".format(num))
    print(" Parabéns você adivinhou o número escolhido!")
else:
    print("Número errado!!")
