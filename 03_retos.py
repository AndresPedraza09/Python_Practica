### Retos ###

"""
EL  FAMOSO FIZZ BUZZ
Escribe un programa que muestre por consola (con un print) los
numeros del 1 al 100 (ambos incluidos y conun salto de linea entre
cada impresion),sustituyendo los siguientes:
-Multiplos de 3  por la palabra "fizz".
-Multiplos de 5 por la palabra "buzz".
-Multiplos de 3 y de a 5 a la vez por la palabra  "fizzbuzz".
"""

def my_funcion ():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        
my_funcion()

"""
¿ES UN ANAGRAMA?

Escribe una funcion que reciba dos palabras (String) y retome
verdader o falso (Bool) segun sean o no anagramas.

-Un Anagrama consiste en formar una palabra reordenando TODAS 
    las letras de otra palabra inicial.
-NO hace falta comprobar que ambas palabras existan.
-Dos palabras exactamente iguales no son anagrama. 
"""

def is_anagrama(word_one, word_two):
    if word_one.lower() == word_two.lower():
       return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagrama("amor","roma"))

"""
Escribe un programa que imprima los 50 primeros numeros de la sucesion
de Fibonacci empezando en 0.
-La serie Fibonacci se compone por una susecion de numeros en
    la que el siguiente siemre es la suma de los dos anteriores
    0, 1, 1, 2, 3, 5, 8,13 ...
"""

def fibonacci():
    
    prev=0
    next=1

    for i in range(0, 50):
        print(prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()