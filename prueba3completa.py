import os, time, msvcrt, csv
pedidos = []

comunas = ('Puente Alto', 'Pirque', 'La pintana')
def registrar_pedido ():
    print ('REGISTRAR PEDIDO\nCLIENTE')
    rut = int(input('Ingrese rut: '))
    nombre = input('Ingrese nombre: ')
    direccion = input('Ingrese direccion: ')
    comuna = int(input('Indique numero de la comuna (1. Puente Alto, 2. Pirque, 3.La pintana): '))
    print('\nPEDIDO')
    cant_5kg = int(input('Indique cantidad de cilindros de 5kg: '))
    cant_15kg = int(input('Indique cantidad de cilindros de 15kg: '))
    total = cant_5kg*12500 + cant_15kg*25500
    pedido = {
        'rut':rut,
        'nombre':nombre,
        'direccion':direccion,
        'comuna':comunas[comuna-1],
        'cant_5kg':cant_5kg,
        'cant_15kg':cant_15kg,
        'total':total
    }
    pedidos.append(pedido)
    print('PEDIDO AGREGADO CON EXITO')
def listar_pedidos ():
    if not pedidos:
        print ('NO EXISTEN PEDIDOS')
    else:
        for p in pedidos:
            print('RUT:',p['rut'])
            print('NOMBRE:',p['nombre'])
            print('DIRECCION:',p['direccion'])
            print('COMUNA:',p['comuna'])
            print('CANT 5KG:',p['cant_5kg'])
            print('CANT 15KG:',p['cant_15kg'])
            print('TOTAL:',p['total'])
            print('-------------------------')

def buscar_pedido():
    if not pedidos:
        print ('NO EXISTEN PEDIDOS')
    else:
        print('BUSCAR PEDIDO POR RUT')
        buscarrut = int(input('Ingrese rut: '))
        rut_existe = False
        for p in pedidos:
            if buscarrut == p['rut']:
                rut_existe = True
                print('RUT:',p['rut'])
                print('NOMBRE:',p['nombre'])
                print('DIRECCION:',p['direccion'])
                print('COMUNA:',p['comuna'])
                print('CANT 5KG:',p['cant_5kg'])
                print('CANT 15KG:',p['cant_15kg'])
                print('TOTAL:',p['total'])
                print('-------------------------')
                return 
        if rut_existe==False: #if nor rut_existe
            print ('NO EXISTE')

def imprimir_ruta():
    if not pedidos:
        print('NO EXISREN PEDIDOS')
    else:
        comuna = int(input('Ingrese numero comuna (1. Puente Alto, 2. Pirque, 3.La pintana): '))
        nombre_archivo = input('Ingrese nombre del archivo: ') + ".csv"
        with open(nombre_archivo, 'w', newline='') as file:
            escritor = csv.DictWriter(file, ["rut",'nombre','direccion','comuna','cant_5kg','cant_15kg'])
            escritor.writeheader() #es para poner como titulo y poner lo de arriba rut, nombre etc
            for p in pedidos:
                if p['comuna']==comunas[comuna-1]:
                    escritor.writer(p)
        print('ARCHIVO GUARDADO CON EXITO')
