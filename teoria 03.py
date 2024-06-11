texto= "Curso de python"

#indica a letra que está na posição tal
print(texto)
print(texto[6])
print(texto[6:8]) #imprime a letra na posição 2 até a 6

#indica as letras que estão em determinado intervalo
print(texto[9:15:2]) #pto
print(texto[9:15]) #python
print(texto[:5]) #curso
print(texto[9:]) #python

#quantidade de caracteres no texto
print(len(texto))

#quantas vezes aparece determinada letra
print(texto.count("o"))
print(f"letras O: {texto.count('o')}")

#Procura em qual posição uma palavra está (obs: quando a resposta é -1, é pq não foi encontrado)
print(f"Existe python?: {texto.find('python')}")#9
print(f"Existe python?: {texto.find(' python')}")#8
print(f"Existe python?: {texto.find('python ')}")#-1

#Indica se tem tal palavra em uma rase (usando booleando)
print(f"{'python' in texto}") #true
print(f"{'python ' in texto}") #false
 
#troca a palavra
trocaTexto= texto.replace("python", "javascript")
print(trocaTexto)
print(texto)
print(f"Temos {texto} e {trocaTexto}, venha estudar com a gente!!!")

#texto todo minúsculo e maiusculo
textoMinusculo= texto.lower()
print(textoMinusculo)
textoMaiusculo= texto.upper ()
print(textoMaiusculo)

#altera o tamanho das letras
textoCapitalizado= texto.capitalize()
print(textoCapitalizado)
textoTitulo= texto.title()
print(textoTitulo)

#remove espaços
texto2= " senai 1 "
textoSemEspaco=texto2.strip()
print(texto2)
print(textoSemEspaco)

#junta texto
juntaTexto= '-'.join(texto)
print(juntaTexto)
juntaTexto2=''.join(texto)
print(juntaTexto2)

#divide texto
divideTexto= texto.split()
print(divideTexto)
