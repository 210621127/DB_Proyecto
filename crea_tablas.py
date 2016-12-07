import sqlite3
import os

try:
    os.remove("db_correos.db")

except FileNotFoundError:
    pass

db = sqlite3.connect("db_correos.db")
c = db.cursor()

c.execute("CREATE TABLE USUARIO(\
    correo TEXT NOT NULL,\
	contra TEXT NOT NULL,\
	apellidoPatU TEXT NOT NULL,\
	apellidoMatU TEXT,\
    nombresU TEXT NOT NULL,\
    contraApp TEXT,\
	PRIMARY KEY(correo)\
)")

c.execute("CREATE TABLE CONTACTO(\
	contacto_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
	email TEXT NOT NULL,\
	registra TEXT NOT NULL,\
	apellidoPatC TEXT NOT NULL,\
	apellidoMatC TEXT,\
	nombresC TEXT NOT NULL,\
	FOREIGN KEY(registra) REFERENCES USUARIO ( correo )\
    )")

c.execute("CREATE TABLE CORREO(\
	correo_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
	fecha NUMERIC NOT NULL,\
	hora NUMERIC NOT NULL,\
	de TEXT NOT NULL,\
	para TEXT NOT NULL,\
	texto TEXT,\
	asunto TEXT,\
	adjunto TEXT,\
    eliminado BOOLEAN NOT NULL,\
	FOREIGN KEY(`de`) REFERENCES USUARIO ( correo )\
)")
c.execute("CREATE TABLE CORREO_E(\
	correo_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
	fecha NUMERIC NOT NULL,\
	hora NUMERIC NOT NULL,\
	de TEXT NOT NULL,\
	para TEXT NOT NULL,\
	texto TEXT,\
	asunto TEXT,\
	adjunto TEXT,\
    eliminado BOOLEAN NOT NULL,\
	FOREIGN KEY(`de`) REFERENCES USUARIO ( correo )\
)")

db.close()
