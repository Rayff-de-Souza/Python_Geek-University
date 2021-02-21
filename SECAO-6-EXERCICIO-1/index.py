"""
GEEK UNIVERSITY - Exercício
	- Faça um programa que leia os primeiros múltiplos de três, considerando números maiores que zero;

* Pequeno UP - A opção do usuário poder escolher quantos múltiplos deseja que o programa
mostre; 
"""

escolha = int(input("Quantos múltiplos de três deseja mostrar (> 0): "))

contador = 0
for n in range(0, escolha + 1):
	print(contador)
	contador = contador + 3
