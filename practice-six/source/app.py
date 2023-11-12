# Importamos las librerías necesarias.
from flask import Flask, flash, redirect, render_template, request, url_for
from models.ModelUsers import ModelUsers
from models.entities.users import User
from flask_mysqldb import MySQL
from config import config

# Establecemos la configuración de la aplicación.
app = Flask(__name__)
db = MySQL(app)

# Definimos las rutas de la aplicación.
# Ruta principal.
@app.route("/")
def index():
    return redirect("login")

# Ruta para el registro de usuarios.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User(0, request.form['username-input'], request.form['password-input'],0)
        logged_user = ModelUsers.login(db, user)
        if logged_user != None:
            if logged_user.usertype == 1:
                return redirect(url_for("admin"))
            else:
                return redirect(url_for("home"))
        else:
            flash("Usuario o contraseña incorrectos.")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")

# Ruta de menú principal para usuarios normales.
@app.route("/home")
def home():
    return render_template("public/home.html")

# Ruta de menú principal para usuarios administradores.
@app.route("/admin")
def admin():
    return render_template("public/admin.html")

# Ruta para cerrar sesión.
if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()