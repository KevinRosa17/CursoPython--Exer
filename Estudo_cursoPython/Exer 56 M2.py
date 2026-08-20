somaidade=0
contM=0
mvelho=0
name=""
for k in range (1,5):
   nm=input("Digite o seu nome: ")
   idade=int(input("Digite sua idade: "))
   sexo= (input("Digite seu sexo M/F: ")).upper().strip()
   if sexo not in["M","F"]:
       print("Opção invalida,encerrando programa")
       break
   elif sexo=="F":
       if idade<20:
        contM+=1
   else:
         if mvelho<=idade:
             mvelho = idade
             name=nm

   somaidade += idade
print("A média de idade desse grupo é {}".format(somaidade / 4))
print("A quantidade de mulheres como menos de 20 anos são {}".format(contM))
print("{} é o homem mais velho do grupo".format(name))



