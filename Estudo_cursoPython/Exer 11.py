#Exercício 11- Total de tinha a ser usado

lg= float(input("Digite a largura da sua parede:"))
la= float(input("Digite a altura da sua parede:"))
A=lg*la
print("Sua parede tem a dimensão de {}x{} e sua área é de {} m²".format(lg,la,A))
print("Para pintar essar parede,voê precisaá de {}L de tinta".format(A/2))