# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Olá Mundo")

#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input("digite um numero: ")
print("O número informado foi", numero)

# #3. Faça um Programa que peça dois números e imprima a soma.
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
print("A soma dos numeros é: ", numero1 + numero2)

#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = int(input("Digite a nota1: "))
nota2 = int(input("Digite a nota2: "))
nota3 = int(input("Digite a nota3: "))
nota4 = int(input("Digite a nota4: "))
print("A média é: ",(nota1 + nota2 + nota3 + nota4) / 2 )

#5. Faça um Programa que converta metros para centímetros.
centimetro = 1
print(f"{centimetro} metro é igual a {centimetro*100} centimetros")

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = int(input("Digite o valor do raio: "))
pi = 3.14
area =  pi * (raio*raio)
print(f'O valor da área do circulo é: {area} m')

#7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
area = int(input("Digite o valor do lado do quadrado: ")) * 4
print(f'A área do quadrado é {area}, e o dobro da área é: {area*2}')

#8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
mes = input("Digite o mês de referencia: ")
ganhoHora = float(input("Quando vc ganha por hora? "))
qtdhorames = float(input("Quantas horas trabalhadas no mês? "))
print("O total do salario no mês de {} é {:.2f} ".format(mes,ganhoHora * qtdhorames))

#9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
f = int(input("Digite a temperatura: "))
c = 5*((f-32)/9)
print(f'Temperatura em Fahrenheit {f}, temperadura em graus celsius  {c}')

#10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c = float(input("Digite a temperatura em graus celsius: "))
f = (c * 9/5) + 32
print(f'Temperatura em graus celsius {c}, temperadura em Fahrenheit {f}')


#11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o sugundo numero: "))
num_real = float(input("Digite um numero real: "))

print(f'Primeiro calculo: {(num1 * 2) + (num2/2)}')
print(f'Segundo calculo: {(num1 * 3) + num_real}')
print(f'Terceiro calculo: {num_real ** 3}')


#12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def calcula_peso():
     altura = float(input("Digite a sua altura: "))
     peso_ideal = (72.7*altura)-58
     return f'Seu peso ideal é: {peso_ideal:.2f}'
print(calcula_peso())

#13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

pessoa = input("Voce é homem ou mulher? ")
if pessoa == "Homem" or "homem":
     print(calcula_peso())
else:
     altura = float(input("Digite a sua altura: "))
     peso_ideal = (62.1*altura) - 44.7
     print(f'Seu peso ideal é: {peso_ideal:.2f}')


# 14 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

multa = float(4)
peso = float(input("Digite peso de peixes: "))
if peso > 50: # 50 limite estabelecido pelo estado
     excesso = peso - 50
     print(f'Peso: {peso:.2f} kg')
     print(f'Excesso peso: {excesso:.2f} kg')
     valor_multa = excesso * multa
     print(f'João deverá pagar R$ {valor_multa:.2f} de multa')
else: print(f'O peso foi {peso} kg, não houve excesso de peso!')

# 15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

print("*"*35)
mes = input("Digite o mês de referência: ")
ganhoHora = float(input("Quanto vc ganha por hora? "))
horas_trab_mes= float(input(f"Quantidade de horas trabalhadas no mes de {mes}: "))

salario = horas_trab_mes * ganhoHora
imposto_renda = 0.11 * salario
inss = 0.08 * salario
sindicato = 0.05 * salario
salario_liq = salario - imposto_renda - inss - sindicato
totaldesconto = imposto_renda + inss + sindicato
print(f'No mês de {mes} o seu salário foi R${salario:.3f}')
print(f'Desconto imposto de renda R$ {imposto_renda:.2f}')
print(f'Desconto INSS R$ {inss:.2f}')
print(f'Desconto sindicado R$ {sindicato:.2f}')
print(f'Total de desconto R$ {totaldesconto:.3f}')
print(f'O salário líquido é R$ {salario_liq:.3f}')
print("*"*35)


#16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


cobertura_tinta = 3
capacidade_lata = 18
preco_lata = 80.0

tamanho_area = int(input("Digite o tamanho da área a ser pintada em m²: "))

litros = tamanho_area / cobertura_tinta
latas_inteiras = int(litros/capacidade_lata)
if litros % capacidade_lata != 0:
    latas_inteiras += 1

valor_total = latas_inteiras * preco_lata
print(f'QTD litros necessários: {litros:.2f} l\n'
      f'Latas de tinta necessárias: {latas_inteiras} lt\n'
      f'Total da compra R$ {valor_total}')


# #17 Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


cobertura_tinta = 6
capacidade_lata = 18
preco_lata = 80.0

capacidade_galao = 3.6
preco_galao = 25.0

tamanho_area = int(input("Digite o tamanho da área a ser pintada em m²: "))

litros = tamanho_area / cobertura_tinta * 1.1
latas_inteiras = int(litros/capacidade_lata)
galao = int(litros/capacidade_galao)



valor_total_latas = latas_inteiras * preco_lata
valor_total_galao = galao * preco_galao

mixlatas = (litros / capacidade_lata)
mixgalao = (litros - mixlatas * capacidade_lata) / 3.6

if litros % capacidade_lata != 0:
    latas_inteiras += 1

print(f'QTD litros necessários: {litros:.2f} l\n'
      f'Latas de tinta necessárias: {latas_inteiras} lt\n'
      f'Total da compra R$ {valor_total}')

