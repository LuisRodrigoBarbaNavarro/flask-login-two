# Práctica 6 I Flask Con Iniciar Sesión (Parte 2) 🐈

---

### Información Básica ✨

**Nombre:** Barba Navarro Luis Rodrigo

**Fecha (Creación):** 11/11/23

**Descripción:** En este repositorio, se almacena la segunda parte de la práctica cinco, donde se pretende establecer una conexión con una base de datos para almacenar los usuarios y validar las credenciales respaldadas en la misma base de datos.

---

### Recursos ✨

!["Primer Ejemplo"](https://i.imgur.com/xmokexV.png)
!["Segundo Ejemplo"](https://i.imgur.com/Wrs70JQ.png)
!["Tercer Ejemplo"](https://i.imgur.com/pP59U8U.png)
!["Cuarto Ejemplo"](https://i.imgur.com/FwmJiwA.png)

---

### Implementación ✨

Con base en la experiencia previa, se puede afirmar que el modelo básico de plantillas utilizado es el mismo. Sin embargo, se realizaron modificaciones en los archivos base, así como implementaciones nuevas que posibilitaron la conectividad con la base de datos, la generación del modelo de base de datos y la verificación de la validez de la información proporcionada.

En el apartado del archivo 'app.py', realicé una modificación para que pueda enviar un mensaje flash en caso de ingresar credenciales erróneas. Además, en la sección de inicio de sesión, utilizando la sintaxis de Jinja, logré que detectara si había mensajes de error y, mediante un bucle for, desplegara todos los mensajes en caso de que fueran más de uno.

En cuanto a la base de datos, creé el esquema especificado y dos Stored Procedures, uno para añadir un usuario y otro para verificarlo. En el caso del Stored Procedure para crear el usuario, lo modifiqué para que verificara la existencia de un usuario con el mismo nombre y generara un mensaje de error en caso afirmativo. También incluí una excepción para cuando se ingresan campos nulos. Asimismo, para el buen funcionamiento de la aplicación, creé tres usuarios: un usuario administrador y dos usuarios normales. El código adicional que implementé para verificar las condiciones de duplicidad y nulidad es el siguiente:

Además, para la creación de usuarios, utilicé los siguientes comandos, y también tengo la intención de mostrar las excepciones capturadas en la aplicación de MySQL Workbench sobre la no duplicidad del usuario y los campos nulos:

En cuanto al modelo de base de datos, considero que es una forma sólida y amigable de especificar un esquema de base de datos. Es muy versátil, especialmente la obtención del objeto de usuario que nos permite realizar muchas operaciones dentro de la aplicación.

En relación con la conexión a la base de datos, inicialmente tuve inconvenientes con la versión de MySQL. Opté por utilizar una versión más baja para garantizar la compatibilidad con Python, presumiblemente debido a un problema de incompatibilidad con Python.

De igual forma, en el apartado del archivo 'app.py', hice que, dependiendo del tipo de usuario, redirija a una vista diferente. Por lo tanto, creé otro documento HTML heredado de 'base/public/base.html' que me permitiera especificar qué tipo de usuario es. Más adelante, con la escalabilidad de aplicaciones, es posible que tenga otras características que permitan que, según el tipo de usuario, las operaciones autorizadas sean distintas.
