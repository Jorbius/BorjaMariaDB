import pymysql

conn = pymysql.connect(host="db", user="root", password="root", database="asDatabase")

cur = conn.cursor()

borrar = f"DROP TABLE IF EXISTS asDatabase.alumnos;"

create = f"CREATE TABLE `alumnos` ( `nombre` varchar(30) NOT NULL, `edad` int(11) NOT NULL); "

insert = f"INSERT INTO `alumnos` (`nombre`, `edad`) VALUES ('Joseba', '21'), ('Borja', '22');"

cur.execute(borrar)
cur.execute(create)
cur.execute(insert)

conn.commit()

print(f"{cur.rowcount} alumnos insertados")
conn.close()
