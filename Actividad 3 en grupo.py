#Maynor Eduardo Morales Chang- 1553025
while True:
    print("Bienvenido a el programa de conversion de unidades de medida")
    print("1.Conversion de unidades de temperatura")
    print("2.Conversion de unidades de longitud")
    print("3.Salir")
    op=int(input("Ingrese el numero de opcion que desea seleccionar:"))
    if op==1:
        while True:
            print()
            print("1.Convertir Fahrenheit a Celsius")
            print("2.Convertir de Celsius a Fahrenheit")
            print("3.salir")
            op2=int(input("Ingrese el numero de opcion que desea seleccionar:"))
            if op2==1:
                fa=int(input("Ingrese la cantidad de grados Fahrenheit para convertir:"))
                conv=(fa-32)/1.8
                print(f"{fa} grados Fahrenheit es equivalente a {conv} grados Celcius")

            elif op2==2:
                ce=int(input("Ingrese la cantidad de grados Celsius para convertir:"))
            elif op2==3:
                print("Regresando al menú")
                break
            else:
                print("Ingrese valores validos")
                break
    elif op==2:
        while True:
            print("1.Convertir de Kilometros a Metros")
            print("2.Convertir de Metros a Kilometros")
            print("3. salir")
            op3=int(input("Ingrese el numero de opcion que desea seleccionar"))
            if op3==1:
                km=int(input("Ingrese la cantidad de kilometrtos que desea convertir a metros"))
                conv2= (km*1000)











