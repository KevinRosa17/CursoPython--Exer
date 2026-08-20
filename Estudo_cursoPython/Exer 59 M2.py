aux=0
choice=0
n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))
print("="*40)
print("Escolha um opção")
while choice !=5:
        print("[1] Somar\n"
              "[2] Multiplicar\n"
              "[3] Maior\n"
              "[4] novos números\n"
              "[5] sair do programa")
        print("="*40)
        choice=int(input("Escolha uma opção: "))
        if choice == 1:
            aux=n1+n2
            print("A soma entre {} + {} = {}".format(n1,n2,aux))
        elif choice ==2:
            aux=n1*n2
            print("A multiplicação entre {} x {} = {}".format(n1, n2, aux))
        elif choice ==3:
            if n1>n2:
                print("O maior número é {}".format(n1))
            else:
                print("O maior número é {}".format(n2))
        elif choice == 4:
            n1=float(input("Digite um novo número para N1: "))
            n2=float(input("Digite um novo número para N2: "))
        else:
            print("Finalizando...")


