from random import randrange
from math import floor
from forcaFigura import desenharFigura

palavras = ["carteira", "conversa", "python", "benhe", "programar", "cobra", "serie"]
palavraAleatoria = palavras[randrange(len(palavras))]
#print(palavraAleatoria)

print('_'*len(palavraAleatoria))

todasLetrasAdvinhadas = []
letrasErradas = 0
tentativasTotais = 6

#cada rodada do jogo
while(true):
	#Ler input do usuario
	print("Advinhe uma letra: ")
	letraNova = input()

	#Assegurar que somente uma letra foi digitada, e não varias
	while(len(letraNova)!=1):
		print("Advinhe somente uma unica letra!")
		letraNova = input()

	#Salvar letra advinhada nova
	todasLetrasAdvinhadas = todasLetrasAdvinhadas + [letraNova]
	
	#verificar se a letra nova existe na palavra
	if(palavraAleatoria.find(letraNova) < 0):
		letrasErradas = letrasErradas+1

	#escrever a palavra com os espacos em branco, ou as letras advinhadas
	letrasFaltando = 0
	for letra in palavraAleatoria:
		if letra in todasLetrasAdvinhadas:
			print(letra, end="")
		else:
			print('_', end="")
			letrasFaltando = letrasFaltando+1
	print("")


	tentativasRestantes = tentativasTotais - letrasErradas

	if(letrasFaltando==0):
		print("Parabens! Voce ganhou!")
		break
	
	desenharFigura(letrasErradas)
	print("Letras advinhadas:")
	print(todasLetrasAdvinhadas)

	if tentativasRestantes > 0:
		print("Voce ainda tem", tentativasRestantes, "alternativas")
	else:
		print("Voce perdeu!")
		break
