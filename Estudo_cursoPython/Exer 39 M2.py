from datetime import date
nm = int(input("Digite o ano do seu nascimento:"))
yr= date.today().year
idade=yr-nm

if idade==18:
    print("Está na hora de se alistar")
elif idade<18:
    print("Ainda não vai se alistar")
    temp = 18-idade
    print("faltanm {} anos para o alistamento".format(temp))
else:
    temp=idade-18
    print(" Já passou {} anos para o alistamento".format(temp))


