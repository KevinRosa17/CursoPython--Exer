# Manipulação de texto
# Ex: Curso em Vídeo Python
#
# 1) identificar uma letra dentro de um texto -> frase[9] = V
# 2) pegar um tederminado numero de caracter  -> frase [9:13] = Víde
# 3) frase[9:21:2]-> começar no caracter 9 até o 21 pulando de 2 em 2
# 4) frase[:5] -> começa no  0 até o caracter 5
# 5) frase[15:] -> inicia no caracter 15 até o final do texto
# 6) frase[9::3]-> inicia no caracter 9 até o final pulando de 3 em 3
# 7) len(frase) -> mostra o comprimento da frase
# 8) frase.count('o') -> contar quantas vezes aparece a letra 'o'
# 9) frase.count('o',0,13) -> mostrar quantos 'o' tem entre o caracter 0 e 13
# 10)frase.find('deo) -> monstrar em que momento começa o deo
# 11) 'curso' in frase -> mostra se existe a palavra 'curso' dentro de frase
# 12) frase.replace('Python','Android') -> subistitui a palabra 'Python', por 'Android'
# 13) frase.upper() -> deixa tudo em maiusculo
# 14) frase.lower() -> deixa tudo em minúsculo
# 15) frase.capitalize() -> vai deixar todos os caracteres em minúsculo, mas a primeira fica em maiusculo
# 16) frase.title() -> vai analizar quantas palavras tem e deixar cada palavra com a primeira letra em maiúsculo
# 17) frase.strip() -> remove os espaços vazios do início e final
# 18) frase.rstrip()-> remove os espços da direita e mantes os da esquerda f
# 19) frase.lstrip() -> remove os espaços da esquerda e mantem os da direita
# 20) frase.split() -> ocorre uma divisão no texto, colocando as palavras dentro de
#                      uma nova lista, por exemplo, na frase curso em vídeo, curso
#                      possui numeração 01234, o em recomeça esse ciclo 01, Vídeo, 01234, Python 012345
# 21) '-'.join(frase) -> separar a frase

frase ="Curso em vídeo Python"
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15:21])

""" Meu deus se eu soubesse que dava pra escrever texto assim
eu não tinha enchido de hastag :)
"""
print(frase.count('o'))
print(frase.upper())
print(len(frase))
frase =frase.replace('Python', 'Android')
print(frase)
print (frase.split())


