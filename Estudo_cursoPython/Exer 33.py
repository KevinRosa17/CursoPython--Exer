N1=int(input("Digite o primeiro número: "))
N2=int(input("Digite o segundo número: "))
N3=int(input("Digite o terceiro número:"))

if N1>N2 and N1>N3 and N2>N3:
    print("O maior número é {}".format(N1))
    print("O menor número é {}".format(N3))
elif N2>N1 and N2>N3 and N3>N1:
    print("O maior número é {}".format(N2))
    print("O nenor número é {}".format(N1))
elif N3>N1 and N3>N2 and N2>N1:
    print("O maior número é {}".format(N3))
    print("O nenor número é {}".format(N1))
