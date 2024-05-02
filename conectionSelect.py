import pyodbc

# Establecer la conexión con la base de datos
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-Q2SVJUH\\SQLEXPRESS;'
    'DATABASE=TERMINAL1;'
    'Trusted_Connection=yes;'
)
 # datos  del servidor 


# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Ejecutar una consulta
cursor.execute('SELECT * FROM persona ')

# Obtener los resultados de la consulta
for row in cursor:
    print(row)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

