#Maynor Eduardo Morales Chang- 1553025
#Santos Juan Diego Chuc Gutiérrez - 1532825
while True:
    print("Bienvenido al programa de conversion de unidades de medida")
    print("1.Conversion de unidades de temperatura")
    print("2.Conversion de unidades de longitud")
    print("3.Salir")
    op=int(input("Ingrese el numero de opcion que desea seleccionar:"))
    if op==1:
        while True:
            print()
            print("1.Convertir Fahrenheit a Celsius")
            print("2.Convertir de Celsius a Fahrenheit")
            print("3.Salir")
            op2=int(input("Ingrese el numero de opcion que desea seleccionar:"))
            if op2==1:
                fa=float(input("Ingrese la cantidad de grados Fahrenheit para convertir:"))
                conv=(fa-32)/1.8
                print(f"{fa} grados Fahrenheit es equivalente a {conv:.2f} grados Celsius")
            elif op2==2:
                ce=float(input("Ingrese la cantidad de grados Celsius para convertir:"))
                conv=(ce*1.8)+32
                print(f"{ce} grados Celsius es equivalente a {conv:.2f} grados Fahrenheit")
            elif op2==3:
                print("Regresando al menú")
                print()
                break
            else:
                print("Ingrese valores válidos")
    elif op==2:
        while True:
            print()
            print("1.Convertir de Kilometros a Metros")
            print("2.Convertir de Metros a Kilometros")
            print("3.Salir")
            op3=int(input("Ingrese el numero de opcion que desea seleccionar:"))
            if op3==1:
                km=float(input("Ingrese la cantidad de Kilometros que desea convertir a Metros:"))
                conv= (km*1000)
                print(f"{km} Kilometros es equivalente a {conv:.2f} Metros")
                print()
            elif op3 ==2:
                metros =float(input("Ingrese la cantidad de Metros que desea convertir a Kilometros:"))
                conv= (metros/1000)
                print(f"{metros} Metros es equivalente a {conv:.2f} Kilometros")
                print()
            elif op3 ==3:
                print("Regresando al menú")
                print()
                break
            else:
                print("Ingrese valores válidos")
                print()

    elif op==3:
        print("Muchas gracias por haber usado el programa, feliz día")
        break
    else:
        print("Porfavor Ingrese valores válidos")
        print()






