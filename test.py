# Definindo a string
string = "Ola mundo!"

# Convertendo a string em uma lista de caracteres
lista_caracteres = list(string)

# Invertendo a lista
lista_caracteres_invertida = []
for i in range(len(lista_caracteres)):
    lista_caracteres_invertida.append(lista_caracteres[len(lista_caracteres)-1-i])

# Convertendo a lista invertida de caracteres de volta em uma string
string_invertida = "".join(lista_caracteres_invertida)

# Imprimindo a string invertida
print(string_invertida)
