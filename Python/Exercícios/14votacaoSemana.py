# Qual dia da semana recebeu mais votos
print("VOTAÇÃO TURMA B - DATA DA LIVE")

seg = int(input("Segunda-feira: "))
ter = int(input("Terça-feira: "))
qua = int(input("Quarta-feira: "))
qui = int(input("Quinta-feira: "))
sex = int(input("Sexta-feira: "))

if ter < seg > qui and qua < seg > sex:
    print("Segunda-feira ganhou com {} votos.".format(seg))
elif qua < ter > sex and seg < ter > qui:
    print("Terça-feira ganhou com {} votos.".format(ter))
elif seg < qua > ter and qui < qua > sex:
    print("Quarta-feira ganhou com {} votos.".format(qua))
elif seg < qui > ter and qua < qui > sex:
    print("Quinta-feira ganhou com {} votos.".format(qui))
elif seg < sex > ter and qua < sex > qui:
    print("Sexta-feira ganhou com {} votos.".format(sex))
