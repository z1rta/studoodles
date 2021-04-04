print("Produção multimídia")
print("--------------------------------------")

tipoAssinatura = input("Digite seu nível de assinatura\n[BASIC] [SILVER] [GOLD] [PLATINUM]: ").upper()
faturamentoCanal = float(input("Informe o faturamento anual de seu canal: R$ "))
bonus = float(0)

if tipoAssinatura == "BASIC":
    bonus = faturamentoCanal * 0.3
    print("O valor do bônus a ser pago é: R$ {:.2f}".format(bonus))
elif tipoAssinatura == "SILVER":
    bonus = faturamentoCanal * 0.2
    print("O valor do bônus a ser pago é: R$ {:.2f}".format(bonus))
elif tipoAssinatura == "GOLD":
    bonus = faturamentoCanal * 0.1
    print("O valor do bônus a ser pago é: R$ {:.2f}".format(bonus))
elif tipoAssinatura == "PLATINUM":
    bonus = faturamentoCanal * 0.05
    print("O valor do bônus a ser pago é: R$ {:.2f}".format(bonus))
