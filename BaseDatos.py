import os
import sqlite3


db_nm = "DatosCreate.db"
schema_filename  = "Crear_schema.sql"

db_is_new = not os.path.exists(db_nm)

#c= conn.cursor()
#result = cursor.execute(query , parameters)
with sqlite3.connect(db_nm) as conn:


    if db_is_new:
        print('Creating schema')
        with open(schema_filename , "rt" ) as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        conn.executescript("""


        insert into task (Nombres , Dorsal , Posicion , PasesBuenos , PasesTotales , Efectividad)
        values ('Emanuel Naval',' 2' , 'Delantero','0','0','0');

        insert into task (Nombres , Dorsal , Posicion , PasesBuenos , PasesTotales , Efectividad)
        values ('Julio Rodriguez',' 15','Arquero','0','0','0');

        insert into task (Nombres , Dorsal , Posicion , PasesBuenos , PasesTotales , Efectividad)
        values ('Sebastian Hernandez',' 18','Central','0','0','0');
        """)
    else:
        print('Database exists, assume schema does, too.')
