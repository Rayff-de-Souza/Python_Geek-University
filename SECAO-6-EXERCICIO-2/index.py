"""
GEEK UNIVERSITY - Exercício
	- Faça um programa que escreva de 1 até 100 duas vezes, sendo a primeira vez com o loop FOR e a
	segunda com o loop WHILE.
"""

print('FOR'.center(20, '_'))
for n in range(1, 101):
	print(n)
print('FOR'.center(20, '_'))

print('\n')

contador = 1
print('WHILE'.center(20, '_'))
while contador < 101:
	print(contador)
	contador = contador + 1
print('WHILE'.center(20, '_'))