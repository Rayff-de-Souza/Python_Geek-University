"""
GEEK UNIVERSITY - Exercício
	- Faça um programa que mostre uma contagem regressiva na tela, iniciando em 10
	e terminando em zero, UTILIZANDO A ESTRUTURA WHILE; 
"""

from time import sleep

contador = 10
while contador != 0:
	print(contador)
	contador = contador - 1
	sleep(1)

