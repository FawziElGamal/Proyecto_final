# Tienda de repuestos - Readme

_Proyecto realizado durante el mes de junio del año 2023 mientras me encontraba estudiando el curso de "Python" que ofrece la plataforma de cursos online "CoderHouse"._  
_El proyecto que se presenta tiene el propósito de servir como "Proyecto Final" para culminar el curso. Su objetivo principal es permitir a los estudiantes aplicar todos los conceptos enseñados durante el curso, así como aquellos que han aprendido de forma autónoma. De esta manera, se busca certificar que los alumnos han completado satisfactoriamente el curso y tienen un dominio adecuado de la materia._

<br>

# Recorrida por la página

<iframe width="560" height="315" src="https://www.youtube.com/embed/VaPS8akQOsw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

<br>


# Indice

1) [Credenciales](#credenciales)
2) [Página de inicio](#página-de-inicio)
3) [Tienda en línea](#tienda-en-linea)  
    3.1) [Productos individuales](#productos-individuales)  
    3.2) [Registro de usuarios](#registro-de-usuarios)  
    3.3) [Inicio de sesión](#inicio-de-sesión)  
    3.4) [Mi perfil](#mi-perfil)  
    3.5) [Cambio de contraseña](#cambio-de-contraseña)  
    3.6) [Carrito de compras](#carrito-de-compras)  
    3.7) [Pedidos](#pedidos)

4) [Página de administrador](#página-de-administrador)
5) [Final](#final)

---

<br>

# Credenciales
### Credenciales de superusuario:
username: fawzi  
password: casa4321

### Credenciales administrador (staff):
username: admin  
password: casa4321

<br>

### Credenciales de cliente (no superusuario ni acceso a administrador):
**Usuario de prueba 1:**  
    username: prueba  
    password: casa4321  

**Usuario de prueba 2:**  
    username: prueba2  
    password: casa4321  

<br>

# Página de inicio

Se accede a dicha página ingresando a la URL principal.  
La misma se encuentra dividida en 5 secciones las cuales son accesibles mediante la barra de navegación (navbar) o simplemente realizano "scroll":

* **Acerca de nosotros:** La cual ofrece una breve reseña acerca de la tienda.
* **Servicios:** En donde se destacan algunas cualidades o servicios distintivos del negocio.
* **Productos:** Algunos productos que el negocio comercializa, exhibidos en ramas generales o familias de repuestos. Las imagenes pueden seleccionarse para visualizarlas en mayor tamaño en forma de carrusel 
* **Tienda:** La cual redirecciona a la tienda en linea
* **Contacto:** Ofrece un formulario de contacto para que las personas puedan dejar sus consultas. Las consultas enviadas pueden visualizarse desde la página de administrador accediendo a la tabla "Contact".  
-Estuvo en plan la opción de sumar la funcionalidad que las consultas sean enviadas a través de email, no obstante para ello se hacía necesario crear una nueva casilla de correo exclusiva para que funcione como motor de envío, configurar el servidor SMTP y demás configuraciones que además requererían exponer las credenciales. Por que lo que por motivos de seguridad se descartó la posibilidad y se optó por el almacenamiento en una base de datos-.

<br>

# Tienda en linea

La misma puede ser accedida por los botones de "Tienda" presentes en la página de inicio, tanto en la barra de navegación como en el cuerpo de la página; o tambien ingresando a la URL principal seguido de /shop/index o shop/products (Ejemplo: localhost:[port]/shop/index).

Allí se observarán todos los productos publicados en forma de tarjetas y una barra de búsqueda la cual permitirá realizar busquedas según nombre del producto y por número de pieza en caso de saberlo.

<br>

<image
  src="doc\readme images\1.png"
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=250px>

Cada producto tendrá el su nombre (o descripción), una valoración en estrellas, su precio (expresado en USD) y un botón de **_Añadir al carrito_**. En la parte superior derecha se observa una pequeña etiqueta **_En stock_** si el producto posee existencias. En el caso que no, se observará **_Agotado_** y el botón de **_Añadir al carrito_** se convertirá en **_Consulte stock_**, como puede observarse a continuación:

<image
  src="doc\readme images\2.png" 
  alt="Descripción de la imagen"
  caption="Producto sin stock"
  width=200px>

<br>

Al presionar la imagen o el nombre del producto se accederá a una información extendida de cada producto de forma individual.

## Productos individuales
---
La siguiente página muestra una mirada mas cercana de cada producto en donde puede obervarse, así como en las tarjetas, información del producto además de su SKU (código de pieza), su precio origial y el rebajado y una descripción la cual en este caso habla sobre la aplicación de la pieza.

<image
  src="doc\readme images\3.png" 
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=550px>

Se posee al lado del boton **_Añadir al carrito_**, un campo que permite seleccionar la cantidad de unidades del producto que quieren agregarse al carrito.

##### -En caso de estar interesado en algun producto, puede presionar el botón **_Añadir al carrito_**, no obstante, primero le solicitará estar logueado en la página y de no poseer una cuenta, podrá registarse, tanto desde el botón **_Registrate_** en la barra de navegación, como podrá ser redireccionado a la mismo lugar ingresando en el botón **_Iniciar sesión_** (en la barra de navegación) y luego seleccionando el hipervinculo _Regístrese_.-

Finalmente, dentro de la misma página en la parte inferior podrá encontrar la sección de "_Productos relacionados_" en donde podrá encontrar más productos.

<br>

## Registro de usuarios
---
Como fue expuesto anteriormente, esta sección es accesible tanto desde el botón **_Registrate_** en la barra de navegación, como podrá ser redireccionado a la mismo lugar ingresando en el botón **_Iniciar sesión_** (en la barra de navegación) y luego seleccionando el hipervinculo _Regístrese_.-  
El mismo consta de un formulario simple de registro, en donde se solicita: 
* **Nombre**
* **Apellido**
* **DNI**
* **Teléfono**
* **Dirección**
* **Email**
* **Nombre de usuario**
* **Contraseña**  

Algunos de éstos campos tienen requerimientos espciales los cuales se encuentran detallados debajo de cada campo en cuestión. 
Los datos mas alla de _Nombre de usuario_, _Email_ y _Contraseña_ son solicitados teniendo en cuenta que se trata de una tienda la cual trabaja con pedidos en donde los mismos deben ser correctamente indentificables con quien haya realizado la compra. 

En caso de haber superado satisfactoriamente el registro (caso contrario se expondrá un mensaje de error), usted será redirigido a la página de inicio ya siendo logueado en donde podrá continuar navegando y comprando dentro del sitio.

<br>

## Inicio de sesión
---
Accediendo desde el boton correspoendiente en la barra de navegación será posible loguearse en el sitio con una cuenta ya registrada.  
El formulario contará con dos campos:
* **Nombre de usuario**
* **Contraseña**

Una vez los mismos sean rellenados con los datos correspondientes, presione en el boton **_Enviar_** para iniciar sesión. Se haber ingresado de forma correcta, será redirigido a la página principal, caso contrario de expondrá un mensaje de error.

Para cerrar la sesión sitúese en la barra de navegación en el extremo derecho y seleccione **_Cerrar sesión_**.

## Mi perfil
---
Una vez logeado podrá observar que en la barra de navegación en el extremo derecho se mostrará una foto de un avatar generico gris, seguido de un saludo hacia usted. Al tocar en dicho saludo de desplegará un menú en el cual la seguna opción es **_Mi peril_**.  
Al entrar en ella podrá observar en la sección izquierda su avatar y la información ingresada al registrarse.  

<image
  src="doc\readme images\4.png" 
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=590px>

Para editar cualquier información de estas, sitúese en la sección derecha denominada *"Editar datos de usuario"*. Los campos ya se encontrarán pre-rellenados con la información actual que usted posee. En caso de querer editar algun dato en particular, basta con borrar lo que se encuentra escrito y colocar la información deseada. En caso de no querer editar algun campo, basta con dejarlos como estan (con la información actual) o borrar su contenido, es indistinto.  
Se añadieron los campos -optativos- *Avatar* y *Redes/URL* en los cuales podrá subir una imagen para que sea asociada a su contacto y subir una URL de contacto de usted, respectivamente.

Una vez cargada toda la información a actualizar, presione el botón **_Actualizar datos_** en donde podrá visualizar la nueva información.

## Cambio de contraseña
---
Otra de las opciones presentes en el menú deplegable debajo de su nombre es **_Cambiar contraseña_**. Al presionar éste, se abrirá una página similar a la de *Mi perfil* en donde en la sección derecha se expondrán los campos necesarios para poder actualizar la contraseña:
* Contraseña actual
* Nueva contraseña
* Confirmar nueva contraseña

Los requisitos para rellenar cada campo se encuentran expuestos debajo de cada casillero en cuestión. Los requisitos para la nueva contraseña serán los mismos que fueron solicitados al registrar su usuario:
* Su contraseña no puede ser muy similar a su otra información personal.
* Su contraseña debe contener al menos 8 caracteres
* Su contraseña no puede ser una contraseña de uso común
* Su contraseña no puede ser completamente numérica.

Una vez rellenados los campos, presione en **_Cambiar contraseña_**. En caso de haberse concretado la actualizacion de forma correcta, usted será redirigido a la página **_Mi perfil_**, caso contrario, se mostrará un mensaje de error por lo que deberá chequear y volver a ingresar los datos incorrectos.

<br>

## Carrito de compras
---
Una vez completado los pasos anteriores (es decir, tener una cuenta y estar logueado) se podrán agregar articulos al carrito y realizar pedidos. En caso de no haber completado los pasos, solicitará al usuario logueo -para más información, ver secciones anteriores en el presente documento.-  
<br>
Para comenzar, agregue productos al carrito. Hay dos formas de hacerlo:
* Desde las tarjetas: Presentes en la página de inicio y en la sección de "_productos relacionados_" cuando se visualiza un articulo puntual. Allí se agregará al carrito 1 unidad del producto en cuestión

<image
  src="doc\readme images\1.png"
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=250px>

* Desde la sección de productos individuales: Como ya comentamos, se accede a la misma presionando la imagen o el nombre de un articulo en la tarjeta para ver su información ampliada. Allí, a diferencia de agregar al carrito desde las tarjetas, desde esta sección pueden agregarse multiples unidades de un mismo articulo, mediante el campo de entrada numerica a la izquierda del boton **_Añadir al carrito_**

<image
  src="doc\readme images\3.png" 
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=550px>

<br>

Al realizar la adición de el/los producto/s, usted sera redirigido al carrito de compras en donde podrá observar el producto que acaba de agregar asi como la cantidad correspondiente.

<image
  src="doc\readme images\5.png" 
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=800px>

<br>

Obervando cada linea de izquierda a derecha, primeramente se observa el nombre del producto y un botón llamado _Borrar articulo_ el cual, como su nombre lo indica, el presionarlo eliminara completamente todas las unidades que posea de ese articulo dentro del carrito.  
Luego, donde se exhibe la cantidad, se encuentra un boton con un "signo menos" _("-")_, el cual se encarga de restar 1 unidad del producto en cuestion. En caso de solo haber seleccionado 1 unidad, al restar la misma el producto desaparecerá del carrito.  
Análogamente, a la derecha del cuadro se observa un "signo más" (_"+"_) el cual cumple la función de agregar 1 unidad del producto en cuestión.  
La siguiente columna muestra el valor unitario del producto el cual al multiplicarlo por la cantidad seleccionada, muestra el valor presente en la columna _"Precio total"_.  
Debajo de la sección de productos, se encuentra el botón _Vaciar carrito_, el cual borra todos los articulos y sus respectivas cantidades (en caso de tener varios) del carrito, en caso que el usuario desista de continuar la compra.  
Por utlimo, se exhibe el _**Subtotal**_ el cual es el resultado de sumar los _Precios Totales_ de todos los articulos.

<br>

En caso de querer seguir agregando productos al carrito, nos dirigimos a la barra de navegación y presionamos el boton **_Home/Productos_** para seguimos agregando productos al carrito.

<image
  src="doc\readme images\6.png" 
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=800px>

<br>

Una vez se desea confirmar el pedido, basta con seleccionar dicho botón verde. Alli seremos redireccionados a una página de confimación en donde se nos informará acerca de nuestro numero de pedido y se nos invitará a la página principal o a la sección de pedidos.

<image
  src="doc\readme images\7.png" 
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=800px>

<br>

## Pedidos
---
Una vez realizado el pedido puede accederse desde el vinculo de redirección que aparece en la pantalla de confirmación asi como tambien en el menú despegable en la barra de navegación.  

<br>

Esta sección es dinámica y el contenido que mostrará dependerá de los privilegios que tenga el usuario:
* Usuario común / cliente: Podrá unicamente ver los pedidos que él ha realizado y los que ha pagado

<image
  src="doc\readme images\8.png" 
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=800px>

<br>

* Usuario que sea parte del staff: Este tipo de perfiles estan pensados para quienes se encargarán de administrar la página. Ellos (entre otras cosas) verán los pedidos generados por todos los usuarios y podrán declarar como pagados los mismos.  
Dado que el proyecto no se encuentra en producción, no se poseen metodos de pago reales, por que lo se optó por utilizar una confirmación de pago manual mediante un checkbox a la derecha de cada pedido. La forma de confirmar un pago consta de seleccionar el checkbox de el/los pedido/s que se desean atestiguar como pagados y luego presionar el botón _**Actualizar registros**_. Con esto, todos estos pedidos pagados pasarán a la sección _**"Pagados"**_ en donde los cada usuario tambien podrá ver este cambio desde su sección de pedidos.

<image
  src="doc\readme images\9.png" 
  alt="Descripción de la imagen"
  caption="Producto en stock"
  width=900px>

<br>
<br>
<br>

# Página de administrador

Dado que el superusuario podrá realizar todo tipo de cambios y modificaciones desde dicha la página de administrador, enfocaremos esta sección a aquellos usuarios que tienen acceso a esta página más no poseen todos los permisos habilitados. Estos usuarios serán denominados _"Administradores"_ y serán los encargados de mantener el proceso diario de la página. Sus permisos quedarán limitados a un grupo de permisos llamados _"Admninistradores"_.  
Desde el panel de administración los administradores podrán:

* Visualizar todos los pedidos y editar los productos que los componen, excepto si fue pagado o no (porque eso se realiza desde la web) y editar el cliente que realizó el pedido (para eso se requiere elevación).

* Añadir y editar productos de forma completa.

* Ver y editar datos de contacto: DNI, teléfono, dirección, avatar y la URL. Para modificar otros datos se requiere elevación.

* Visualizar las consultas que envían los usuarios desde el formulario de la página de inicio.

Cualquier otra acción que se desee realizar debe solicitarse elevación dado que algun cambio de los que no se encuentran autorizados podría afectar información importante y comprometer relaciones de datos. En ese caso, deberan intervenir los superusuarios.   Proximamente podría desarrollarse algun usuario intermedio el cual, sin ser superusuario, pueda llegar a realizar alguna tarea adicional.

<br>

--- <a name="final"></a>

Habriendo cubrido todas las secciones que componen a esta página web, damos por finalizada esta guía explicativa. No obstante, cualquier consulta o comentario pueden escribirme a mi dirección de correo: fawzielgamal@icloud.com

<br>

## Gracias por su atención!<a name="final"></a>
<div id="final" />



