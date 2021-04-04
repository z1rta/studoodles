# Votação para premiação do time
print("VOTAÇÃO CONSOLE DE PREMIAÇÃO")

voto1 = input("Digite o voto do 1º membro: ").upper()
voto2 = input("Digite o voto do 2º membro: ").upper()
voto3 = input("Digite o voto do 3º membro: ").upper()
voto4 = input("Digite o voto do 4º membro: ").upper()
voto5 = input("Digite o voto do 5º membro: ").upper()
consoleEscolhido = int(0)
playstation = int(0)
xbox= int(0)
nintendo = int(0)

if voto1 == "PLAYSTATION":
    playstation = playstation + 1
elif voto1 == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if voto2 == "PLAYSTATION":
    playstation = playstation + 1
elif voto2 == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if voto3 == "PLAYSTATION":
    playstation = playstation + 1
elif voto3 == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if voto4 == "PLAYSTATION":
    playstation = playstation + 1
elif voto4 == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if voto5 == "PLAYSTATION":
    playstation = playstation + 1
elif voto5 == "XBOX":
    xbox = xbox + 1
else:
    nintendo = nintendo + 1

if xbox < playstation > nintendo:
    print("Playstation ganhou com {} votos.".format(playstation))
elif playstation < xbox > nintendo:
    print("Xbox ganhou com {} votos.".format(xbox))
else:
    print("Nintendo ganhou com {} votos.".format(nintendo))
