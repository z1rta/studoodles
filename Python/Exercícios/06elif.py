pontuacao = input("Insira a pontuação do cliente: ")
pontuacao = int(pontuacao)
if pontuacao >= 1000:
    print("O cliente ganhou 3gb adicionais em sua franquia de internet!")
elif pontuacao >= 500:
    print("O cliente ganhou 1,5gb adicionais em sua franquia de internet!")
elif pontuacao >= 200:
    print("O cliente ganhou 500mb adicionais em sua franquia de internet!")
else:
    print("O cliente não tem direito a pontos adicionais!")
