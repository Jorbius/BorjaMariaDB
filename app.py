import pymysql

conn = pymysql.connect(host="db", user="root", password="root", database="database")

cur = conn.cursor()

borrar = f"DROP TABLE IF EXISTS database.alumnos"

create = f"CREATE TABLE alumnos (nombre VARCHAR(30), edad INTEGER)"

insert = f"INSERT INTO alumnos (nombre, edad) VALUES ('Joseba', 21)"
#insert2 = f"INSERT INTO alumnos (nombre, edad) VALUES ('Janire', 21)"
#insert3 = f"INSERT INTO alumnos (nombre, edad) VALUES ('Gaizka', 21)"
#insert4 = f"INSERT INTO alumnos (nombre, edad) VALUES ('Borja', 22)"

cur.execute(borrar)
cur.execute(create)
cur.execute(insert)

print(f"{cur.rowcount} alumnos insertados")
conn.close()
