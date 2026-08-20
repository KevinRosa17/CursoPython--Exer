import random

ch=["PEDRA","PAPEL","TESOURA"]
es=input("Digite pedra, papel ou tesoura para jogar contra o computador:").upper()
computador=random.choice(ch)
if computador==es:
    print("{}".format(computador))
    print("EMPATE")

elif computador != es:
    print("COMPUTADOR ESCOLHEU {}".format(computador))
    if computador== "PEDRA" and es=="TESOURA":
        print("COMPUTADOR VENCE")
    elif computador=="PEDRA" and es=="PAPEL":
        print("JOGADOR VENCE")
    elif computador== "TESOURA" and es == "PAPEL":
        print("COMPUTADOR VENCE")
    elif computador=="TESOURA" and es=="PEDRA":
        print("JOGADOR VENCE")
    elif computador=="PAPEL" and es=="TESOURA":
        print("JOGADOR VENCE")
    else:
        print("COMPUTADOR VENCE")

