# print("senai nami jafet")  #palavrinhas amarelas= comandos do próprio python
# #palavrinhas vermelhas= nomes 

nome = "maria estella" #palavrinhas azuis= variáveis que eu criei

salario = 1200.50
salarioBruto = 2050.33 #camecase
salario_bruto = 3300.25 #snakecase

print("Salario =" , salario)
salario = salario+ 150.00 #salario=1200.5+150=1350.50

print(salarioBruto)
print(salario_bruto)

# print("Salario Atualizado="+salario) CTRL+; (faz o comentário de tudo)

# print("*****OPERAÇÕES*****")
n1 = 10
n2 = 5

#soma
soma = n1+n2
print("Soma =", soma)
print("Soma=", str(n1+n2)) #jeito de simplificar e não criar tanta variável
print(f"soma")

#subtração
subtracao = n1-n2
print("Subtracao =", subtracao)
print("Subtracao=", str(n1-n2))

#multiplicacao
multiplicacao = n1 * n2
print("Multiplicacao=", multiplicacao)
print("Multiplicacao=", str(n1*n2))


#divisao
divisao = n1 / n2
print("Divisao=",divisao)
print("Divisao=", str(n1/n2))

# #OPERADOR DE DIVISÃO INTEIRA:
divisaoInteira= n1//n2
print("Divisao Inteira=", divisaoInteira)

potencia = n1 ** n2
print("Potencia=", potencia)

restoDivisao= n1%n2
print("Resto da divisao=", restoDivisao)

divInteira=5//2
print(f"Divisao 5/2={5/2}")

print("******LEITURA*******")

numeroInteiro= int(input("Digite um numero inteiro:"))
print(f"Numero digitado = {numeroInteiro}")

numeroReal= float(input("Digite um numero real:"))
print(f"Numero digitado = {numeroReal}")

booleano= bool(input("Digite um valor booleano:"))
print(f"Valor boleano digitado = {booleano}")

# #IDENTIFICAR O TIPO PRIMITIVO
variavel1= 345
print(type(variavel1))

variavel2= 1.89
print(type(variavel2))

variavel3= "djgifn"
print(type(variavel3))

variavel4= "false"
print(type(variavel4))

#ANÁLISE DE VARIÁVEL
texto= "12345"
print(texto.isnumeric())
print(texto.isalpha())

texto2= "anthony"
print(texto2.islower())
print(texto2.isupper())
