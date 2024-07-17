# EX 05

# num1 = int(input('Digite o numero: '))

# d = num1 * 2
# t = num1 * 3
# p = num1 ** 0.5

# print(f'O seu numero é {num1}, o dobro dele é {d}, o triplo é {t} e a raiz é {p}')


# -------------------------------------------------------------------------------------------------


# EX 06

# n1 = int(input('Digite a primeira nota: '))
# n2 = int(input('Digite a segunda nota: '))

# m = (n1 + n2) // 2

# print(f'A sua média é {m}')


# -------------------------------------------------------------------------------------------------


# EX 07

# m = int(input('Digite o valor em metros: '))

# c = m * 100
# mi = c * 10

# print(f'O valor convertido para centimetros é {c} e em milimetros é {mi}')


# -------------------------------------------------------------------------------------------------


# EX 08

# n = int(input('Digite o valor desejado: '))
# i = 1

# while i <= 10:
#     print(f'{n} x {i} = {n * i}')
#     i += 1


# -------------------------------------------------------------------------------------------------


# EX 08
# n = int(input(f'Digite o valor desejado: '))

# for i in range(1, 11):
#     print(f'{n} x {i} = {n * i}')


# -------------------------------------------------------------------------------------------------


# EX 10

# v = int(input('Digite o valor que tem em reais: '))

# d = v / 3.27

# print(f'O valor em dolares é U${d:.2f}')


# -------------------------------------------------------------------------------------------------


# EX 11

# a = int(input(f'Digite a altura: '))
# l = int(input(f'Digite a largura: '))

# q = a * l

# print(f'A quantidade de tinta necessaria é {q // 2 :.2f}')


# -------------------------------------------------------------------------------------------------


# EX 12

# p = int(input('Digite o preço do produto: '))

# d = p * 0.95

# print(f'O preço com o desconto de 5% é R${d:.2f}')


# -------------------------------------------------------------------------------------------------


# EX 13

# s = int(input('Digite o salario do funcionario: '))

# n = s * 1.15

# print(f'O novo salario com o aumento de 15% é R${n:.2f}')


# -------------------------------------------------------------------------------------------------


# EX 15

# km = int(input('Digite a quantidade de km rodados: '))
# dia = int(input('Digite a quantidade de dias alugados: '))

# pkm = km * 0.15
# pdia = dia * 60

# print(f'O valor total será R${pkm + pdia:.2f}, o valor dos kms rodados são R${pkm:.2f} e o valor dos dias alugados são R${pdia:.2f}')


# -------------------------------------------------------------------------------------------------


# EX 16

# import math

# num = float(input('Digite um numero: '))

# print(f'A porção inteira do numero digitado é {math.floor(num)}')


# -------------------------------------------------------------------------------------------------


# EX 17

# import math

# co = float(input('Digite o valor do cateto oposto: '))
# ca = float(input('Digite o valor do cateto adjacente: '))

# print(f'O valor da hipotenusa é {math.hypot(co, ca):.2f}')


# -------------------------------------------------------------------------------------------------


# EX 18

# import math

# a = float(input('Digite o valor do angulo(1 a 360): '))

# s = math.sin(a)
# c = math.cos(a)
# t = math.tan(a)

# print(f'Seno: {s}\nCosseno: {c}\nTangente: {t}')


# -------------------------------------------------------------------------------------------------


# EX 19

# import random

# a1 = input('Digite o primeiro aluno: ')
# a2 = input('Digite o segundo aluno: ')
# a3 = input('Digite o terceiro aluno: ')
# a4 = input('Digite o quarto aluno: ')

# l = [a1, a2, a3, a4]

# e = random.choice(l)

# print(f'O escolhido foi: {e}')


# -------------------------------------------------------------------------------------------------


# EX 20

# import random

# a1 = input('Digite o primeiro aluno: ')
# a2 = input('Digite o segundo aluno: ')
# a3 = input('Digite o terceiro aluno: ')
# a4 = input('Digite o quarto aluno: ')

# a = 1

# l = [a1, a2, a3, a4]

# random.shuffle(l)

# print('A ordem sorteada foi: ')


# for i in range(0, 4):
#     print(f'{a}_{l[i]}')
#     a += 1
#     i += 1


# -------------------------------------------------------------------------------------------------


# EX 22

# n = input('Digite seu nome: ')
# l = len(n.replace(' ', ''))
# p = n.split()

# print(f'Nome todo maiusculo: {n.upper()}\nNome todo minusculo: {n.lower()}\nQtd de letras no nome: {l}\nQuantidade de letras do primeiro nome: {len(p[0])}')


# -------------------------------------------------------------------------------------------------


# EX 23

n = int(input('Digite um numero de 0 a 9999: '))

print(f'')