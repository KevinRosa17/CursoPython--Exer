from datetime import date
atual =date.today().year
nascimento = int(input("Digite seu ano de nascimento:"))
idade= atual-nascimento
print(idade)
if idade<=9:
    print("Mirim")
elif idade<=14 and idade>9:
    print("Infantil")
elif idade >14 and idade<=19:
    print("Junior")
elif idade>19 and idade<=20:
    print("Senior")
else:
    print("Master")
