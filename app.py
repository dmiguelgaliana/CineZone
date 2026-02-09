from flask import Flask, render_template, request, redirect, session
from database import get_connection
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "clave_secreta_asix"
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        mail = request.form["mail"]
        contraseña = request.form["contraseña"]
        fecha = request.form["fecha"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registro (Nombre, Mail, Contraseña, Fecha) VALUES (%s, %s, %s, %s)",
                       (nombre, mail, contraseña, fecha))
        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        mail = request.form["mail"]
        contraseña = request.form["contraseña"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Nombre FROM registro WHERE Mail=%s AND Contraseña=%s", (mail, contraseña))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["usuario"] = user[0]
            return redirect("/privada")
        else:
            return render_template("login.html", error="Credenciales incorrectas")

    return render_template("login.html")

@app.route("/privada")
def privada():
    if "usuario" not in session:
        return redirect("/login")
    return render_template("privada.html", usuario=session["usuario"])

@app.route("/nueva_resena", methods=["GET", "POST"])
def nueva_resena():
    if "usuario" not in session:
        return redirect("/login")

    if request.method == "POST":
        usuario = session["usuario"]
        titulo = request.form["titulo"]
        resena = request.form["resena"]
        puntuacion = request.form["puntuacion"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reseñas (usuario, título, reseña, puntuacion) VALUES (%s, %s, %s, %s)",
                       (usuario, titulo, resena, puntuacion))
        conn.commit()
        conn.close()

        return redirect("/mis_resenas")

    return render_template("reseña_form.html")

@app.route("/mis_resenas")
def mis_resenas():
    if "usuario" not in session:
        return redirect("/login")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT título, reseña, puntuacion FROM reseñas WHERE usuario=%s", (session["usuario"],))
    datos = cursor.fetchall()
    conn.close()

    return render_template("mis_reseñas.html", reseñas=datos)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
