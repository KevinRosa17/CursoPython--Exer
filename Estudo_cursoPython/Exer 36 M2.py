print("==========================================")
print("===========EMPRESTIMO BANCÁRIO============")
print("==========================================")
nm=input("Digite o seu nome:")
sl= float(input("Digite seu salário R$:"))
cs= float(input("Digite o valor da casa:"))
tem= int(input("Digite o tempo em anos que deseja quitar a dívida :"))

vlp = cs/(tem*12)
ex = sl*0.3
print("===========================================")
print("Valor da prestação é de R$ {:.2f}/Mês".format(vlp))
if vlp> ex :
    print("Emprestimo negado")
else:
    print(" Parabéns {}, seu emprestimo foi aprovado".format(nm))