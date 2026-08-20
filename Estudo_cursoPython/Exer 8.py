# Exercício 8 - Conversor de medidas

md=float(input("Digite uma medida em (m) :"))
print("{} metros corresponte a\n km: {}\n hm: {}\n dam: {}\n dm: {}\n cm: {}\n mm: {}".format(md,md/1000,md/100,md/10,(md*10),(md*100),(md*1000)))