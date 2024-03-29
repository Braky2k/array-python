# -*- coding: utf-8 -*-
"""exercicios-arrays.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LyNJFONdMcAkhSP13DRVFIorDksnu0RN
"""

# Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

lista = []
contador = 0

for c in range(5):
  num = int(input('Digite um número: '))
  lista.append(num)
for i in lista:
  print(f'{contador} : {i}')
  contador += 1

# Ler uma lista de 10 números reais e mostre-os na ordem inversa que foram lidos.

lista = []

for c in range(10):
  n = float(input('Digite um número real: '))
  lista.append(n)

lista.reverse()

print(lista)

# Ler uma lista com 5 idades e exibir a maior e a menor.

lista = []

for i in range(5):
  idade = int(input('Digite a idade: '))
  lista.append(idade)

print(f'{max(lista)} anos é a maior idade apresentada.\n{min(lista)} anos é a menor idade apontada.')

# Inicialize uma lista de 10 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR.
# Imprima as listas PAR e IMPAR.

lista = []

for c in range(10):
  numero = int(input(f'Digite o {c+1}º número: '))
  lista.append(numero)

impar = [c for c in lista if c % 2 == 1]
par = [c for c in lista if c % 2 == 0]

print(f'Número Ìmpares: {impar}\nNúmero Par: {par}')

# Escreva um programa que troque o primeiro com o último elemento de uma lista qualquer.

lista = []
parar = 1

while parar != 2:
  num = input('Digite um número: ')
  parar = int(input('Deseja continuar?\n[ 1 ] Sim\n[ 2 ] Não\n\n'))
  while parar != 2 and parar != 1:
    parar = int(input('Deseja continuar?\n[ 1 ] Sim\n[ 2 ] Não\n\n'))
  lista.append(num)
  if parar == 2: break

lista[0], lista[-1] = lista[-1], lista[0]

print(f'A lista depois da alteração ficou da seguinte forma: {lista}')

[[1 + j*4 + i for i in range(4)] for j in range(3)]

# O código fica da seguinte forma pois J esta sendo repetido 3 vezes.
# Como a contagem começa do 0 o j recebe mais 1.
# a variável j se multiplica por 4, por ser o mesmo range do contador i.
# se o contador i fosse outro número, deveria também alterar a multiplicação do j

# Considere que você recebe um dicionário contendo informações sobre produtos em uma loja.
# Cada chave do dicionário é o nome de um produto e cada valor é uma tupla contendo o preço e a quantidade em estoque desse produto.
# Você deve criar um programa em Python que solicite ao usuário que insira um preço máximo.
# Em seguida, o programa deve imprimir os produtos cujo preço seja menor ou igual ao preço máximo inserido pelo usuário.

produtos = {
    'camiseta': (25.00, 10),
    'calça': (45.00, 5),
    'sapato': (60.00, 3),
    'boné': (15.00, 8)
}

preco = float(input('Digite o preço que gostaria de gastar: R$'))

for x in produtos:
  if produtos[x][0] <= preco: print(f'{x.title()} disponível para a compra!')

# Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média.
# Conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
# As notas não são informadas em ordem crescente ou decrescente.

#TITULO
print('-' * 50)
print('AVALIAÇÃO DO ATLETA'.center(50))
print('-' * 50)

#Dicionário
placar = {'nome': '', 'notas': []}

#Adicionando as notas
placar['nome'] = input('Digite o nome do ginasta: ').title().strip()
for i in range(4): placar['notas'].append(float(input(f'→ Digite a nota do {i+1}º jurado: ')))

#Maior e menor nota
maxima = max(placar['notas'])
minima = min(placar['notas'])

#Excluindo a maior e menor nota
placar['notas'].remove(maxima)
placar['notas'].remove(minima)

#Calculando a média
placar['media'] = sum(placar['notas']) / len(placar['notas'])

print('=-=' * 11)

# Impressão dos dados
print(f'''Dados do Participante\n
Nome: {placar['nome']}
Maior nota: {maxima}
Menor nota: {minima}
Média: {placar['media']}''')