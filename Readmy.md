🎬 CineZone — Proyecto Final ASIX
🌟 Descripción del proyecto
CineZone es una aplicación web desarrollada con Flask y MySQL como proyecto final del módulo
Implantació d’Aplicacions Web (ASIX).

El sitio permite:

Registro e inicio de sesión de usuarios

Acceso a una zona privada

Publicación de reseñas de películas

Visualización de un catálogo de 10 películas

Página “About me” con portafolio del alumno

Todo con un diseño moderno basado en Bootstrap 5, animaciones CSS y una estructura profesional.

🧩 Características principales
🔓 Parte pública
Catálogo de 10 películas con tarjetas visuales

Animaciones suaves y diseño responsive

Página “About me” con proyectos del alumno

Acceso a login y registro

🔐 Parte privada
Bienvenida personalizada

Formulario para añadir reseñas

Listado de reseñas creadas por el usuario

Cierre de sesión

🗄️ Base de datos
📌 Tabla registro
Campo	Tipo
Nombre	varchar(50)
Mail	varchar(50)
Contraseña	varchar(50)
Fecha	varchar(50)
📌 Tabla reseñas
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

Jinja2 (templates)

📦 Instalación y ejecución
1️⃣ Clonar el repositorio
bash
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
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
La web estará disponible en:

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
🎨 Diseño y estilo
La web incluye:

Navbar moderna con iconos

Cards animadas para películas

Hover effects y sombras dinámicas

Footer minimalista

Formularios estilizados

Animaciones suaves al cargar contenido

Todo el estilo personalizado está en:

Código
static/css/estilos.css
👤 Autor
Diego — 2º ASIX  
Proyecto final del módulo Implantació d’Aplicacions Web.

📄 Licencia
Proyecto de uso educativo.
