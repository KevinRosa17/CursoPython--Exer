import random
n1 = input("Digite o primeiro nome:")
n2 = input("Digite o Segundo nome:")
n3 = input("Digite o terceiro nome:")

lista=[n1,n2,n3]
escolhido = random.choice(lista)
print("O Aluno escolhido foi {}".format(escolhido))

from random import choice
n1 = input("Digite o primeiro nome:")
n2 = input("Digite o Segundo nome:")
n3 = input("Digite o terceiro nome:")
lista=[n1,n2,n3]
escolhido = choice(lista)
print("O Aluno escolhido foi {}".format(escolhido))