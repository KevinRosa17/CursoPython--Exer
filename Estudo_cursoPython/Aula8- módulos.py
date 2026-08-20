# Aula 8 usando múdulos
# Exemplo : import bebidas <- todas as funcionalidades
#           from doce import pudim <- apenas funcionalidades que eu escolher
#
#
import math
num = int(input("Digite um número"))
raiz= math.sqrt(num)
print("A raiz de {} é igual a {:.2f}".format(num,raiz))

from math import sqrt
num = int(input("Digite um número"))
raiz= math.sqrt(num)
print("A raiz de {} é igual a {:.2f}".format(num,raiz))

import random
num= random.randint (1,10)
print(num)

import emoji

print(emoji.emojize(":thumbs_up:", language="alias"))
print(emoji.emojize(":red_heart:", language="alias"))
print(emoji.emojize("Olá mundo :earth_americas:", language="alias"))

