import math

ang = float(input("Digite o valor do angulo:"))
rad= math.radians(ang)
fcs = math.sin(rad)
fcc = math.cos(rad)
fct = math.tan(rad)
print("O Seno,Cosseno e Tangente do ângulo {}º são respectivamente {:.2f}, {:.2f} e {:.2f}".format(ang, fcs, fcc, fct))
