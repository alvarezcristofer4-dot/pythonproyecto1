import requests 
from tabulate import tabulate
import mysql.connector

URL = 'https://restcountries.com/v3.1/region/America'

response = requests.get(URL)

if response.status_code == 200:
    print('conexion a api exitosa')
    data = response.json()
    rows = []
    for dic_user in data['results']:
        nombre = dic_user['name']['first'] +' '+ dic_user['name']['last']
        pais = dic_user['location']['country']
        email = dic_user['email']
        telefono = dic_user['phone']
        foto = dic_user['picture']['large']
        rows.append([nombre, pais, email, telefono, foto])
        
    headers = ['Nombre', 'Pais', 'Email', 'Telefono', 'Foto']
    print(tabulate(rows,headers,tablefmt='grid'))
    
    #CARGAMOS DATA EN LA BASE DE DATOS
    connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_g6'
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuario (
                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(255) NOT NULL,
                pais VARCHAR(255) NOT NULL,
                email VARCHAR(255),
                telefono VARCHAR(50),
                foto TEXT
            )
            """
        )
        #INSERTAMOS LOS USUARIOS A LA BD
        for usuario in rows:
            cursor.execute(
                """
                INSERT INTO usuario (nombre, pais, email, telefono, foto)
                VALUES (%s, %s, %s, %s, %s)
                """,
                usuario
            )
        connection.commit()
        connection.close()
        print(f'Registros importados a la base de datos') 
    else:
        print('Error al conectarse a la base de datos')   
else:
    print(f'error : {response.status_code}')