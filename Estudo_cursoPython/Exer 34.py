sl= float(input("Digite o seu salário R$:"))
if sl>1250:
    sl=(sl*0.1)+sl
    print("O novo salário é de R${:.2f}".format(sl))
else:
    sl=(sl*0.15)+sl
    print("O novo salário é de R${:.2f}".format(sl))