nombre = "Yaretzi"
apellido = "Macías"
nombre_completo = "Yaretzi Maacías"
país = "México"
ciudad =  "Agascalientes"
edad = 19
año = 2025
is_married = "no"
is_true = "si"
nombre, apellido, país, edad = "Yaretzi", "Macías", "México", "19"

#1. comprobar el tipo de datos de todas las variables
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(país))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
#2. Utilizar función len para para saber la longitud de tu nombre
print(len(nombre))
#3. comparar la longitud de tu nombre y tu apellido
print(len(nombre)<len(apellido))
#4. declarar 5 como num_1 y 4 como num_2
num_uno = 5
num_dos = 4
#5. sumar num_uno y num_dos y asignar el valor a variable total
Total = num_uno + num_dos
print(Total)
#6. restar num_dos menos num_uno y asignar el valor a variable diff
diff = num_uno - num_dos
print(diff)
#7. multiplicar num_uno por num_dos y asignar el valor a variable producto
producto = num_uno * num_dos
print(producto)
#8. dividir num_uno entre num_dos y asignar el valor a variable división
división = num_uno / num_dos
print(división)
#9. utilizar la división módulo para hallar num_dos entre num_uno y asignar el valor a variable remainder
remainder = num_dos % num_uno
print(remainder)
#10. calcular num_uno a la potencia de num_dos y asignar el valor a variable exp
exp = num_uno**num_dos
print(exp)
#11. hallar floor division de num_uno entre num_dos y asignar el valor a variable floor_division
floor_division = num_uno // num_dos
print(floor_division)
#12. radio de un círculo 30 metros
radio = 30
PI = 3.1416 
area_del_circulo = PI * radio**2
print(area_del_circulo)
D= 30*2
circunferencia_del_circulo = PI*D
print(circunferencia_del_circulo)
rad = float(input("Introduzca un valor para el radio: "))
area_circulo= PI * rad**2
print("El área del circulo es: ", area_circulo)
#13. utilizar la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario
print(input("Escriba su nombre "))
Nombre = "nombre"
print(input("Escriba su apellido "))
Apellido = "apellido"
print(input("Escriba su país de procedencia "))
País = "país"
print(input("Escriba su edad "))
edad = "edad"
