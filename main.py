#from conectionSelect import conn
import pyodbc

# Establecer la conexión con la base de datos
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-Q2SVJUH\\SQLEXPRESS;'
    'DATABASE=TERMINAL1;'
    'Trusted_Connection=yes;'
)

try:

    cursor = conn.cursor()
    with conn.cursor() as cursor:
        cursor.execute("select * from Personas")


        resultado= cursor.fetchone()


        while resultado:
            print(resultado)
            resultado = cursor.fetchone() 
    
    while True:
        actualizar= input ("\n quieres actualizar un registro s/n")
        if actualizar.lower() == "s":
            with conn.cursor() as cursor:
                idl = input ("ingresa el id del registro que desa modificar:")
                consultaverificacion=("select PersonaID from Personas where PersonaID = ?;")
                cursor.execute(consultaverificacion,(idl))
                resultado= cursor.fetchone()
                print (resultado)

                if resultado:
                    nombre = input ("inrese su nuevo nombre:")
                    apellido = input ("ingrese su nuevo apellido:")

                    consultau="update Personas set Nombre = ?, Apellido = ? where PersonaID =?"
                    cursor.execute(consultau,(nombre,apellido,idl))

                    cursor.commit()

                    print("su reguistro se actualizo correctamente")
                else:
                    print("el id ingresado es incorrecto")
        else:
            print("salio de la actualizacion o modificacion de los registros")
            break
    while True:
        eliminar = input ("\n quieres eleminar un registro s\n:")         
        if eliminar.lower() == "s":
            idl = input ("ingresa el id del registtro que desea eliminar:")
            consultaverificacion = ("select id from login where id = ? ;")
            cursor.execute(consultaverificacion,(idl))
            resultado = cursor.fetchone()
            print(resultado)
            if resultado:
                consultad = "delete from login where id = ?,"
                cursor.execute(consultad,(idl))

                cursor.comit()
                print ("su reguistro se elimino correctamente ")
            else:
                print("el id ingresado es incorrecto")
        else:
            print ("salio de la eliminacion de los registros")
            break
except Exception as e:
    print ("ocurrio un error ",e)

                


