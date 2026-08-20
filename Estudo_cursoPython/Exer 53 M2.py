wrd=(input("Digite uma palavra:")).upper().strip()
palabre = wrd.split()
junto="".join(palabre)
inverso=""
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
print(junto,inverso)
if inverso==junto:
    print("Temos um palindromo")
else:
    print("Não temos um palindromo")




