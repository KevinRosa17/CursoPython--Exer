aux = 0
aux2=0
menorpeso=0
for k in range(1,6):
    peso=float(input("peso da {}ª pessoa: ༼ つ ◕_◕ ༽つ:".format(k)))
    if k==1:
        aux=peso
        aux2=peso
    else:
        if peso>aux:
            aux=peso
        if peso<aux2:
            aux2=peso

print("O maior peso lido foi {}".format(aux))
print("O menor peso lido foi {}".format(aux2))