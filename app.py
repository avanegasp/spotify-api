from flask import Flask
from app.routes import main

#Inicia una aplicación Flask. 
# El parámetro __name__ le dice a Flask dónde 
# encontrar los archivos relacionados con el proyecto.
app = Flask(__name__)

app.register_blueprint(main)

if __name__ == "__main__":   
    app.run(debug=True)
#Inicia el servidor web de Flask en modo de depuración, lo que 
# facilitaría ver errores y reinicia automáticamente el servidor 
# cuando realizas cambios en el código. 
