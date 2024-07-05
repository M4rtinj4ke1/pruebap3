from prueba3completa import *
import os, msvcrt

while True:
    print('GAXPLOSIVE')
    print('[1] Registrar pedido')
    print('[2] Listar todos los pedidos')
    print('[3] Buscar pedido por RUT')
    print('[4] Imprimir hoja de ruta')
    print('[5] Salir del programa')
    opc = input('Ingrese una opcion> ')

    if opc == "1":
        registrar_pedido()
    elif opc == "2":
        pass
    elif opc == "3":
        pass
    elif opc == "4":
        pass
    elif opc == "5":
        pass
    else:
        print ('ERROR, OPCION INCORRECTA')
    print('....presione una teclapara continuar....')
    msvcrt.getch()