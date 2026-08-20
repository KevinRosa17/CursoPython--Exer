from datetime import date
yr=int(input("Digite o ano para saber se é bissexto ou digiti 0 para saber sobre o ano atual: "))
if yr==0:
    yr= date.today().year
if yr%4==0 and yr%100 !=0 or yr%400==0:

    print(" {} é bissexto".format(yr))
else:
    print("{} não é bissexto".format(yr))
