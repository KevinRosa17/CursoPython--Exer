sexo=input("Digite o seu sexo M/F").strip().upper()[0]
while sexo not in "MnFf":
    sexo=input("Digite apenas M ou F: ").strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))