# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Olá Mundo")

#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input("digite um numero: ")
print("O número informado foi", numero)

#3. Faça um Programa que peça dois números e imprima a soma.
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