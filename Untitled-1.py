#Convertir a mayusculas, quitar espacios y caracteres especiales e invertir palabra o frase
def palindromo(frase):
    normal = ""
    for caracter in frase:
        if caracter.isalpha():
            normal += caracter.upper()
            invertida = ""
    for i in range(len(normal) - 1, -1, -1):
        invertida += normal[i]

 # Comparar ambas versiones
    return normal == invertida

#Solicitar palabra o frase
palabra_o_frase = input ("Ingresa palabra o frase: ")
resultado = palindromo(palabra_o_frase)


#Resultado
if resultado:
    print('"{palabra_o_frase}" es palindromo')
else:
    print('"{palabra_o_frase}" no es palindromo')