l1=float(input("Digite o valor do lado 1:"))
l2=float(input("Digite o valor do lado 2:"))
l3=float(input("Digite o valor do lado 3:"))

if (l1<(l2+l3) and l1> abs(l2-l3)) and (l2<(l3+l1) and l1> abs(l3-l2)) and (l3<(l1+l2) and l2 >abs(l1-l3)):
    if l1 == l2 and l1 != l3:
        print("É um triãngulo isoceles")
    elif l2 == l1 and l2 == l3:
        print(" É um triângulo equilátero")
    else:
        print("É um triângulo escaleno")
elif 1<=0 or l2<=0 or l3<=0:
    print(" Não há triângulo com lado 0 ou valor negativo")
else:
    print("Não pode formar um triângulo")






