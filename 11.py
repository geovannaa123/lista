"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
n1= int(input('Insira um numero inteiro '))
n2= int(input('Insira um numero inteiro '))
n3= float(input('Insira um numero real '))

#dobro do primeiro com metade do segundo
produto=(n1 * 2 ) + (n2/2)

#soma do triplo do primeiro com o terceiro
soma= (n1 * 3 ) + n3

#o terceiro elevado ao cubo
cubo= n3**3

print(f'o produto do dobro do primeiro com metade do segundo: {produto}')
print(f'a soma do triplo do primeiro com o terceiro: {soma}')
print(f'o terceiro elevado ao cubo: {cubo}')

