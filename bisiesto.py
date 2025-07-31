''''
Determinar si un year es bisiesto
'''


year = int(input("Ingrse el year que desea verificar"))
if year % 4 == 0 and(year % 100 !=0 or year  % 400 == 0 or year % 100 == 0):
    print('El year',year,'es un year bisicesto')
else:
    print('El year ',year,'no es un year bisicesto')

#Aplicar descuento segun la cantidad de productos comprados. Cada producto cusra $100.000.

cantidad = int(input('Digite la cantidad de productos comprados:'))

if cantidad > 0:
    total = cantidad * 100000

    if 5 <= cantidad <= 20:
        total *=0.99
    elif cantidad <= 50:
            total *= 0.97
    elif cantidad <= 100:
            total *= 0.93
    elif cantidad > 100:
            total *=0.90
    print('El total a pagar es igual a ${}'.format(total))
else:
    print('Ha digitado una cantidad invalida.')

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def division(a,b):
    return a/b
def multiplicacion(a,b):
    return a*b
""""Calculo de el area de un triangulo usando la fprmula: A=(base*altura)/2"""

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la aaltura del triangulo:"))

area = (base * altura)/2

print("El area del triangulo es:",area)


def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): El peso de la persona en kilogramos.
        altura (float): La altura de la persona en metros.

    Returns:
        float: El valor del IMC calculado.
    """
    return peso / (altura * altura)

def nivel_de_peso(imc):
    """
    Clasifica el nivel de peso de una persona según su IMC.

    Args:
        imc (float): El valor del Índice de Masa Corporal.

    Returns:
        str: La clasificación del nivel de peso (ej. "bajo peso", "normal").
    """
    if imc < 18.5:
        return "bajo peso"
    elif 18.5 <= imc < 25:
        return "normal"
    elif 25 <= imc < 30:
        return "sobrepeso"
    else:
        return "obesidad"

# Solicitar al usuario que ingrese su peso y altura
try:
    peso_usuario = float(input("Ingresa tu peso en kilogramos: "))
    altura_usuario = float(input("Ingresa tu altura en metros: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa números para el peso y la altura.")
else:
    # Calcular el IMC
    imc_calculado = calcular_imc(peso_usuario, altura_usuario)

    # Obtener el nivel de peso
    clasificacion_peso = nivel_de_peso(imc_calculado)

    # Imprimir el resultado
    print(f"Su IMC es: {imc_calculado:.2f}") # Se formatea a 2 decimales para una mejor lectura
    print(f"Su nivel de peso es: {clasificacion_peso}")

# Solicitar al usuario que ingrese el tiempo en segundos
try:
    segundos_totales = int(input("Dime el tiempo en segundos: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
else:
    # Calcular los minutos totales
    minutos_totales = segundos_totales // 60

    # Calcular los segundos restantes
    segundos_resto = segundos_totales % 60

    # Calcular las horas
    horas = minutos_totales // 60

    # Calcular los minutos restantes
    minutos_resto = minutos_totales % 60

    # Imprimir el resultado
    print(f"{horas} horas, {minutos_resto} minutos, {segundos_resto} segundos")

# Solicitar al usuario que ingrese las tres notas
try:
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
except ValueError:
    print("Entrada inválida. Por favor, ingrese números para las notas.")
else:
    # Calcular el promedio de las notas
    promedio = (nota1 + nota2 + nota3) / 3

    # Mostrar el promedio
    print(f"El promedio de las notas es: {promedio:.2f}")

    # Verificar si el alumno aprueba o reprueba
    if promedio >= 3.0:
        print("¡Felicidades! El alumno ganó la materia.")
    else:
        print("Lo siento, el alumno perdió la materia.")

import random
aleatorio = random.randint(1,100)

while True:
    num = int(input("Ingrese un numero entre 1 y 100"))
    if num == aleatorio:
        print("Felicidades adivinaste el numero!")
    elif num < aleatorio:
        print("El numero es mayor, Intenta nuevamente")
    else:
        print("El numero es menor, Intenta nuevamente")
print("Fin del juego!")
    
        

#Leer dos numeros enteros y determinar cual es el mayor

a = int(input("Ingresa un numero:"))
b = int(input("Ingresa otro numero:"))

if a == b:
    print("Los numeros son iguales")
else:
    if a > b:
        print(f"El numero mayor es:{a}")
    else:
        print(f"El numero mayor es:{b}")
        

''''Determinar si un numero es par o impar '''
print("Ingrese el numero a comprobar")
num = int(input())
if num % 2 == 0:
    print("El numero",num,"Es par")
else:
        print("El numero ",num,"Es Impar")

# Solicitar al usuario que ingrese la temperatura en grados Celsius
try:
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número.")
else:
    # Convertir Celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Convertir Celsius a Kelvin
    kelvin = celsius + 273.15

    # Imprimir los resultados
    print(f"{celsius}°C es igual a {fahrenheit}°F")
    print(f"{celsius}°C es igual a {kelvin}K")
