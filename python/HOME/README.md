# Notas

Un numeral sirve para poner un comentario al codigo
o sea es algo que la maquina no va a ejecutar

    #esto no se ejecuta solo sirve para
    #poner explicaciones o notas en el codigo

# Basic

Al tener python instalado la teminal sirve como una pequeña calculadora

    4

    >>>50 - 5*6
    20

    >>(50 - 5*6) / 4
    5.0

    >>>8 / 5  # toda divicion debuelve un froat(frotante)
    1.6
NOTA: si se desea usar la respuesta del ultimo vasta con poner _ y la operacion necesaria
## Operaciones basicas

    / | divicion
    // | divicion que retorna un entero
    + | - | * | suma resta multiplicacion
    ** | potencia
    % | el restante de una divicion

## Variables

para crear una variable basta con ponerele un nombre y igualarlo 

    numero1 = 1
    numero2 = 1+1
    >>>numero1 + numero2
    3
NOTA: al usar un fortante en una operacion con un entero siempre generara un frotante

al usar comillas simples o dobles se genera una variable tipo texto
    'lunes'
    "lunes"
NOTA: \n | sirve para pasar a la siguiente linea

en python se puede operar con cadenas de texto

    >>>3 * 'un' + 'ium'
    'unununium'

## arrays

Listas

    >>>squares = [1, 4, 9, 16, 25]

    >>>squares
    [1, 4, 9, 16, 25]

Es posible anidar listas (crear listas que contengan otras listas), por ejemplo:

    a = ['a', 'b', 'c']

    n = [1, 2, 3]

    x = [a, n]

    x
    [['a', 'b', 'c'], [1, 2, 3]]

    x[0]
    ['a', 'b', 'c']

    x[0][1]
    'b'
## ciclos

while
repite el bloque de codigo mientras la condicion sea verdadera

    while condicion:

for
El ciclo for se utiliza para iterar sobre una secuencia

    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(f"Me gusta la {fruta}")
