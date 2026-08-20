num= int(input("Digite um número: "))
k=3
fibo=0
fibo2=1
print("{}->{}".format(fibo, fibo2),end="")
while k<=num:
    fibo3=fibo+fibo2
    print("->{}".format(fibo3),end="")
    fibo=fibo2
    fibo2=fibo3
    k += 1





