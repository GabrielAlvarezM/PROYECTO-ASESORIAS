# PROYECTO-ASESORIAS
Todo lo que se utilizo en el proyecto de asesorías
Gestor de Asesorías - README

Este archivo proporciona una descripción general del código fuente del Gestor de Asesorías, una aplicación de escritorio escrita en Python.

Requisitos previos

Python 3.0 o superior
PyQt6 (biblioteca de interfaz gráfica de usuario)
Paquetes adicionales según se necesite (ver código para detalles)
Estructura del código

El código está organizado en los siguientes archivos:

principal.py (principal.py en el código original): Contiene el punto de entrada principal de la aplicación y crea una instancia de la ventana de inicio de sesión (VentanaLogin).
ventanas.py: Define las clases para las diferentes ventanas de la aplicación:
VentanaLogin: Maneja el inicio de sesión del usuario, verificando la identificación y contraseña.
VentanaAlumno: Proporciona un menú para las acciones disponibles para los estudiantes.
VentanaProfesor: Proporciona un menú para las acciones disponibles para los profesores.
VentanaEmergenteAsesorias (clase sin uso en el código proporcionado): Posiblemente pensada para mostrar información emergente sobre las asesorías.
usuarios.py: Define la clase base usuarios para usuarios del sistema (estudiantes y profesores), que maneja la identificación, contraseña y el archivo de texto asociado.
estudiante.py: Define la clase estudiante que hereda de usuarios y agrega funcionalidades específicas para los estudiantes, como solicitar asesorías, ver sus inscripciones y acceder a su menú.
profesor.py: Define la clase profesor que hereda de usuarios y agrega funcionalidades específicas para los profesores, como agregar, eliminar y ver asesorías pendientes, y posiblemente administrar alumnos en asesorías (función no implementada actualmente).
Funcionalidades implementadas actualmente

Inicio de sesión con verificación de identificación y contraseña.
Menús para estudiantes y profesores.
Funcionalidad básica de las ventanas (principalmente mostrar mensajes informativos).
Funcionalidades no implementadas

La mayor parte de la lógica de la aplicación aún no está implementada, como se indica en los mensajes de las ventanas (QMessageBox.information). Esto incluye:
Solicitar asesorías.
Ver asesorías inscritas.
Contactar a profesores.
Agregar, eliminar y ver asesorías pendientes (para profesores).
Administración de alumnos en asesorías (para profesores).
Consideraciones

Las rutas de los archivos de texto que almacenan la información de usuarios, mensajes y asesorías están codificadas en el código y es posible que deba modificarlas según la ubicación real de los archivos en su sistema.
Se utilizan códigos de escape para el color en la terminal (COLOR_ROJO, FIN_COLOR), pero es probable que no tengan efecto en la interfaz gráfica de usuario.
La clase VentanaEmergenteAsesorias aparece en el código pero no se usa actualmente.
Próximos pasos

El código actual sirve como base para desarrollar la funcionalidad completa del Gestor de Asesorías. Los pasos siguientes podrían incluir:

Implementar las funcionalidades faltantes según las definiciones de las clases y los mensajes informativos existentes.
Conectar la aplicación con una base de datos real para almacenar la información de usuarios y asesorías de forma persistente.
Mejorar la interfaz gráfica de usuario para proporcionar una experiencia más visual y fácil de usar.
Agregar documentación adicional para explicar el código con más detalle y facilitar su mantenimiento.
