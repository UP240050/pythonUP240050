#1. declarar edad como variable entera
Edad = int(19)
#2. declarar altura como variable flotante 
Altura = float(1.63)
#3. declarar una variable que almacene un número complejo
Y = 1 + 1j

#4. Ingresar valores para calcular área de un triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
print("El área del triángulo es: ", area) 

#5. Ingresar valores para calcular el perímetro de un recatángulo
lado1 = float(input("Ingrese el valor del primer lado del triángulo: "))
lado2 = float(input("Ingrese el valor del segundo lado del triángulo: "))
lado3 = float(input("Ingrese el valor del tercer lado del triángulo: "))
perimetro = lado1 + lado2 + lado3
print("El perímetro del triángulo es: ", perimetro)

#6. Ingresar valores para calcular el área y perímetro de un rectángulo
base = float(input("Ingrese valor de la base del rectángulo: "))
altura = float(input("Ingrese valor de la altura del rectángulo: "))
area = (base * altura)
perimetro = 2*(base + altura)
print("El área del rectángulo es: ", area)
print("El perímetro del rectángulo es: ", perimetro)

#7. Ingresar valores para calcular el área y circunferencia de un círculo 
radio = float(input("Ingrese el valor del radio del círculo: "))
Pi = 3.14
area = Pi * radio**2
c = 2 * Pi * radio
print("El área del círculo es: ", area)
print("La circunferencia del círculo es: ", c)

#8. calcular la pendiente
# Ecuación y = 2*x-2
pendiente =  2
#Intersección en y cuando x=0
intersección_y  = 2 * 0 - 2
#Intersección en x cuando y=0
# 0=2x-2
#2x=2
#x=1
interseccion_x = 1
print("La pendiente de la ecuación y=2x-2 es: ", pendiente)
print("La intersección en y es: ", intersección_y)
print("La intersección en x es: ", interseccion_x)

#9. Calcular la pendiente e hipotenusa 
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m = (y2-y1)/(x2-x1)
print("La pendiente entre los puntos (2,2) y (2,10) es: ", m)
import math
a=4
b=8
c2= (a**2)+(b**2)
c= math.sqrt(c2)
print("La hipotenusa mide: ", c)
#10. comparar las pendientes del ejercicio 8 y 9
print(pendiente > m)

#11. calcular el valor de y y que de 0
x = -3
y = x**2 + 6*x + 9
print ("El valor de y en y = x^2 + 6x + 9 cuando x=-3 es: ", y)
#12. encontrar la longitus de python y dragon y hacer una comparación falsa
print(len("python")<len("dragon"))
#13. usar el operador and para checar si on se encuentra en python y dragon
print("on" in "python" and "on" in "dragon")
#14. usar operador in para ver si jargon se encuentra en el enunciado
print("jargon" in "I hope this course is not full of jargon")
#15. no hay on en python y dragon
print("on" in "python" and "on" in "dragon")
#16. convertir python a valor flotante y string
(len("python"))
valor_flotante = float(len("python"))
print("El valor flotante de python es: ", valor_flotante)
valor_string = (len("python"))
print(valor_string)
#17. cómo saber si un número es par o impar
numero = int(input("Introduce un número: "))
resultado = ["Impar", "Par"][numero % 2]
print(f"El número es: {resultado}")
#18. ver si floor division de 7 y 3 es igual al valor entero de 2.7
floor_division=7//3
valor_entero =int(2.7)
resultado = floor_division==valor_entero
print ("¿floor division de 7 y 3 es igual al valor entero de 2.7? ", resultado)
#19. ver si "10" es igual a 10
x = (type("10"))
y = (type(10))
res = x == y
print("10 string y 10 int son iguales? ", res)
#20. ver si in 9.8 es gual a 10
a = int(9.8)
b = 10
result = a == b
print("¿int 9.8 es igual a 10? ", result)
#21. calcular salario
horas = int(input("Ingrese las horas que trabaja: "))
tarifa = int(input("Ingrese su pago por hora: "))
salario = horas * tarifa
print ("Su salario es de: $", salario)
#22. calcular segundos de vida de una persona al año
edad = int(input("Introduzca su edad: "))
seg_por_año= 3600*8760
seg_edad = seg_por_año * edad
print ("Usted ha vivido ", seg_edad, "segundos")
#23. tabla
for n in range(1, 6):
    print(f"{n}  {1}  {n**2}  {n**3}")