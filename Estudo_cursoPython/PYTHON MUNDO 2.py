""" Condições Aninhadas"""

nome = input("Digite seu nome:").upper()
if nome== "KEVIN":
    print("Belíssimo nome")
elif nome == "LUCAS":
    print("Seu nome é bastante popular no Brasil")
elif nome in " ANA CLÁUDIA JÉSSICA JULIANA":
    print("Seu nome é bem bonito")
else:
    print("Seu nome é norma :/")
    print("Tenha um bom dia {}".format(nome.capitalize()))