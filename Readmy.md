🎬 CineZone
CineZone es una aplicación web desarrollada con Flask y MySQL como proyecto final del módulo Implantació d’Aplicacions Web (ASIX).
La web permite a los usuarios registrarse, iniciar sesión, acceder a una zona privada y publicar reseñas de películas.
Incluye una parte pública con un catálogo visual de 10 películas y una página “About me”.

🚀 Funcionalidades
🔓 Parte pública
Página de inicio con 10 películas destacadas.

Diseño moderno con Bootstrap 5, animaciones y cards visuales.

Página About me con portafolio del alumno.

Acceso a login y registro.

🔐 Parte privada
Acceso solo para usuarios registrados.

Página de bienvenida personalizada.

Formulario para añadir reseñas.

Listado de reseñas creadas por el usuario.

Cierre de sesión.

🗄️ Base de datos
La aplicación utiliza MySQL con dos tablas:

Tabla registro
Campo	Tipo
Nombre	varchar(50)
Mail	varchar(50)
Contraseña	varchar(50)
Fecha	varchar(50)
Tabla reseñas
Campo	Tipo
id	int AUTO_INCREMENT PRIMARY KEY
usuario	varchar(50)
titulo	varchar(100)
resena	text
puntuacion	int
🛠️ Tecnologías utilizadas
Python 3

Flask

MySQL / phpMyAdmin

Bootstrap 5

HTML5 + CSS3

FontAwesome

📦 Instalación
1️⃣ Clonar el repositorio
bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
(Sustituye TU-USUARIO y TU-REPO por los reales.)

2️⃣ Instalar dependencias
bash
pip install -r requirements.txt
Contenido del archivo:

Código
flask
mysql-connector-python
3️⃣ Configurar MySQL
Inicia MySQL (XAMPP, WAMP o Workbench).

Crea la base de datos:

Código
base de datos proyecto
Crea las tablas registro y reseñas con los campos indicados arriba.

Asegúrate de que los nombres coinciden exactamente.

4️⃣ Ejecutar la aplicación
bash
python app.py
Flask mostrará:

Código
Running on http://127.0.0.1:5000
Abre tu navegador y entra en:

Código
http://127.0.0.1:5000
🖼️ Imágenes necesarias
Coloca estas imágenes en:

Código
static/img/
Nombres requeridos:

Código
peli1.jpg
peli2.jpg
peli3.jpg
peli4.jpg
peli5.jpg
peli6.jpg
peli7.jpg
peli8.jpg
peli9.jpg
peli10.jpg
logo.png
🎨 Diseño
La web utiliza:

Navbar moderna con iconos.

Cards animadas para las películas.

Animaciones suaves al cargar contenido.

Footer minimalista.

Formularios estilizados con Bootstrap.

Estilos personalizados en:

Código
static/css/estilos.css
👤 Autor
Diego — 2º ASIX  
Proyecto final del módulo Implantació d’Aplicacions Web.

📄 Licencia
Proyecto de uso educativo.
