num=int(input("Digite um número: "))
mult=1
while num>0:
     print(num,end="")
     print("x" if num>1 else "=",end="")
     mult*=num
     num-=1
print("{}".format(mult))

