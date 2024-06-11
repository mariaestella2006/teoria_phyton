print('PROGRAMANDO EM BLOCOS')
#Usamos if e também else
#usamos ao seguine padrão:

# INSTRUÇÃO
# ENQUANTO CONDIÇÃO:
#     INSTRUÇÃO
#     SE CONDIÇÃO:
#             INSTRUÇÃO
#     SENÃO
#             INSTRUÇÃO
# INSTRUÇÃO

#estrutura CONDICIONAL
nota = float(input("Digite sua media:")) #criou variável

if nota>5: #os dois pontos declaram uma nova estrutura
    print(f"Você passou de ano!") #se for verdadeiro,essa mensagem vai aparecer
else:
    print(f"REPETIUR- Vai estudar seu mane")
print("FIM")#como esta mensagem está fora do bloco, ela ai aparecer indepedente se é verdade ou não

print('OPERADORES DE COMPARAÇÃO')
# x==x #true se os operandos forem iguais
# x!=y #true se os operandos não forem iguais
# x>y #true se o operando da esquerda for maior do que o da direita
# x<y #true se o operando da direita for maior do que o da esquerda
# x>=y #true se o operando da esquerda for maior ou igual do que o da direita
# X<=Y #true se o operando da direita for maior ou igual do que o da esquerda

print('OPERADORES LÓGICOS OR E AND')
#OR= O operador retorna true 

# or= amigão de todos (aceita tudp)
# and= perfeccionista

#EXEMPLO:
media= 5
if media>6:
    print("APROVADO!")
else:
    if media<3:
        print("REPROVADO")
    else:
        print("RECUPERAÇÃO")
        
# Media escola
# - Aprovado se  media maior ou igual a 7
# - faltas até 10

notaMedia = float(input("Digite sua média:"))

if notaMedia<=7:
    print(f"Você está aprovado")