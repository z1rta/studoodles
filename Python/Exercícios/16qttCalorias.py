alimento = int(input("Quantos alimentos você consumiu hoje? "))
i = 1
cal = 0
soma = 0

while i <= alimento:
    cal = int(input("Quantas calorias tem o {}o. alimento? ".format(i)))
    soma = soma + cal
    i = i + 1

print("Você consumiu um total de {} calorias hoje.".format(float(soma)))
