
#ESTETICA DEL COLOR
COLOR_ROJO = '\033[91m'
COLOR_VERDE = '\033[92m'
COLOR_AZUL_BRILLANTE = '\033[94m'
COLOR_AZUL_NEGRITA = '\033[94;1m'
FIN_COLOR = '\033[0m'
#BIBLIOTECAS
import sys
import platform
import getpass
from pathlib import Path
from datetime import date, time, datetime
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow,QVBoxLayout, QPushButton,QDialog ,QComboBox, QWidget, QLabel, QGridLayout, QLineEdit, QSizePolicy, QFormLayout, QMessageBox, QListWidget, QInputDialog

#ruta de txt con mensajes
RMSG = Path(r"D:\POO\BDMSG.txt")
#ruta de txt con asesorias
RASE = Path(r"D:\POO\BDASE.txt")
#ruta de txt con alumnos
RALUM = Path(r"D:\POO\BDALUM.txt")
#ruta de txt con profesores
RPROF = Path(r"D:\POO\BDPROF.txt")


class VentanaLogin(QMainWindow):

    def __init__(self):
        super().__init__()
        self.iniciarventana()
        self.setCentralWidget(self.iniciarventana())
        self.show()


    def iniciarventana(self):

        self.setGeometry(100,200,280,280)
        self.setWindowTitle("Gestor de Asesorías")

        #!!!!!!!!!!!!!!!!LOS ICONOS LOS PONGO COMENTADOS PARA NO ESTAR CAMBIANDO LA RUTA A CADA RATO!!!!!!!!!!!!!!!!!!
        #icon_path= "C:/Users/gabos/Pictures/Roblox/RobloxScreenShot20240502_190525658.png"
        #self.setWindowIcon(QIcon(str(icon_path)))

        central_widget = QWidget(self)
        form_layout = QFormLayout(central_widget)
    
        self.id_label = QLabel("ID del usuario: ")
        self.password_label = QLabel("Contrasenha: ")
        self.boton_iniciar_sesion = QPushButton("Iniciar sesion")
        self.boton_salir = QPushButton("Salir")
        self.id_label_edit = QLineEdit()
        self.password_label_edit = QLineEdit()
        self.password_label_edit.setEchoMode(QLineEdit.EchoMode.Password)

        form_layout.addRow(self.id_label, self.id_label_edit)
        form_layout.addRow(self.password_label, self.password_label_edit)
        form_layout.addRow(self.boton_iniciar_sesion)
        form_layout.addRow(self.boton_salir)

        self.boton_iniciar_sesion.clicked.connect(self.login_clicked)
        self.boton_salir.clicked.connect(self.close)

        return central_widget

    def login_clicked(self):
        id = self.id_label_edit.text()
        password = self.password_label_edit.text()
        
        if(len(id)==8  and id[0:6].isdigit() and id[-1] in {"E","P","A"}):
                if(id[-1] == 'E'): 
                    usu = usuarios(id, password, RALUM)            
                elif(id[-1] == 'P'):
                    usu = usuarios(id, password, RPROF)

        else:
            QMessageBox.critical(
                self,"Error", f"El id {id} no cumple con el formato"
            )
            self.refresh()
        usu.guardartxt()
        band = False
        for x in usu.txt:
            if id == x["ID"] and password == x["Contrasena"]:
                band=True
                if(len(id)==8  and id[0:6].isdigit() and id[-1] in {"E","P","A"}):
                    if(id[-1] == 'E'): 
                        usuario = estudiante(x['ID'],x['Nombre'],x['Carrera'],x['Semestre'],x['Contrasena'] )
                
                    elif(id[-1] == 'P'):
                        usuario = profesor(x['ID'],x['Nombre'],x['Contrasena'])        

        if (band):
            QMessageBox.information(

                self,"Bienvenido", f"Bienvenido al sistema: {usuario.nom}"

            )
            self.close()
            usuario.Menu()
            
        else:
            QMessageBox.critical(
                self,"Error", f"El id {id} o el password no coinciden"
            )
            self.refresh()



    def refresh(self):
        self.id_label_edit.clear()
        self.password_label_edit.clear()




class VentanaAlumno(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def iniciarventana(self):

        self.setGeometry(100,200,280,280)
        self.setWindowTitle("Gestor de Asesorías")

        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.boton_ver_asesorias = QPushButton("Ver asesorías disponibles")
        self.boton_solicitar_asesoria = QPushButton("Solicitar ingreso a asesoría")
        self.boton_ver_inscritas = QPushButton("Ver asesorías inscritas")
        self.boton_contactar_profes= QPushButton("Contactar a profesores")
        self.boton_cerrar_sesion = QPushButton("Cerrar sesión")
        
        form_layout.addWidget(self.boton_ver_asesorias, 0, 0)
        form_layout.addWidget(self.boton_solicitar_asesoria, 1, 0)
        form_layout.addWidget(self.boton_ver_inscritas, 2, 0)
        form_layout.addWidget(self.boton_contactar_profes, 3, 0)
        form_layout.addWidget(self.boton_cerrar_sesion, 4, 0)
        
        self.boton_ver_asesorias.clicked.connect(self.ver_asesorias)
        self.boton_solicitar_asesoria.clicked.connect(self.solicitar_asesoria)
        self.boton_ver_inscritas.clicked.connect(self.ver_inscritas)
        self.boton_contactar_profes.clicked.connect(self.contactar_profes)
        self.boton_cerrar_sesion.clicked.connect(self.cerrarSesion)

        return central_widget

    def ver_asesorias(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")

    def solicitar_asesoria(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")
        
    def ver_inscritas(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")
        
    def contactar_profes(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")

    def cerrarSesion(self):

        self.close()
        self.ventana_login = VentanaLogin()
        self.ventana_login.show()

        
    



class VentanaProfesor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(self.iniciarventana())
        self.show()


    def iniciarventana(self):

        self.setGeometry(100,200,280,280)
        self.setWindowTitle("Gestor de Asesorías")

        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.boton_agregar_asesoria = QPushButton("Agregar asesoría")
        self.boton_eliminar_asesoria = QPushButton("Eliminar asesoría")
        self.boton_ver_pendientes = QPushButton("Ver asesorías pendientes")
        self.boton_admin_alumnos = QPushButton("Administrar alumnos")
        self.boton_contactar_alumnos = QPushButton("Contactar a alumnos")
        self.boton_cerrar_sesion = QPushButton("Cerrar sesión")
        
        form_layout.addWidget(self.boton_agregar_asesoria, 0, 0)
        form_layout.addWidget(self.boton_eliminar_asesoria, 1, 0)
        form_layout.addWidget(self.boton_ver_pendientes, 2, 0)
        form_layout.addWidget(self.boton_admin_alumnos, 3, 0)
        form_layout.addWidget(self.boton_contactar_alumnos, 4, 0)
        form_layout.addWidget(self.boton_cerrar_sesion, 5, 0)
        
        self.boton_agregar_asesoria.clicked.connect(self.agregar_asesoria)
        self.boton_eliminar_asesoria.clicked.connect(self.eliminar_asesoria)
        self.boton_ver_pendientes.clicked.connect(self.ver_pendientes)
        self.boton_admin_alumnos.clicked.connect(self.admin_alumnos)
        self.boton_contactar_alumnos.clicked.connect(self.contactar_alumnos)
        self.boton_cerrar_sesion.clicked.connect(self.cerrarSesion)

        return central_widget
    
    def agregar_asesoria(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")
        
    def eliminar_asesoria(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")
        
    def ver_pendientes(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")
        
    def admin_alumnos(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")
        
    def contactar_alumnos(self):
        QMessageBox.information(self, "Info", "Funcionalidad no implementada")

    def cerrarSesion(self):
        
        self.close()
        self.ventana_login = VentanaLogin()
        self.ventana_login.show()    


class usuarios:
    def __init__(self, id: str, contra: str, dir: str)-> None:
        self.id = id
        self.__contra = contra
        self.__dir = dir
        self.__registros = []

    def guardartxt(self):
        self.txt = []
        ruta_archivo = self.__dir
        if ruta_archivo.exists():
                with ruta_archivo.open('r',encoding='utf-8') as archivo:
                    self.encabezados = archivo.readline().strip().split('|')
                    for linea in archivo:
                        # Dividir cada línea por el delimitador '|' para obtener los campos individuales
                        campos = linea.strip().split('|')
                        
                        # Crear un diccionario vacío para el registro actual
                        registro = {}
                        # Llenar el diccionario con los pares clave-valor correspondientes
                        for i in range(len(self.encabezados)):
                            registro[self.encabezados[i]] = campos[i]

                        self.txt.append(registro)
        else:
            print(COLOR_ROJO + "No se encontro el archivo" + FIN_COLOR)

                
    #def verAsesorias(self)->bool:
        ruta_archivo = RASE
       # Verificar si el archivo existe
        if ruta_archivo.exists():
           with open(ruta_archivo, encoding="utf-8") as f:
            contents = f.read()
            print(contents)
            return(False)
        else:
            print(COLOR_ROJO + "No se encontro el archivo" + FIN_COLOR)
                     
class VentanaEmergenteAsesorias(QMainWindow):
    def __init__(self):
        super().__init__()

        
    def iniciarventana(self):

        self.setGeometry(100,200,280,280)
        self.setWindowTitle("Gestor de Asesorías")

        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        
        return central_widget
    

class estudiante():
    def __init__(self,ID: str, Nombre: str, Carrera: str, Semestre: str, Contrasena: str) -> None:
        self.id = ID
        self.nom = Nombre
        self.Carr = Carrera
        self.Sem = Semestre
        self.__contra = Contrasena

    def Menu(self):
        self.ventana_alumno = VentanaAlumno()

        return self.ventana_alumno.iniciarventana()
    
        
        

    def solicitarAsesoria(self)->bool:
        self.guardartxt()
        band = True
        IdAS = input("Id de asesoria::: ")
        IdAS = IdAS.upper()
        for x in self.txt:
            if(x['ID'] == IdAS):
                if(int(x['Cupo']) > 0):
                    x['Cupo'] = int(x['Cupo'])-1
                    band = False
                else:
                    print(COLOR_ROJO + "Sin cupo"+ FIN_COLOR)
        if(band):
            print(COLOR_ROJO + "No se encontro la asesoria"+ FIN_COLOR)
        else:
            ruta_archivo = RASE
            with ruta_archivo.open('w',encoding='utf-8') as archivo:
                # Escribir los encabezados
                archivo.write(f"{self.encabezados[0]}|{self.encabezados[1]}|{self.encabezados[2]}|{self.encabezados[3]}|{self.encabezados[4]}|{self.encabezados[5]}|{self.encabezados[6]}\n")
                
                # Escribir los datos, cada uno en una nueva línea
                for registro in self.txt:  
                    archivo.write(f"{registro['ID']}|{registro['Materia']}|{registro['Hora de inicio']}|{registro['Hora de Fin']}|{registro['Id Profesor']}|{registro['Fecha']}|{registro['Cupo']}\n")

    def menuAlumno(self)->None:
        band = True
        while(band):
            print(f"MENU ALUMNOS\n1. Ver asesorias disponibles\n2. Solicitar ingreso a asesoria\n3. Ver asesorias inscritas\n4. Contactar a profesores\n5. Regresar a inicio de sesion\n")
            opc = int(input("Ingrese opcion deseada: "))

            if opc == 1:
                band = self.verAsesorias()
            elif opc == 2:
                band = self.solicitarAsesoria()
            elif opc == 3:
                verAsesoriasInscritas()
            elif opc == 4:
                ##LA PODEMOS ELIMINAR SI NO HAY TIEMPO
                #contactarProfesores()
                print("placeholder")

            elif opc == 5:
                print("Cerrando menu de alumno, gracias")
                break
            else:
                print(COLOR_ROJO+"OPCION INVALIDA"+FIN_COLOR)
                print("")

    
class profesor(usuarios):
    def __init__(self,idp: str, nombre: str, contra: str) -> None:
        self.__id = idp
        self.nom = nombre
        self.contra = contra
    
    def Menu(self):
        self.ventana_profesor = VentanaProfesor()
        self.ventana_profesor.iniciarventana()

    def __agregarAsesorias(self)->bool:
        self.guardartxt()
        ruta_archivo = RASE
        idn = input("ID::: ")
        materian= input("Materia::: ")
        HIn = input("Hora de inicio::: ")
        HFn = input("Hora de Fin::: ")
        Dia = input("Dia::: ")
        cupo = input("Cupo::: ")
        with ruta_archivo.open('w',encoding='utf-8') as archivo:
            # Escribir los encabezados
            archivo.write(f"{self.encabezados[0]}|{self.encabezados[1]}|{self.encabezados[2]}|{self.encabezados[3]}|{self.encabezados[4]}|{self.encabezados[5]}|{self.encabezados[6]}\n")
            
            # Escribir los datos, cada uno en una nueva línea
            for registro in self.txt:  
                archivo.write(f"{registro['ID']}|{registro['Materia']}|{registro['Hora de inicio']}|{registro['Hora de Fin']}|{registro['Id Profesor']}|{registro['Fecha']}|{registro['Cupo']}\n")
            archivo.write(f"{idn}|{materian}|{HIn}|{HFn}|{self.__id}|{Dia}|{cupo}\n")
        return(True)
    
    def __eliminarAsesorias(self)->bool:
        self.guardartxt()
        ruta_archivo = RASE
        idn = input("ID::: ")
        with ruta_archivo.open('w',encoding='utf-8') as archivo:
            # Escribir los encabezados
            archivo.write(f"{self.encabezados[0]}|{self.encabezados[1]}|{self.encabezados[2]}|{self.encabezados[3]}|{self.encabezados[4]}|{self.encabezados[5]}|{self.encabezados[6]}\n")
            
            # Escribir los datos, cada uno en una nueva línea
            for registro in self.txt:  
                if(idn != registro['ID']):
                    archivo.write(f"{registro['ID']}|{registro['Materia']}|{registro['Hora de inicio']}|{registro['Hora de Fin']}|{registro['Id Profesor']}|{registro['Fecha']}|{registro['Cupo']}\n")

        return(True)
    
    def __verAsePen(self)->bool:
        self.guardartxt()
        self.c = datetime.now()
        print(f"{self.encabezados[0]}|{self.encabezados[1]}|{self.encabezados[2]}|{self.encabezados[3]}|{self.encabezados[4]}|{self.encabezados[5]}|{self.encabezados[6]}\n")
        for registro in self.txt:
            if(datetime.strptime(registro['Fecha'],'%d/%m/%Y') >= self.c):
                print((f"{registro['ID']}|{registro['Materia']}|{registro['Hora de inicio']}|{registro['Hora de Fin']}|{registro['Id Profesor']}|{registro['Fecha']}|{registro['Cupo']}\n"))
        return(True)
    
    # Funcion para desplegar menu de profesor (anidar cada funcion del menu de profesor a esta funcion) (PRIMER SPRINT)
    def menuProfesor(self)->None:
        band = True
        while(band):
            print(f"MENU PROFESORES\n1. Agregar asesoria para alumno\n2. Eliminar asesoria existente\n3. Ver asesorias pendientes(a futuro)\n4. Administrar alumnos en asesorias\n5. Contactar a alumnos\n6. Regresar a inicio de sesion\n")
            opc = int(input("Opcion::: "))
            if opc == 1:
                band = self.__agregarAsesorias()

            elif opc == 2:
                band = self.__eliminarAsesorias()

            elif opc == 3:
                band = self.__verAsePen()

            elif opc == 4:
                administrarAlumnos()

            elif opc == 5:
                #LA PODEMOS ELIMINAR SI NO HAY TIEMPO
                #contactarAlumnos()
                print("placeholder")

            elif opc == 6:
                print("Cerrando menu de profesor, gracias")
                break
            else:
                print(COLOR_ROJO+"OPCION INVALIDA"+FIN_COLOR)
            

# Funcion para agendar asesorias disponibles
def solicitarAsesoria():

    return

# Funcion para ver asesorias a las que se esta inscrit@
def verAsesoriasInscritas():

    return

# Funcion para comunicarse con profesores de asesorias a las que se esta inscrit@

#LA PODEMOS ELIMINAR SI NO HAY TIEMPO, NO ESTA ADAPTADA AL TXT NI A OBJETOOOOOS!!!!!!!!!!!!!!!!!!!!!!!!!!
def contactarProfesores(lista_prof : dict):
    #for que pasa por el diccionario de profesores y muestra su id y nombres
    for n,Profesor in enumerate(lista_prof):
        print(n+1, " :")
        print("ID del profesor: " ,Profesor)
        print(lista_prof[Profesor]["nombre"])
    #while para que se repita si es que no seleccionan una de las opciones
    while True:
        seleccion = int((input("Seleccione el profesor con el que desea hablar: ")))
        if seleccion > len(lista_prof) or seleccion < 1:
            print("Seleccione una de las opciones por favor")
        else:
            mensaje = str(input("Deposite el mensaje que quiere dar al profesor: "))
            print("El mensaje ha sido enviado.")
            break
    return



#FUNCIONES MENU PROFESORES (que tienen que ser insertadas a menuProfesor)--------------------------------------------------------------------



# Funcion para aceptar/rechazar o eliminar alumnos de asesorias
def administrarAlumnos():

    return

# Funcion para comunicarse con alumnos de asesorias creadas LA PODEMOS ELIMINAR SI NO HAY TIEMPO
#def contactarAlumnos():

    return


#Codigo principal----------------------------------------------------------------------------------------------------------------------



def main():
# Funciones (todo se hara con funciones) (no tengo acentos en el teclado)
    print("INICIO DE SESION, ASESORIAS")
    band= True
    band1=True
    while(band):
        id= input("ID::: ")
        id = id.upper()
        if(len(id)==8  and id[0:6].isdigit() and id[-1] in {"E","P","A"}):
            if(id[-1] == 'E'):
                while(band1):
                    contra = getpass.getpass("Contrasena::: ")
                    usuario = estudiante(id, contra, RALUM)
                    if(usuario.comprob()):
                        band1= False
                        band=False
                        print(COLOR_VERDE+"Acceso completo" + FIN_COLOR)
                    else:
                        print(COLOR_ROJO+ "Accesso denegado" + FIN_COLOR)
                usuario.menuAlumno()
            elif(id[-1] == 'P'):
                while(band1):
                    contra = getpass.getpass("Contrasena::: ")
                    usuario = profesor(id, contra, RPROF)
                    if(usuario.comprob()):
                        band1= False
                        band=False
                        print(COLOR_VERDE+"Acceso completo" + FIN_COLOR)
                    else:
                        print(COLOR_ROJO+ "Accesso denegado" + FIN_COLOR)
                usuario.menuProfesor()


    




# Codigo principal

# Aca llamen las funciones para probarlas/testearlas
app = QApplication(sys.argv)

Window = VentanaLogin()


sys.exit(app.exec())