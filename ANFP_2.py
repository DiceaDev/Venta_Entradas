# La ANFP requiere que usted desarrolle una aplicación en Python que permita registrar la venta de entradas a los estadios. La aplicación debe permitir la venta de entradas y entregar información estadística.
# Para tal efecto la ANFP ha enviado un conjunto de requerimientos que usted debe implementar en la aplicación.
# Requerimientos
# A.	Los datos para ingresar son: cantidad de entradas y tipo de entrada. El cajero ingresará para el tipo de entrada socio un 1 y para el tipo de entrada público general un 2.
# B.	El precio de la entrada para público general es de $8.500 y para socios tiene un descuento del 20%.
# C.	Una función debe recibir la cantidad de entradas y el tipo, luego debe calcular el total a pagar según el tipo de entrada, el resultado será enviado devuelta a la llamada de la función, para que ésta la muestre por pantalla.
# D.	La aplicación debe mostrar la cantidad entradas vendidas para socios y la cantidad de entradas vendida público general.
# E.	Cada vez que se realiza una venta la aplicación consulta al cajero si desea seguir vendiendo entradas, el cajero puede responder “si”, para continuar con otra venta o “no” para finalizar.


Socio = 0
P_General = 0
X = 's'

#Funcion que calcula el total a pagar
def calcular_total(Entradas,Tipo_Entrada):
    Descuento = 0.2
    Precio = 8500
    if Tipo_Entrada == 1:
        Total = (Tipo_Entrada * Precio) - ((Tipo_Entrada * Precio) * Descuento)
        print (f'Total a pagar: ${int(Total* Entradas)}') #Imprimimos el valor Publico General
        return Total, Entradas #Retornamos el total a pagar y la cantidad de entradas
    else:
        print(f'Total a Pagar: ${Precio * Entradas}') #Imprimimos el valor Publico General
        return  Precio, Entradas
#Aquí se ingresa la cantidad de entrada y el tipo de publico 
while X == "si" or X == "s" or X == "S":
        Entradas = int(input('Ingresa la cantidad de entradas: '))
        Tipo_Entrada = int(input("Selecciona el tipo de Entrada: [1]Socio [2]Publico general "))
        while Tipo_Entrada not in range(1,3):
            Tipo_Entrada = int(input("Ingrese una opción válida: [1]Socio [2]Publico General "))
        if Tipo_Entrada == 1:
            Socio = Socio + Entradas
            calcular_total(Entradas,Tipo_Entrada)
        else:
            P_General = P_General + Entradas
            calcular_total(Entradas,Tipo_Entrada)
        print (f'cantidad entradas vendidas para socios: {Socio}')
        print(f'cantidad entradas vendidas para Publico General: {P_General}')
        X = input("¿Quieres ingresar otra Venta? [s]Si o [n]No)")
