#Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português. Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico, amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. Antes que Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.

while True: 
  	try: 
					# TODO:	Programe aqui dentro as condições necessárias para satisfazer o problema
					# e imprima a saída de acordo com a situação das pernas do papagaio
					a=input()
					if a=="esquerda":
						print("ingles")
					elif a=="direita":
						print("frances")
					elif a=="nenhuma":
						print("portugues")
					elif a=="ambas":
						print("caiu")
						
		except EOFError: 
				break