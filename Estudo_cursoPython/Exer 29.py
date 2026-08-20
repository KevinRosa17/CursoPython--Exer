km=float(input("Digite a velocidade(km): "))
if km>80:
    multa=(km-80)*7
    print("Velocidade acima da permitida")
    print("Multa de R$ {}".format(multa))
else:
    print("Velocidade dentro do limite")