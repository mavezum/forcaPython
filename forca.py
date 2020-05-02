from random import randrange
from forcaFigura import desenharFigura

possiveisPalavras = ["serie", "cobra", "python", "panda", "carteira", "livro", "mapa"]

#gera indice aleatorio
indiceAleatorio = randrange(len(possiveisPalavras))
palavra = possiveisPalavras[indiceAleatorio]

#print(palavra)

print('_'*len(palavra)) 

letrasAdvinhadas = []
tentativasTotais = 6
letrasErradas = 0
tentativasRestantes = tentativasTotais

while(tentativasRestantes > 0):
	letrasFaltando = 0
	print("Advinhe uma letra:")
	letraNova = input()

	#validando um unico caracter
	while((len(letraNova)!= 1)):
		print("Advinhe *somente* uma letra:")
		letraNova = input()

	letrasAdvinhadas = letrasAdvinhadas + [letraNova]

	#checar se a letra nova sequer existe n
	if(palavra.find(letraNova) < 0):
		letrasErradas = letrasErradas + 1

	tentativasRestantes = tentativasTotais - letrasErradas
	#checando se cada letra advinhada existem na palavra
	for letra in palavra:
		if letra in letrasAdvinhadas:
			print(letra, end="")
		else:
			print('_', end="")
			letrasFaltando = letrasFaltando+1

	print("")

	print("Letras advinhadas até agora:")
	print(letrasAdvinhadas)

	#usar a funcao desenharFigura
	desenharFigura(letrasErradas)

	#checar se restam alternativas
	if(tentativasRestantes < 1):
		print("Voce perdeu! Fim de jogo :(")
		break

	#checar se restam letras faltando
	if(letrasFaltando==0):
		print("Parabens! Voce ganhou!")
		break
