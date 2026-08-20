from datetime import datetime
auxmaior=0
auxmenor=0
hj = datetime.now().year
for i in range(1,8):
    idade=int(input("Em que ano a {}º pessoa nasceu: ".format(i)))
    calc=hj-idade
    if calc>=18:
        auxmaior+=1
    else:
        auxmenor+=1
print("Ao todo tivemos {} pessoas maiores de idade:".format(auxmaior))
print("Ao todo tivemos {} pessoas maiores de idade:".format(auxmenor))

