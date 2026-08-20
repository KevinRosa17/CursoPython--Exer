fs=input("Digite uma frase: ").strip().upper()
print("A letra A aparece {} vezes na frase".format(fs.count('A')))
print("A letra A aparece na posição {} ".format(fs.find('A')+1))
print("A última letra A aparece na posição{}".format(fs.rfind('A')+1))