#Exercício 15- Aluguel de carros

Km= float(input("Quilômetros rodados pelo carro (Km):"))
D=int(input("Dias alugados:"))
valor=(60*D+ (0.15*Km))
print("O total a ser pago é de R${:.2f}".format(valor))