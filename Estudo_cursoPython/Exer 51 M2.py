a1=int(input("Digite o primeiro termo da progressão: "))
r=int(input("Digite a razão da progressão: "))

for i in range(0,10):
    an=(a1+i* r)
    print(an,end=" -> ")
print("acabou")
