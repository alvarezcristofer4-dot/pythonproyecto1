import os
from time import sleep
"""
PROYECTO 1 : CRUD DE EMPRESAS
NOMBRE: CRISTOFER ALVAREZ QUISPE
"""

dic_empresas = {
    "300":{
        'razon_social':'Tecsup',
        'direccion' : 'calle perú 32'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        
        ruc = input("Ingrese RUC: ")
        razon_social = input("Ingrese Razón Social: ")
        direccion = input("Ingrese Dirección: ")
        dic_nuevo_empresa = {
            'razon_social': razon_social,
            'direccion': direccion,
        }
        dic_empresas[ruc] = dic_nuevo_empresa
        print("Empresa registrado existosamente")
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESA")
        print("=" * ANCHO)
        for ruc,info in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"RAZÓN SOCIAL : {info['razon_social']}")
            print(f"DIRECCIÓN : {info['direccion']}")
            print("-" * ANCHO)
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC del empresa a actualizar : ")
        if ruc in dic_empresas:
            print(f"empresa encontrado : {dic_empresas[ruc]['razon_social']}")
            nuevo_razon_social = input(f"NUEVO RAZÓN SOCIAL({dic_empresas[ruc]['razon_social']}) : ")
            nuevo_direccion = input(f"NUEVO DIRECCION({dic_empresas[ruc]['direccion']}) : ")
            if nuevo_razon_social:
                dic_empresas[ruc]['razon_social'] = nuevo_razon_social
            if nuevo_direccion:
                dic_empresas[ruc]['direccion'] = nuevo_direccion
            print("EMPRESA ACTUALIZADO EXITOSAMENTE!!!")
        else:
            print('No se econtro el empresa para el RUC ingresado')
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC del empresa a actualizar : ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print('EMPRESA ELIMINADO EXITOSAMENTE')
        else:
            print('No se econtro el EMPRESA para el RUC ingresado')
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(1)
        break
    else:
        print("OPCION NO VALIDA...")
    
    input("Presione ENTER para continuar...")
