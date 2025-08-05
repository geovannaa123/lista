"""Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês."""

vh= float(input('Qual o valor da hora aula? '))
ht= float(input('Quantas horas trabalhadas? '))
total= ht * vh

print(f'Com base na hora aula de {vh} e {ht} horas trabalhadas voce receberá o valor de:{total} ')