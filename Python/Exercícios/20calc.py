def somar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multip(x, y):
    return x * y


def divi(x, y):
    if b != 0:
        return x / y
    return 0

opcao = -1

while opcao != 5:
    print('BEM VINDX A NOSSA CALCULADORA!')
    print('~' * 30)
    print('[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n[5] - Sair')
    opcao = int(input('Digite qual operação deseja realizar: '))
    print('~' * 30)

    if opcao == 1:
        print('~~~~~~~~~~~~ SOMA ~~~~~~~~~~~~')
        print(calc.somar(float(input('Digite o primeiro valor: ')), float(input('Digite o segundo valor: '))))
    elif opcao == 2:
        print('~~~~~~~~~ SUBTRAÇÃO ~~~~~~~~~~')
        print(calc.subtrair(float(input('Digite o primeiro valor: ')), float(input('Digite o segundo valor: '))))
    elif opcao == 3:
        print('~~~~~~~ MULTIPLICAÇÃO ~~~~~~~~')
        print(calc.multip(float(input('Digite o primeiro valor: ')), float(input('Digite o segundo valor: '))))
    elif opcao == 4:
        print('~~~~~~~~~~ DIVISÃO ~~~~~~~~~~~')
        print(calc.divi(float(input('Digite o primeiro valor: ')), float(input('Digite o segundo valor: '))))
