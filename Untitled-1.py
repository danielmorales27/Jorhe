from collections import Counter

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
def caracteres_no_iguales(frase):
    normal = ""

    for caracter in frase:
        if caracter.isalpha():
            normal += caracter.upper()

    # Contar frecuencia de cada letra
    frecuencia = Counter(normal)

    # Encontrar la letra mas comun
    letra_mas_comun = max(frecuencia, key=frecuencia.get)

    # Contar cuantas letras son diferentes 
    diferencias = sum(1 for letra in normal if letra != letra_mas_comun)

    print(f"Número de letras que no coinciden: {diferencias}")

# Llamar a la funcion despues del codigo principal
caracteres_no_iguales(palabra_o_frase)