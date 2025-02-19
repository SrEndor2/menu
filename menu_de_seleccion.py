def es_anagrama(palabra1, palabra2):
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

def invertir_cadena(cadena):
    return cadena[::-1]

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def eliminar_duplicados(lista):
    return list(set(lista))

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]

def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def encontrar_mayor(lista):
    return max(lista)

def invertir_lista(lista):
    return lista[::-1]

def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]

def encontrar_segundo_mayor(lista):
    if len(lista) < 2:
        return None
    lista.sort(reverse=True)
    return lista[1]

def contar_vocales(texto):
    vocales = "aeiou"
    cuenta = 0
    for letra in texto.lower():
        if letra in vocales:
            cuenta += 1
    return cuenta

def ordenar_tuplas(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[1])

def contar_unicos(cadena):
    return len(set(cadena))

def palabras_mas_largas(texto, n):
    palabras = texto.split()
    palabras.sort(key=len, reverse=True)
    return palabras[:n]

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_hasta(n):
    primos = []
    i = 2
    while len(primos) < n:
        if es_primo(i):
            primos.append(i)
        i += 1
    return primos

# Menú
def mostrar_menu():
    print("\n--- Menú de Funciones ---")
    print("1. Anagrama")
    print("2. Invertir una cadena")
    print("3. Fibonacci")
    print("4. Eliminar duplicados")
    print("5. Palíndromo")
    print("6. Contar palabras")
    print("7. Encontrar el mayor elemento")
    print("8. Invertir una lista")
    print("9. Filtrar números pares")
    print("10. Encontrar el segundo mayor")
    print("11. Contar vocales")
    print("12. Ordenar una lista de tuplas")
    print("13. Contar caracteres únicos")
    print("14. Encontrar palabras más largas")
    print("15. Encontrar números primos")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (0-15): ")
        
        if opcion == "1":
            palabra1 = input("Ingresa la primera palabra: ")
            palabra2 = input("Ingresa la segunda palabra: ")
            print(f"¿Son anagramas? {es_anagrama(palabra1, palabra2)}")
        
        elif opcion == "2":
            cadena = input("Ingresa una cadena: ")
            print(f"Cadena invertida: {invertir_cadena(cadena)}")
        
        elif opcion == "3":
            n = int(input("Ingresa el valor de n: "))
            print(f"Fibonacci({n}) = {fibonacci(n)}")
        
        elif opcion == "4":
            lista = input("Ingresa una lista de números separados por espacios: ").split()
            lista = [int(x) for x in lista]
            print(f"Lista sin duplicados: {eliminar_duplicados(lista)}")
        
        elif opcion == "5":
            cadena = input("Ingresa una cadena: ")
            print(f"¿Es palíndromo? {es_palindromo(cadena)}")
        
        elif opcion == "6":
            texto = input("Ingresa un texto: ")
            print(f"Conteo de palabras: {contar_palabras(texto)}")
        
        elif opcion == "7":
            lista = input("Ingresa una lista de números separados por espacios: ").split()
            lista = [int(x) for x in lista]
            print(f"El mayor elemento es: {encontrar_mayor(lista)}")
        
        elif opcion == "8":
            lista = input("Ingresa una lista de elementos separados por espacios: ").split()
            print(f"Lista invertida: {invertir_lista(lista)}")
        
        elif opcion == "9":
            lista = input("Ingresa una lista de números separados por espacios: ").split()
            lista = [int(x) for x in lista]
            print(f"Números pares: {filtrar_pares(lista)}")
        
        elif opcion == "10":
            lista = input("Ingresa una lista de números separados por espacios: ").split()
            lista = [int(x) for x in lista]
            print(f"El segundo mayor es: {encontrar_segundo_mayor(lista)}")
        
        elif opcion == "11":
            texto = input("Ingresa un texto: ")
            print(f"Número de vocales: {contar_vocales(texto)}")
        
        elif opcion == "12":
            lista_tuplas = eval(input("Ingresa una lista de tuplas (ej. [(3, 2), (1, 3), (4, 1)]): "))
            print(f"Tuplas ordenadas: {ordenar_tuplas(lista_tuplas)}")
        
        elif opcion == "13":
            cadena = input("Ingresa una cadena: ")
            print(f"Caracteres únicos: {contar_unicos(cadena)}")
        
        elif opcion == "14":
            texto = input("Ingresa un texto: ")
            n = int(input("Ingresa el número de palabras más largas a encontrar: "))
            print(f"Palabras más largas: {palabras_mas_largas(texto, n)}")
        
        elif opcion == "15":
            n = int(input("Ingresa el número de primos a generar: "))
            print(f"Primeros {n} números primos: {primos_hasta(n)}")
        
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()