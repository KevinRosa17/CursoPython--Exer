import math

catA= int(input("Digite o valor do Cateto Oposto: "))
catO = int(input("Digite o valor do Cateto Adjacente: "))
hip = math.sqrt(catA**2 + catO**2)
print("O valor da hipotenusa é igual a {}".format(hip))