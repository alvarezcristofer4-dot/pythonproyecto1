import os
from time import sleep
"""
PROYECTO 1 : CRUD DE EMPRESAS
NOMBRE: CRISTOFER ALVAREZ
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
        
        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese Nombre: ")
        email = input("Ingrese Email: ")
        dic_nuevo_EMPRESA = {
            'nombre': nombre,
            'email': email
        }
        dic_EMPRESAs[dni] = dic_nuevo_EMPRESA
        print("EMPRESA registrado existosamente")
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESA")
        print("=" * ANCHO)
        for dni,info in dic_EMPRESAs.items():
            print(f"DNI : {dni}")
            print(f"Nombre : {info['nombre']}")
            print(f"Email : {info['email']}")
            print('*' * ANCHO)
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR  EMPRESA")
        print("=" * ANCHO)
        dni = input("Ingrese DNI del EMPRESA a actualizar : ")
        if dni in dic_EMPRESAs:
            print(f"EMPRESA Encontrado : {dic_EMPRESAs[dni]['nombre']}")
            nuevo_nombre = input(f"NUEVO NOMBRE({dic_EMPRESAs[dni]['nombre']}) : ")
            nuevo_email = input(f"NUEVO EMAIL({dic_EMPRESAs[dni]['email']}) : ")
            if nuevo_nombre:
                dic_EMPRESAs[dni]['nombre'] = nuevo_nombre
            if nuevo_email:
                dic_EMPRESAs[dni]['email'] = nuevo_email
            print("EMPRESA ACTUALIZADO EXITOSAMENTE!!!")
        else:
            print('No se econtro el EMPRESA para el DNI ingresado')
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        dni = input("Ingrese DNI del EMPRESA a actualizar : ")
        if dni in dic_EMPRESAs:
            del dic_EMPRESAs[dni]
            print('EMPRESA ELIMINADO EXITOSAMENTE')
        else:
            print('No se econtro el EMPRESA para el DNI ingresado')
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(1)
        break
    else:
        print("OPCION NO VALIDA...")
    
    input("Presione ENTER para continuar...")
