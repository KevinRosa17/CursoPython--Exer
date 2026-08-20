vl= float(input("Digite o valor do produto R$: "))
print("======================================")
print("======Digite a forma de pagamento=====")
print("======================================")
print("[1] à vista dinheiro/cheque = 10% de desconto" )
print("[2] à vista no cartão = 5% de desconto" )
print("[3] em até 2x no cartão = preço normal" )
print("[4] 3x ou mais no cartão = preço normal" )
print("======================================")
num=int(input(("DIGITE UM NÚMERO:")))
if num not in (1,2,3,4):
    print("Opção inválida")

else:

    if num==1:
        vl = vl-(vl*0.10)
        print("Preço a ser pago {:.2f}".format(vl))
    elif num==2:
        vl = vl-(vl*0.05)
        print("Preço a ser pago {:.2f}".format(vl))
    elif num==3:
        div=vl/2
        print("Preço total R$: {:.2f}.Parcelamento de 2x: R$ {:.2f}".format(vl,div))
    else:
        par=int(input("Digite quantas vezes quer parcelar:"))
        pr=vl+(0.2*vl)
        div = (pr / par)
        print("Preço total R$: {:.2f}.Parcelamento de {}x: R$ {:.2f}".format(pr,par, div))


