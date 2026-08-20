N1=int(input("Digite um valor:"))
N2=int(input("Digite outro valor:"))

S=N1+N2
m=N1*N2
d=N1/N2
di= N1//N2
e = N1**N2
print("A soma é {}, \n o priduto é {} \n e a divisão é {:.3f}".format(S,m,d), end="")
print(" Divisão inteira {} e potência {}".format(di,e))
