"""
Nombre: Rodriguez Bocanegra, Juan Daniel
Materia: Seminario de Solucion de Problemas de Bases de datos
Profesor: Michel Davalos Boites

# Actividad 08 (UPDATE)
Implementar las modificaciones en el software. Subir reporte con capturas de
pantalla de la ejecución del programa, el .sql y el .py (o repositorio).

"""
import sqlite3
import os
import time
import getpass

class Usuario():
    def __init__(self, data):
        self.correo = data
        self.contra = data
        self.apellidoPatU = data
        self.apellidoMatU = data
        self.nombresU = data
    def __str__ (self):
        return "\n\tEmail:      "+str(self.correo)\
              +"\n\tContraseña: "\
              +"\n\tNombre:     "+str(self.apellidoPatU)+" "+str(self.apellidoMatU)+","\
            +str(self.nombresU)

class Contacto():
    def __init__(self,data):
        self.contacto_id = data
        self.email = data
        self.registra = data
        self.apellidoPatC = data
        self.apellidoMatC = data
        self.nombresC = data
    def __str__(self):
        if self.apellidoMatC != None:
            return "\tID: "+str(self.contacto_id)+\
              "\n\tEmail: "+str(self.email)+\
              "\n\tNombre: "+str(self.apellidoPatC)+" "+str(self.apellidoMatC)+","\
                +str(self.nombresC)
        else:
            return "\tID: "+str(self.contacto_id)+\
              "\n\tEmail: "+str(self.email)+\
              "\n\tNombre: "+str(self.apellidoPatC)+","+str(self.nombresC)

class Correo():
    def __init__(self, data):
        self.correo_id = data
        self.fecha = data
        self.hora = data
        self.de = data
        self.para = data
        self.texto = data
        self.asunto = data
        self.adjunto = data
        self.eliminado = data

    def __str__(self):
        return "\tID:     "+str(self.correo_id)\
            +"\n\tFecha:  "+str(self.fecha)\
            +"\n\tHora:   "+str(self.hora)\
            +"\n\tPara:   "+str(self.para)\
            +"\n\tAsunto: "+str(self.asunto)\
            +"\n\tTexto:\n\t------------------------------\n\t"+str(self.texto)\
            +"\n\t------------------------------"\
            +"\n\tAdjunto: "+str(self.adjunto)

class MenuContatos():
    def __init__(self):
        pass

    def agregar(self, user, db):
        u = user
        cursor = db.cursor()
        c = Contacto(None)
        print("\n\t* * * Agregar contacto * * *\n")
        print("\n\tPresione solo <ENTER> para regresar...")

        c.email = input("\n\tIngrese el correo del contacto: ")
        while len(c.email) < 1:
            return
        while len(c.email) < 2: #<----- modificar para que reconozca minimo 8 caracteres
            print("\n\t(!) Ingrese un correo valido!")
            c.email = input ("\n\tCorreo: ")

        c.registra = u.correo
        c.apellidoPatC = input("\n\tApellido paterno: ")
        while len(c.apellidoPatC) < 1 :
            c.apellidoPatC = input("\t(!) Ingrese un apellido valido: ")
        c.apellidoMatC = input("\n\tApellido materno: ")
        if len(c.apellidoMatC) == 0:
            c.apellidoMatC = None

        c.nombresC = input("\n\tNombres(s): ")
        while len(c.nombresC) < 1:
            c.nombresC = input("\t(!) Ingrese un nombre valido: ")

        cursor.execute("INSERT INTO CONTACTO(contacto_id,email,registra,\
        apellidoPatC,apellidoMatC,nombresC) VALUES (?,?,?,?,?,?)", \
        (c.contacto_id,c.email,c.registra,c.apellidoPatC,c.apellidoMatC,c.nombresC))

        db.commit()
        input("\n\tContacto registrado satisfactoriamente...")

    def mostrarContactos(self,user,db):
        flag = False
        u = user
        c = Contacto(None)
        cursor = db.cursor()

        os.system("clear")
        rows = cursor.execute('SELECT * FROM CONTACTO WHERE registra = ?',(u.correo,))

        print("\n\tContactos registrados\
        \n\n=================================================")

        for row in rows:
            if row[0] != None:
                flag = True
            c.contacto_id = row[0]
            c.email = row[1]
            c.registra = row[2]
            c.apellidoPatC = row[3]
            c.apellidoMatC = row[4]
            c.nombresC = row[5]
            print(c)
            print("-------------------------------------------------")

        if flag == False:
            print("\t(!) No existen contactos registrados!!")

        print("=================================================")
        input("\n\tPresione una tecla paracontinuar...")

    def submenu(self,u,c):
        self.list = []
        i = 0
        print("\n\t1) Buscar\n\t2) Indice\n\t0) Salir")
        while True:
            opc = input("\n\tSeleccione una opcion: ")
            if opc.isdigit():
                opc = int(opc)
                if opc == 1 or opc == 2 or opc == 0:
                    break
            else:
                print("\n\t(!) Ingrese solo digitos!!")

        if opc == 1:
            tmp = input("\n\tIngrese un email para buscar: ")
            if len(tmp) == 0:
                return None
            else:
                c.execute("SELECT * FROM CONTACTO WHERE email = ? AND \
                registra = ?",(tmp,u.correo,))
                row = c.fetchone()
                if row != None:
                    return row
                else:
                    return None
        elif opc == 2:
            print("\n\tIndice")
            rows = c.execute("SELECT * FROM CONTACTO WHERE registra = ?",\
            (u.correo))
            for row in rows:
                i += 1
                self.list.append(row[1])
                print("\t",i,") "+self.list[i-1])
            while True:
                selec = input("\n\tSeleccione un contacto: ")
                if selec.isdigit():
                    selec = int(selec)
                    if selec < 1 or selec > i:
                        print("\n\t(!) Seleccione un numero de la lista!")
                    else:
                        break
                else:
                    print("\n\t(!) Ingrese unicamente numeros!")
            tmp = self.list[selec-1]
            c.execute("SELECT * FROM CONTACTO WHERE email = ?",(tmp,))
            row = c.fetchone()
            if row != None:
                return row
            else:
                return None
        elif opc == 0:
            return 0
        else:
            print("\n\t(!) Ingrese alguna de las opciones del menu!!")


    def eliminar(self,u,c):

        while True:
            con = Contacto(None)
            os.system("clear")

            print("\n\t* * * ELIMINA CONTACTO * * *")
            row = self.submenu(u,c)
            if row == None:
                print("\n\t(!) No se encontro el contacto")
                input("\n\tPresione una tecla para continuar...")
                break
            elif row == 0:
                return
            else:
                con.contacto_id = row[0]
                con.email = row[1]
                con.apellidoPatC = row[3]
                con.apellidoMatC = row[4]
                con.nombresC = row[5]
                print("\n\t")
                print(con)
                print("\n\tConfirmacion para borrar\n\n\t1) SI\n\t2) NO")
                while True:
                    opc = input("\n\tSeleccione una opcion: ")
                    if opc.isdigit():
                        if opc == '1':
                            c.execute("DELETE FROM CONTACTO WHERE contacto_id =\
                            ?",(con.contacto_id,))
                            print("\n\tEliminacion exitosa!")
                            input("\n\tPresione una tecla para continuar...")
                            break
                        elif opc == '2':
                            os.system("clear")
                            print("\n\tEliminacion abortada!!!")
                            input("\n\tPresione una tecla para continuar...")
                            break
                    else:
                        print("\n\t(!)Ingrese solo numeros!")
                break
    def modificar(self,u,c):

        while True:
            con = Contacto(None)
            os.system("clear")

            print("\n\t* * * MODIFICA CONTACTO * * *")
            row = self.submenu(u,c)
            if row == None:
                print("\n\t(!) No se encontro el contacto")
                input("\n\tPresione una tecla para continuar...")
                break
            elif row == 0:
                return
            else:
                con.contacto_id = row[0]
                con.email = row[1]
                con.apellidoPatC = row[3]
                con.apellidoMatC = row[4]
                con.nombresC = row[5]
                os.system("clear")
                print("\n\tContacto seleccionado\n")
                print("\n\t===========================================\n")
                print(con)
                print("\n\t===========================================\n")
                print("\t1) Apellido paterno\n\t2) Apellido materno")
                print("\t3) Nombres\n\t0) Salir")
                while True:
                    opc = input("\n\tSeleccione una opcion: ")
                    if opc.isdigit():
                        if opc == '1':
                            while True:
                                tmp = input("\n\tIngrese el nuevo apellido: ")
                                if len(tmp) == 0:
                                    print("\n\t(!) El campo no puede estar vacio!")
                                else:
                                    break
                            c.execute("UPDATE CONTACTO set apellidoPatC = ? \
                            WHERE contacto_id = ?",(tmp,con.contacto_id,))
                            print("\n\tContacto actualizado!")
                            input("\n\tPresione una tecla para continuar...")
                            break
                        elif opc == '2':
                            tmp = input("\n\tIngrese el nuevo apellido: ")
                            c.execute("UPDATE CONTACTO set apellidoMatC = ? \
                            WHERE contacto_id = ?",(tmp,con.contacto_id,))
                            print("\n\tContacto actualizado!")
                            input("\n\tPresione una tecla para continuar...")
                            break

                        elif opc == '3':
                            while True:
                                tmp = input("\n\tIngrese el nuevo nombre: ")
                                if len(tmp) == 0:
                                    print("\n\t(!) El campo no puede estar vacio!")
                                else:
                                    break
                            c.execute("UPDATE CONTACTO set nombresC = ? \
                            WHERE contacto_id = ?",(tmp,con.contacto_id,))
                            print("\n\tContacto actualizado!")
                            input("\n\tPresione una tecla para continuar...")
                            break
                        elif opc == '0':
                            return
                    else:
                        print("\n\t(!)Ingrese solo numeros!")
                break

    def menu(self,user,db):
        cursor = db.cursor()
        opc = -1
        while True:
            db.commit()
            os.system("clear")
            print("\n\t* * * CONTACTOS * * * \n")
            print("\n\t1) Mostrar contactos ") # Muestra contactos - con id-
            print("\t2) Agregar nuevo contacto") #Agrega un nuevo contacto -correo-
            print("\t3) Eliminar contacto") # Elimina de la base de datos (submenu)
            print("\t4) Modificar contacto") # Modifica un contacto (submenu)
            print("\t0) Salir")
            opc = input ("\n\tIngrese una opcion: ")
            if opc.isdigit() == True:
                opc = int(opc)
                if opc == 1:
                    self.mostrarContactos(user,db)
                elif opc == 2:
                    os.system("clear")
                    self.agregar(user,db)
                elif opc == 3:
                    self.eliminar(user,cursor)
                elif opc == 4:
                    self.modificar(user,cursor)
                elif opc == 0:
                    break
            else:
                print("\n\t(!) Seleccione una de las opciones del menu...")
                input("\n\tPresione una tecla para continuar...")

class MenuCorreoNuevo():
    def __init (self):
        pass
    def menu(self,user,db,mContactos):
        menuC = mContactos
        u = user
        cursor = db.cursor()
        c = Correo(None)

        while True:
            os.system("clear")
            print("\n\t* * * CORREO NUEVO * * *\n")

            print("\n\tPresione solo < ENTER > par regresar....\n")
            c.fecha = time.strftime("%d/%m/%Y")
            c.hora = time.strftime("%X")
            print("\tFecha: ", c.fecha)
            print("\tHora:  ",c.hora)

            c.de = u.correo
            print("\tDe:    ",c.de)

            c.para = input("\tPara:  ")
            if len(c.para) == 0:
                return
            while len(c.para) < 6:
                c.para = input("\tIngrese un correo valido: ")
            cursor.execute("SELECT * FROM CONTACTO WHERE email = ? AND \
                registra = ?", (c.para, u.correo))
            if cursor.fetchone() != None:
                break
            else:
                print("\n\t(!) El contacto que escribio no esta registrado...")
                input("\tPresione una tecla para continuar...")
                os.system("clear")
                menuC.agregar(user,db)

        linea = ''
        print("\n\tPresione solo < ENTER > para continuar o escriba el texto...")
        c.texto = input("\tTexto:\n\t")

        while True and len(c.texto) > 0:
            linea = input("\t")
            if len(linea) < 1:
                break
            c.texto += '\n\t'+linea
        if len(c.texto ) == 0:
            c.texto = None

        c.asunto = input("\tAsunto: ")
        if len(c.asunto) == 0:
            c.asunto = None

        c.adjunto = input("\tAdjunto: ")
        if len(c.adjunto) == 0:
            c.adjunto = None

        c.eliminado = False
        c.hora = time.strftime("%X")

        cursor.execute("INSERT INTO CORREO (correo_id,fecha,hora,de,para,\
        texto,asunto,adjunto,eliminado) VALUES (?,?,?,?,?,?,?,?,?)",\
        (c.correo_id,c.fecha,c.hora,c.de,c.para,c.texto,c.asunto,\
        c.adjunto,c.eliminado))

        input("\n\tCorreo guardado exitosamente!")
        db.commit()

class MenuCorreoEnviado():
    def __init__(self):
        pass

    def recientes(self,user,cursor):
        i = 0
        flag = False
        os.system("clear")
        rows = cursor.execute("SELECT * FROM CORREO WHERE de = ? AND eliminado\
            = ? ORDER BY correo_id DESC", (user.correo,False) )
        for row in rows:
            if i > 4:
                input("\n\tPresione una tecla para mostrar mas correos...")
                os.system("clear")
                i = 0
            e = Correo(None)
            if row[0] != None:
                flag = True
            e.correo_id = row[0]
            e.fecha = row [1]
            e.hora = row [2]
            e.para = row [4]
            e.texto = row [5]
            e.asunto = row [6]
            e.adjunto = row [7]
            print(e)
            print("=========================================")
            i += 1
        if flag == False:
            print("\n\t(!) No existen correos enviados!!")
        input("\n\tNo hay mas correos, presione una tecla para regresar...")

    def busquedaFecha(self,user,cursor):
        flag = False
        while True:
            os.system("clear")
            print("\n\tPresione solo < ENTER > para regresar...")
            fecha = input("\n\tIngrese la fecha en formato dd/mm/aaaa: ")
            if len(fecha) < 10 and len(fecha) > 1 or len(fecha) > 10:
                print("\n\t(!) Ingrese la fecha en el formato que se muestra!!")
                input("\n\tPresione una tecla para continuar...")
            elif len(fecha) == 0:
                return
            else:
                break
        rows = cursor.execute("SELECT * FROM CORREO WHERE de = ? AND \
            fecha = ? AND eliminado = ?",(user.correo,fecha,False) )
        os.system("clear")
        for row in rows:
            e = Correo(None)
            if row[0] != None:
                flag = True
            e.correo_id = row[0]
            e.fecha = row [1]
            e.hora = row [2]
            e.para = row [4]
            e.texto = row [5]
            e.asunto = row [6]
            e.adjunto = row [7]
            print(e)
            print("=========================================")
        if flag == False:
            print("\n\t(!) No existen correos enviados con la fecha dada!!")
            input("\n\tPresione una tecla para continuar...")
        else:
            self.subMenu(user,cursor)

    def busContacto(self,user,cursor):
        self.list = []
        i = 0
        flag = False
        rows = cursor.execute("SELECT * FROM CONTACTO WHERE registra = ?",\
            (user.correo) )
        print("\n\tContactos registrados: ")
        for row in rows:
            i += 1
            self.list.append(row[1])
            print("\t",i,") "+self.list[i-1])
        while True:
            selec = input("\n\tSeleccione un contacto: ")
            if selec.isdigit():
                selec = int(selec)
                if selec < 1 or selec > i:
                        print("\n\t(!) Seleccione un numero de la lista!")
                else:
                    break
            else:
                print("\n\t(!) Ingrese un numero!")
        tmp = self.list[selec-1]
        rows = cursor.execute("SELECT * FROM CORREO WHERE de = ? AND para = ?\
            AND eliminado = ?",(user.correo,tmp,False))
        os.system("clear")
        for row in rows:
            e = Correo(None)
            if row[0] != None:
                flag = True
            e.correo_id = row[0]
            e.fecha = row [1]
            e.hora = row [2]
            e.para = row [4]
            e.texto = row [5]
            e.asunto = row [6]
            e.adjunto = row [7]
            print(e)
            print("=========================================")

        if flag == False:
            print("\n\t(!) No existen correos registrados!!")
            input("\n\tPresione una tecla para continuar...")
        else:
            self.subMenu(user,cursor)

    def busTexto(self,user,cursor):
        flagT = False
        flagA = False
        flagC = False
        while True:
            print("\n\tIngrese el texto a buscar o presione < ENTER > para regresar...")
            text = input("\n\tTexto: ")
            if len(text) == 0:
                return
            else:
                break
        rows = cursor.execute("SELECT * FROM CORREO WHERE texto LIKE ? AND \
            eliminado = ?",('%'+text+'%',False))
        os.system("clear")
        print("\n\tBusqueda en TEXTO:\n")
        for row in rows:
            e = Correo(None)
            if row[0] != None:
                flagT = True
            e.correo_id = row[0]
            e.fecha = row [1]
            e.hora = row [2]
            e.para = row [4]
            e.texto = row [5]
            e.asunto = row [6]
            e.adjunto = row [7]
            print(e)
            print("=========================================")

        rows = cursor.execute("SELECT * FROM CORREO WHERE para LIKE ? AND \
            eliminado = ?",('%'+text+'%',False))
        print("\n\n\tBusqueda en CC:\n")
        for row in rows:
            e = Correo(None)
            if row[0] != None:
                flagC = True
            e.correo_id = row[0]
            e.fecha = row [1]
            e.hora = row [2]
            e.para = row [4]
            e.texto = row [5]
            e.asunto = row [6]
            e.adjunto = row [7]
            print(e)
            print("=========================================")

        rows = cursor.execute("SELECT * FROM CORREO WHERE asunto LIKE ? AND \
            eliminado = ?",('%'+text+'%',False))
        print("\n\n\tBusqueda en ASUNTO:\n")
        for row in rows:
            e = Correo(None)
            if row[0] != None:
                flagA= True
            e.correo_id = row[0]
            e.fecha = row [1]
            e.hora = row [2]
            e.para = row [4]
            e.texto = row [5]
            e.asunto = row [6]
            e.adjunto = row [7]
            print(e)
            print("=========================================")

        if flagT == False and flagC == False and flagA == False:
            print("\n\t(!) No hay conincidencias!!")
            input("\n\tPresione una tecla para continuar...")
        else:
            self.subMenu(user,cursor)

    def subMenu(self,user,cursor):
        flag = False
        while True:
            print("\n\tPresione < ENTER > para regresar...\n")
            id = input("\n\tIntroduzca el ID del correo para seleccionar uno: ")

            if len(id) == 0:
                return

            elif id.isdigit():
                rows = cursor.execute('SELECT* FROM CORREO WHERE correo_id = ?\
                AND eliminado = ?',(id,False))
                for row in rows:
                    e = Correo(None)
                    if row[0] != None:
                        flag = True
                        os.system("clear")
                    e.correo_id = row[0]
                    e.fecha = row [1]
                    e.hora = row [2]
                    e.para = row [4]
                    e.texto = row [5]
                    e.asunto = row [6]
                    e.adjunto = row [7]
                    print("=========================================")
                if flag == False:
                    print("\n\t(!) EL ID ingresado no existe!!")
                else:
                    break
            else:
                print("\n\t(!) Ingrese solo numeros!!")

        while True:
            os.system("clear")
            print("\n\tCorreo encontrado:")
            print("\n\t=========================================")
            print(e)
            print("\n\t=========================================")
            print("\n\t1) Descargar adjunto\n\t2) Eliminar\n\t3) Reenviar a...")
            opc = input("\n\tSeleccione una opcion o presione < ENTER > para regresar...")
            if opc == '':
                return
            elif opc == '1':
                pass
            elif opc == '2':
                self.eliminar(user,cursor,e)

                break
            elif opc == '3':
                pass
            else:
                print("\n\tIngrese una de las opciones...")
                input("\n\tPresione una tecla para continuar...")

    def recuperar(self,user,cursor):
        while True:
            print("\n\t¿Desea recuperar todos los eliminados? \n\t1) SI\n\t2) NO")
            opc = input("\n\tSeleccione una opcion: ")
            if opc.isdigit():
                opc = int(opc)
                if opc == 1:
                    cursor.execute('UPDATE CORREO set eliminado = ? WHERE \
                        de = ?',(False,user.correo))
                    print("\n\tRecuperacion exitosa!")
                    input("\n\tPresione una tecla para continuar...")
                    break
                elif opc == 2:
                    print("\n\tRecuperacion abortada!!!")
                    input("\n\tPresione una tecla para continuar...")
                    return
                else:
                    input("\n\t(!) Ingrese una de las opciones!")
            else:
                print("\n\t(!) Ingrese solo numeros!!")
    def eliminar(self,user,cursor,e):
        while True:
            print("\n\tSeguro que desea eliminar? \n\t1) SI\n\t2) NO")
            opc = input("\n\tSeleccione una opcion: ")
            if opc.isdigit():
                opc = int(opc)
                if opc == 1:
                    cursor.execute('UPDATE CORREO set eliminado = ? WHERE \
                        correo_id = ?',(True,e.correo_id,))
                    print("\n\tEliminacion exitosa!")
                    input("\n\tPresione una tecla para continuar...")
                    break
                elif opc == 2:
                    print("\n\tEliminacion abortada!!!")
                    input("\n\tPresione una tecla para continuar...")
                    return
                else:
                    input("\n\t(!) Ingrese una de las opciones!")
            else:
                print("\n\t(!) Ingrese solo numeros!!")

    def vaciaPapelera(self,user,cursor):
        lista = []
        c = cursor
        u = user
        while True:
            print("\n\tSeguro que desea vaciar la papelera? \n\t1) SI\n\t2) NO")
            opc = input("\n\tSeleccione una opcion: ")
            if opc.isdigit():
                opc = int(opc)
                if opc == 1:
                    rows = c.execute('SELECT * FROM CORREO WHERE eliminado = ? \
                    AND de = ?',(True,u.correo,))
                    for row in rows:
                        lista.append(row)
                    for row in lista:
                        c.execute("INSERT INTO CORREO_E(correo_id,fecha,hora,\
                        de,para,texto,asunto,adjunto,eliminado) VALUES (?,?,?,\
                        ?,?,?,?,?,?)",(None,row[1],row[2],row[3],row[4],\
                        row[5],row[6],row[7],row[8],))
                        c.execute("DELETE FROM CORREO WHERE correo_id = ?",\
                        (row[0],))

                    print("\n\tEliminacion exitosa!")
                    input("\n\tPresione una tecla para continuar...")
                    break
                elif opc == 2:
                    print("\n\tEliminacion abortada!!!")
                    input("\n\tPresione una tecla para continuar...")
                    return
                else:
                    input("\n\t(!) Ingrese una de las opciones!")
            else:
                print("\n\t(!) Ingrese solo numeros!!")

    def menu(self,user,db):
        cursor = db.cursor()
        e = Correo(None)
        while True:
            db.commit()
            os.system("clear")
            print("\n\t* * * CORREO ENVIADO * * *\n")
            print("\t1) Recientes")      #Mostrar correos enviados de 5 en 5
            print("\t2) Buscar por fecha") #Busca por fecha dada
            print("\t3) Buscar por contacto") #Busca enviados a un cierto contacto
            print("\t4) Buscar por texto") #Buscar por una cadena de texto,CC,asunto del correos
            print("\t5) Recuperar todos los eliminados") #recupera todos los correos marcados como eliminados
            print("\t6) Vaciar papelera") #Marca manda a una tabla especial el correo y lo elimina de la tabla original
            print("\t0) Salir")
            opc = input("\n\tSeleccione una opcion: ")

            if opc.isdigit() == True:
                opc = int(opc)
                if opc == 1:
                    self.recientes(user,cursor)
                elif opc == 2:
                    self.busquedaFecha(user,cursor)
                elif opc == 3:
                    self.busContacto(user,cursor)
                elif opc == 4:
                    self.busTexto(user,cursor)
                elif opc == 5:
                    self.recuperar(user,cursor)
                elif opc == 6:
                    self.vaciaPapelera(user,cursor)
                elif opc == 0:
                    break
                else:
                    print("\n\t(!) Seleccione una de las opciones del menu!!!")
                    input("\n\tPresione una tecla para continuar...")
            else:
                print("\n\t(!) Ingrese digitos!!!")
                input("\n\tPresione una tecla para continuar...")


class MainMenu():

    def __init__(self):
        pass
    def menuGeneral(self,user,db):
        mNuevo = MenuCorreoNuevo()
        mEnviado = MenuCorreoEnviado()
        mContactos = MenuContatos()

        while True:
            os.system("clear")
            print("\n\t* * * MENU  * * *\n\n\t1) Correo enviado\n\t2) Contactos \
                \n\t3) Correo nuevo\n\t0) Salir")
            opc = input("\n\tSeleccione una opcion: ")

            if opc.isdigit() == True:
                opc = int(opc)

                if opc == 1:
                    mEnviado.menu(user,db)
                elif opc == 2:
                    mContactos.menu(user,db)
                elif opc == 3:
                    mNuevo.menu(user,db,mContactos)
                elif opc == 0:
                    db.commit()
                    break
                else:
                    print("\n\t(!) Seleccione una de las opciones del menu!!!")
                    input("\n\tPresione una tecla para continuar...")
            else:
                print("\n\t(!) Ingrese solo digitos!!!")
                input("\n\tPresione una tecla para continuar...")

class Login_Registro():
    db = sqlite3.connect("db_correos.db")
    c = db.cursor()
    #c.execute("PRAGMA foreign_keys = ON")

    mg = MainMenu()

    def __init__(self):
        pass

    def login(u,db):
        while True:
            u = u
            db = db
            c = db.cursor()

            os.system("clear")
            print("\n\t* * * LOGIN * * *\n\t(Presione <ENTER> para regresar)")
            email = input("\n\tEmail: ")
            if email == '':
                break
            contra = getpass.getpass ("\n\tContraseña: ")

            rows = c.execute ('SELECT * FROM USUARIO WHERE correo = ? AND \
                contra = ?',(email, contra))
            for row in rows:
                u.correo = row[0]
                u.contra = row[1]
                u.apellidoPatU = row[2]
                u.apellidoMatU = row[3]
                u.nombresU = row[4]

            if u.correo != None:
                input("\n\tLogin correcto!")
                return True
            else:
                input("\n\t(!) Email o contraseña incorrectos!!")

    def registrarse(user,db):
        c = db.cursor()
        while True:
            os.system("clear")
            print("\n\t* * * Registro * * * \n\t(Presione <ENTER> para regresar)")
            user.correo = input ("\n\tEmail: ")
            if user.correo == '':
                return
            c.execute ('SELECT * FROM USUARIO WHERE correo = ?',(user.correo,))
            if c.fetchone() != None:
                print("\n\t(!) El correo ingresado ya ha sido registrado!!")
                input("\n\tPresione una tecla para continuar...")
            else:
                break
        while True:
            pass1 = getpass.getpass("\tContrañena: ")
            pass2 = getpass.getpass("\tIngrese de nuevo la contraseña: ")
            if pass1 != pass2 :
                print("\n\t(!) Las contraseñas no coinciden!")
            if len(pass1) < 1:
                print("\n\t(!) Ingrese una contraseña valida")
            else:
                if pass1 == pass2:
                    user.contra = pass1
                    break
        user.apellidoPatU = input("\tApellido paterno: ")
        while user.apellidoPatU.isalnum() == False:
            print("\n\t(!) Apellido invalido!")
            user.apellidoPatU = input ("\tIngrese su apellido paterno de nuevo: ")

        user.apellidoMatU = input("\tApellido Materno: ")

        user.nombresU = input("\tNombre(s): ")
        while len(user.nombresU) < 1:
            print("(!) Nombre invalido!")
            user.nombresU = input("\tIngrese su nombre de nuevo: ")
        c.execute("INSERT INTO USUARIO (correo,contra,apellidoPatU,\
            apellidoMatU,nombresU) VALUES (?,?,?,?,?)",\
            (user.correo, user.contra,user.apellidoPatU,user.apellidoMatU,\
            user.nombresU))
        db.commit()
        print("\n\tRegistro exitoso!")
        input("\n\tPresione una tecla para continuar...")

    while True:
        user = Usuario(None)

        os.system("clear")
        print("\n\t* * * INICIO DE SESION/REGISTRO * * * \n\n\t1) Iniciar sesion \
            \n\t2) Registrarse \n\t0) Salir")
        opc = input("\n\tElige una opcion: ")

        if opc.isdigit() == True:
            opc = int(opc)
            if opc == 1:
                os.system("clear")
                if login(user,db) == True:
                    mg.menuGeneral(user,db)
            elif opc == 2:
                os.system("clear")
                registrarse(user,db)
            elif opc == 0:
                db.close()
                exit()
            else:
                print("\n\t(!) Seleccione una de las opciones del menu!!!")
                input("\n\tPresione una tecla para continuar...")
        else:
            print("\n\t(!) Ingrese solo digitos...")
            input("\n\tPresione una tecla para continuar...")
