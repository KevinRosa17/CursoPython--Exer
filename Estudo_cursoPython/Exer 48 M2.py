'''n=587
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
print(a,b,c)'''

som=0
for c in range(1,500):
    if(c%2==1):
     aux = c
     somaalg=0
     for i in range(0,3):
        a= aux % 10
        aux=aux//10
        somaalg+=a
     if(somaalg%3==0):
         som=som+c
print(som)




