n1=float(input("Digite a N1:"))
n2=float(input("Digite a N2:"))
N3=float(input("Digite a N3:"))

md=(n1+n2+N3)/3
if md >= 7:
    print(" Aprovado")
elif md >=5 and md<= 6.9:
    print("Recuperação")
else:
    print(" Reprovado")
