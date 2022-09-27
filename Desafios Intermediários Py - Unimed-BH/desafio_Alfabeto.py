#Dada a letra N do alfabeto, nos diga qual a sua posição.
import string
letra = input()
alfabeto=list(string.ascii_uppercase)
posicao=alfabeto.index(letra)
print(posicao+1)
