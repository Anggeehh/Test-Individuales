# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Buscamos el archivo 'perfil_2_3_2.html' dentro de la carpeta /templates
    # También podemos pasar datos como variables (nombre="Angel")
    return render_template("perfil_2_3_2.html", estudiante="Angel Piñero Orellana", nickname="Angeh", id_dev="2026" )

if __name__ == "__main__":
   
    app.run(debug=True) 