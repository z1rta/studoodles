trasacao = float(input("Quantas transações financeiras você realizou hoje?  "))
i = 1
val = 0
soma = 0

while i <= trasacao:
    val = float(input("Qual o valor da {}o. transação? R$ ".format(i)))
    soma = soma + val
    i = i + 1

med = soma / trasacao
print("O valor total dos seus gastos hoje foi R$ {:.2f}".format(float(soma)))
print("A média dos seus gastos foi R$ {:.2f}".format(med))
