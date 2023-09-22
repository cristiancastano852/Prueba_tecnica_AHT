# PruebatecnicaAHT

Prueba técnica para el cargo de **Desarrollador Python**.

## Problema:

- Use flask para servir una plantilla HTML.

- La plantilla HTML debe tener un formulario con 2 campos de entrada enteros numéricos, un botón y mostrar el resultado de la operación.

- La ruta del controlador de Flask que sirve la plantilla debe aceptar un método GET para entregar la plantilla y un método POST para recibir y operar con los datos del formulario.

- Con los 2 números ingresados por el usuario se debe calcular la suma de todos los números pares entre el número de inicio y fin.

- Mostrar el resultado en la plantilla HTML.

## Solución:

- Se creo el archivo **index.html**, donde se diseña la interfaz web.

- El archivo app.py, define las rutas del proyecto y el método que recibe las peticiones POST y GET. Allí es implementada toda la lógica para calcular la suma de los números pares dentro del rango.

- Se utiliza **Bootstrap** para crear el formulario y los componentes, y el archivo styles.css para mejorar los estilos.

- En la carpeta test se crean los **test** para hacer pruebas a la aplicación.

- Se implemente **CI (continuos integration)** usando **gitHub Actions**. El pipeline en la carpeta de workflows.

## Para ejecutar la aplicación:

- Tener **python** instalado.

- Ejecutar el comando **pip install requeriments.txt** para instalar Flask y Flask-Testing.

- Para compilar la aplicación, se ejecuta **python app.py** y se accede al link mostrado en la consola.

**Autor:** Cristian Castaño
**E-mail:** cristiancastano852@gmail.com
**Empresa:** AHT GLOBAL
