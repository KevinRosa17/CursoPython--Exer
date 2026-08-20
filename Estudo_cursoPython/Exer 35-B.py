import math
l1=float(input("Digite o valor do lado 1:"))
l2=float(input("Digite o valor do lado 2:"))
l3=float(input("Digite o valor do lado 3:"))

if (l1<(l2+l3) and l1> abs(l2-l3)) and (l2<(l3+l1) and l1> abs(l3-l2)) and (l3<(l1+l2) and l2 >abs(l1-l3)):
    print("É possível forma um triângulo")
else:
    print("Não é possível formar um triângulo")