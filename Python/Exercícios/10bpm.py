#AVALIAR SE O BATIMENTO POR MINUTO DO USUÁRIO ESTÁ DENTRO DA FAIXA ADEQUADA DE SUA IDADE.

print("Bem-vindo(a) à checagem de BPM do Health Track!")
print("------------------------------------------------------------")
print("Por gentileza, insira as informações solicitadas a seguir --")

resposta = "SIM"
while resposta == "SIM":
    idade = int(input("Digite sua idade: "))
    bpm = int(input("Com o auxilio de um aparelho, nos informe seu batimento por minuto: "))

    if 8 <= idade <= 17:
        if 80 <= bpm <= 100:
            print("Seu batimento está DENTRO da faixa adequada.")
        elif bpm < 80:
            print("Seu batimento está ABAIXO da faixa adequada.")
        else:
            print("Seu batimento está ACIMA da faixa adequada.")
    elif 18 <= idade <= 64:
        if 70 <= bpm <= 80:
            print("Seu batimento está DENTRO da faixa adequada.")
        elif bpm < 70:
            print("Seu batimento está ABAIXO da faixa adequada.")
        else:
            print("Seu batimento está ACIMA da faixa adequada.")
    elif idade >= 65:
        if 50 <= bpm <= 60:
            print("Seu batimento está DENTRO da faixa adequada.")
        elif bpm < 50:
            print("Seu batimento está ABAIXO da faixa adequada.")
        else:
            print("Seu batimento está ACIMA da faixa adequada.")

    resposta = input("Deseja realizar uma nova consulta? ").upper()
