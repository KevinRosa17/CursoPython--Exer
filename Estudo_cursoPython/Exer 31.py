dt=float(input("Digite a distância da viagem (km):"))
if dt<=200:
    co=dt*0.5
    print("O preço da passagem é de R$ {}".format(co))
else:
    co=dt*0.45
    print("O prelo da passagem é de R$ {}".format(co))