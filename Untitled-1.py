#Convertir a mayusculas, quitar espacios y caracteres especiales e invertir palabra o frase
def palindromo(frase):
    normal = "".join(caracter.upper() for caracter in frase if caracter.isalpha())
    invertida = normal[::-1]
    return normal == invertida


#Solicitar palabra o frase
palabra_o_frase = input ("Ingresa palabra o frase: ")
resultado = palindromo(palabra_o_frase)


#Resultado
if resultado:
    print('"{palabra_o_frase}" es palindromo')
else:
    print('"{palabra_o_frase}" no es palindromo')