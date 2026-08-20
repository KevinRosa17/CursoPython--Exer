num=int(input("Digite um valor inteiro qualquer: "))
print(" Digite a base de conversão")
print("===========================")
print("[1] binário")
print("[2] octal")
print ("[3] hexadecimal")
print("===========================")
ch=int(input("Digite um número"))

if ch==1:
    print("{} convertido para binário é igual a {}".format(num,bin(num)[2:]))
elif ch==2:
    print("{} convertido para octal é igual a {}".format(num,oct(num)[2:]))
else:
    print("{} convertido para hexadecimal é iagual a {}".format(num,hex(num)[2:]))

