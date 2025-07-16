#1
# for i in range(1, 11):
#     for k in range(1, 11):
#         print(f"{i} x {k} = {i * k}")

#2
# numero = int(input("Ingrese un número: "))
# suma = 0
# for i in range(1, numero + 1):
#     if i % 2 == 0:
#         suma += i
# print(f"La suma de los numeros pares desde 1 hasta {numero} es: {suma}")

#3
# nombres = []
# for i in range(10):
#     nombre = input("Ingrese un nombre: ")
#     nombres.append(nombre)
# print("Los nombres que empiezan con vocal son:")
# for nombre in nombres:
#     if nombre[0].lower() in "aeiou":
#         print(nombre)

#4  No se como realizarlo

#5  Sin usar random
# numeros=[]
# for i in range(20):
#     numero=int(input("Ingrese un numero random del 1 al 100:"))
#     numeros.append(numero)
# print("Los numeros multiplos de 3 son:")
# for numero in numeros:
#     if numero % 3==0:
#         print(numero)

#6
# while True:
#     contra=input("Ingrese su contraseña:")
#     if contra=="admin123":
#         print("contraseña correcta")
#         break
#     else:
#         print("Contraseña incorrecta, intentelo de nuevo")
#

#7
# for i in range(3):
#     contra=int(input("Ingrese su contraseña:"))
#     if contra==1963:
#         print("PIN correcto")
#     else:
#         print("PIN incorrecto")

#8
# numeros=[]
# while True:
#     numero=int(input("Ingrese los nunmero que desea para sacar el promedio (Solo funciona con positivos) :"))
#     if numero<0:
#         break
#     numeros.append(numero)
# promedio= sum(numeros)/ len(numeros)
# print(f"El promedio de los numeros ingresados es: {promedio}")

#9
# pasos=0
# while pasos <10000:
#     pasostiempo=int(input("Ingrese los pasos que ha echo en la ultima hora:"))
#     pasos += pasostiempo
#     print(f"Los pasos que llevas hasta el momento son: {pasos}")
# print("Felicidades ha alcanzado la meta de pasos diarios")

#10
# numero=77
# while True:
#     num=int(input("Ingresa un numero que crees que es el numero secreto :"))
#     if num<1 or num>100:
#         print("Ingrese un numero valido")
#         continue
#     elif num<numero:
#         print("El numero secreto es mayor")
#
#     elif num>numero:
#         print("El numero secreto es menor")
#     else:
#         print("Felicidades adivinaste el numero secreto")
#         break

#11-
# numeros = [3, 5, 1, 8, 2]
# mayor = numeros[0]
# for n in numeros:
#     if n > mayor:
#         mayor = n
# print("El número mayor es:", mayor)

#12
#
# figura=input("Ingrese que tipo de figura desea (circulo)(triangulo)(cuadrado):")
# pi=3.1416
# if figura=="circulo":
#     radio=float(input("Ingrese el radio del circulo:"))
#     area=pi*radio*radio
#     print(f"El area del circulo es: {area} u^2")
# elif figura=="triangulo":
#     base=float(input("Ingrese el tamaño de la base del triangulo:"))
#     altura=float(input("Ingrese el tamaño de la altura del triangulo:"))
#     area= base*altura/2
#     print(f"El area del triangulo es: {area} u^2")
# elif figura=="cuadrado":
#     lado=float(input("Ingrese el tamaño de los lados del cuadrado:"))
#     area=lado*lado
#     print(f"El area del cuadrado es {area} u^2")
#
# else:
#     print("Porfavor ingrese valores validos")

#13
# print("1.De celsius a Fahrenheit")
# print("2.De Fahrenheit a celcius")
# escala=int(input("Ingrese el numero de opcion que desea realizar: "))
#
# if escala==1:
#     grados=int(input("Ingrese la cantidad de grados Celcius que quiere convertir:"))
#     conversion=grados*9/5 +32
#     print(f"{grados} Grados Celcius equivale a {conversion} Grados Fahrenheit")
#
# elif escala==2:
#     grados=int(input("Ingrese la cantidad de grados Fahrenheit que quiere convertir:"))
#     conversion=(grados-32)/1.8
#     print(f"{grados} Grados Fahrenheit equivale a {conversion} Grados Celcius")
#
# else:
#     print("Ingrese datos validos porfavor")

#14
# texto=input("Ingrese el texto que desea verificar:")
# vocales="aeiouAEIOU"
# contador=0
#
# for i in texto:
#     if i in vocales:
#         contador+=1
# print(f"El texto conteiene {contador} vocales")

#15
# numero=int(input("Ingrese un numero para verificar si es primo:"))
# q=(numero%2)
# p=(numero%3)
# if q!=0 and p!=0:
#     print("El numero ingresado es un numero primo")
# else:
#     print("El numero ingresado no es un numero primo")

#16 No recuerdo con claridad POO
#17 No recuerdo con claridad POO
#18 No recuerdo con claridad POO
#19 No recuerdo con claridad POO
#20 No recuerdo con claridad POO

#21
# while True:
#     print("Menú de cálculos:")
#     print("1. Calcular área")
#     print("2. Convertir temperatura")
#     print("3. Salir")
#
#     opcion = input("Seleccione una opción: ")
#     if opcion == "1":
#         figura=input("Ingrese que tipo de figura desea (circulo)(triangulo)(cuadrado):")
#         pi=3.1416
#         if figura=="circulo":
#             radio=float(input("Ingrese el radio del circulo:"))
#             area=pi*radio*radio
#             print(f"El area del circulo es: {area} u^2")
#         elif figura=="triangulo":
#             base=float(input("Ingrese el tamaño de la base del triangulo:"))
#             altura=float(input("Ingrese el tamaño de la altura del triangulo:"))
#             area= base*altura/2
#             print(f"El area del triangulo es: {area} u^2")
#         elif figura=="cuadrado":
#             lado=float(input("Ingrese el tamaño de los lados del cuadrado:"))
#             area=lado*lado
#             print(f"El area del cuadrado es {area} u^2")
#
#         else:
#             print("Porfavor ingrese valores validos")
#     elif opcion== "2":
#         print("1.De celsius a Fahrenheit")
#         print("2.De Fahrenheit a celcius")
#         escala = int(input("Ingrese el numero de opcion que desea realizar: "))
#
#         if escala == 1:
#             grados = int(input("Ingrese la cantidad de grados Celcius que quiere convertir:"))
#             conversion = grados * 9 / 5 + 32
#             print(f"{grados} Grados Celcius equivale a {conversion} Grados Fahrenheit")
#
#         elif escala == 2:
#             grados = int(input("Ingrese la cantidad de grados Fahrenheit que quiere convertir:"))
#             conversion = (grados - 32) / 1.8
#             print(f"{grados} Grados Fahrenheit equivale a {conversion} Grados Celcius")
#
#         else:
#             print("Ingrese datos validos porfavor")
#
#     elif opcion== "3":
#         print("Saliendo del programa")
#         break
#
#     else:
#         print("Opcion no valida")

#22
# while True:
#     rol=input("Ingrese el rol que cumple en la universidad (administrador o estudiante) :")
#     curso=[]
#     notas=[]
#     if rol=="administrador":
#         print("1.Crear un curso")
#         print("2.Añadir una nota")
#         print("3.Salir")
#         opcion=int(input("Seleccione una opcion: "))
#         if opcion==1:
#             curs=input("Ingrese el nombre del curso a crear: ")
#             curso.append(curs)
#         elif opcion==2:
#             nota=int(input("Ingrese la nota del estudiante: "))
#             notas.append(nota)
#         elif opcion==3:
#             print("Terminando el programa")
#             break
#
#     elif rol=="estudiante":
#         print("1.Ver mis cursos")
#         print("2.Ver mis notas ")
#         print("3.Salir")
#
#         opcion=int(input("Seleccione una opcion: "))
#
#         if opcion==1:
#             print(curso)
#         elif opcion==2:
#             print(notas)
#         elif opcion==3:
#             print("Terminando el programa")
#             break

#23
# lista = []
#
# while True:
#     print("Menú de gestión de lista:")
#     print("1. Agregar elemento")
#     print("2. Buscar elemento")
#     print("3. Eliminar elemento")
#     print("4. Mostrar todos los elementos")
#     print("5. Salir")
#
#     opcion = input("Seleccione una opción: ")
#
#     if opcion == "1":
#         elemento = input("Ingrese el elemento a agregar: ")
#         lista.append(elemento)
#         print(f"Elemento '{elemento}' agregado.")
#
#     elif opcion == "2":
#         elemento = input("Ingrese el elemento a buscar: ")
#         if elemento in lista:
#             print(f"Elemento '{elemento}' encontrado.")
#         else:
#             print(f"Elemento '{elemento}' no encontrado.")
#
#     elif opcion == "3":
#         elemento = input("Ingrese el elemento a eliminar: ")
#         if elemento in lista:
#             lista.remove(elemento)
#             print(f"Elemento '{elemento}' eliminado.")
#         else:
#             print(f"Elemento '{elemento}' no encontrado.")
#
#     elif opcion == "4":
#         print("Elementos en la lista:")
#         for item in lista:
#             print("-", item)
#
#     elif opcion == "5":
#         print("Saliendo del programa.")
#         break
#
#     else:
#         print("Opción no válida.")

#24
# estudiantes = {}
#
# while True:
#     print("Menú de Sistema de Notas:")
#     print("1. Registrar estudiante")
#     print("2. Ingresar notas")
#     print("3. Consultar promedio")
#     print("4. Salir")
#
#     opcion = input("Seleccione una opción: ")
#
#     if opcion == "1":
#         nombre = input("Ingrese el nombre del estudiante: ")
#         estudiantes[nombre] = []
#         print(f"Estudiante {nombre} registrado.")
#
#     elif opcion == "2":
#         nombre = input("Ingrese el nombre del estudiante: ")
#         if nombre in estudiantes:
#             nota = float(input("Ingrese la nota: "))
#             estudiantes[nombre].append(nota)
#             print(f"Nota ingresada para {nombre}.")
#         else:
#             print("Estudiante no encontrado.")
#
#     elif opcion == "3":
#         nombre = input("Ingrese el nombre del estudiante: ")
#         if nombre in estudiantes and estudiantes[nombre]:
#             promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
#             print(f"El promedio de {nombre} es: {promedio}")
#         else:
#             print("Estudiante no encontrado o sin notas.")
#
#     elif opcion == "4":
#         print("Saliendo del programa.")
#         break
#
#     else:
#         print("Opción no válida.")

#25 No se como realizarlo
# tareas = []
#
# while True:
#     print("\nMenú de Tareas:")
#     print("1. Agregar tarea")
#     print("2. Marcar tarea como completada")
#     print("3. Ver tareas")
#     print("4. Salir")
#
#     opcion = input("Seleccione una opción: ")
#     if opcion == "1":
#         tarea = input("Ingrese la tarea: ")
#         tareas.append({"tarea": tarea, "completada": False})
#         print("Tarea agregada.")
#
#     elif opcion == "4":
#         print("Saliendo del programa.")
#         break
#     else:
#         print("Opción no válida.")
# 
