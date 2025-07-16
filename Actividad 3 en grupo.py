#Maynor Eduardo Morales Chang- 1553025
#Santos Juan Diego Chuc Gutiérrez - 1532825
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
                fa=float(input("Ingrese la cantidad de grados Fahrenheit para convertir:"))
                conv=(fa-32)/1.8
                print(f"{fa} grados Fahrenheit es equivalente a {conv} grados Celcius")
            elif op2==2:
                ce=float(input("Ingrese la cantidad de grados Celsius para convertir:"))
                conv=(ce*1.8)+32
                print(f"{ce} grados Fahrenheit es equivalente a {conv} grados Celcius")
            elif op2==3:
                print("Regresando al menú")
                break
            else:
                print("Ingrese valores validos")
    elif op==2:
        while True:
            print("1.Convertir de Kilometros a Metros")
            print("2.Convertir de Metros a Kilometros")
            print("3.Salir")
            op3=int(input("Ingrese el numero de opcion que desea seleccionar:"))
            if op3==1:
                km=int(input("Ingrese la cantidad de Kilometros que desea convertir a Metros:"))
                conv= (km*1000)
                print(f"{km} Kilometros es equivalente a {conv} Metros")
            elif op3 ==2:
                metros =int(input("Ingrese la cantidad de Metros que desea convertir a Kilometros:"))
                conv= (metros/1000)
                print(f"{metros} Metros es equivalente a {conv} Kilometros")
            elif op3 ==3:
                print("Regresando al menu")
                break
            else:
                print("Ingrese valores validos")

    elif op==3:
        print("Muchas gracias por haber usado el programa, feliz día")
        break








