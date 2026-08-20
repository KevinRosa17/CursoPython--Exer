#Exercício 12- Desconto de um produto

vl1=float(input("Qual é o valor do produto? R$:"))
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(vl1,vl1-(vl1*5)/100))