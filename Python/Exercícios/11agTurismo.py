print("Bem vindx ao HojeTurismo!")
print("----------------------------------------")
print("Estamos com uma promoção incrível!\n")
print("Que tal comprar hoje e viajar pós pandemia?")
print("Garantindo uma experiência incrível com a família e com descontos mais incríveis ainda!")
print("\nApós escolher seu pacote, preencha abaixo.")
print("---------------------------------------------")

valorBruto = float(input("Digite o valor do pacote selecionado: R$ "))
quantPassageiros = int(input("Digite a quantidade de passageiros que moram na mesma casa: "))
catAssentos = input("Qual a categoria dos assentos? ").upper()
valorDesc = float(0)

if catAssentos == "ECONOMICA":
    if quantPassageiros >= 4:
        valorDesc = valorBruto * 0.95
    elif quantPassageiros == 3:
        valorDesc = valorBruto * 0.96
    else:
        valorDesc = valorBruto * 0.97
elif catAssentos == "EXECUTIVA":
    if quantPassageiros >= 4:
        valorDesc = valorBruto * 0.92
    elif quantPassageiros == 3:
        valorDesc = valorBruto * 0.93
    else:
        valorDesc = valorBruto * 0.95
elif catAssentos == "PRIMEIRA CLASSE":
    if quantPassageiros >= 4:
        valorDesc = valorBruto * 0.8
    elif quantPassageiros == 3:
        valorDesc = valorBruto * 0.85
    else:
        valorDesc = valorBruto * 0.9
valorMedio = valorDesc / quantPassageiros

print("\n---------------------------------------------------------------------")
print("O valor bruto do pacote contratado é: R$ {:.2f}".format(valorBruto))
print("O valor do pacote com desconto é: R$ {:.2f}".format(valorDesc))
print("O valor médio por viajante é: R$ {:.2f}".format(valorMedio))
