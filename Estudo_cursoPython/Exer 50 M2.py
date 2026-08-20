import random
aux = 0
for i in range(0,6):
    num = random.randint(0, 10)
    print(num)
    if(num%2==0):
       aux+=num
print("A soma dos números pares dessa sequência é {}:".format(aux))