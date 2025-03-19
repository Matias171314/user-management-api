from flask import Flask

# Inicializamos la aplicación Flask
app = Flask(__name__)  # __name__ indica que este es el punto de entrada del programa

# Definimos la ruta principal ("/") que devuelve un mensaje al acceder
@app.route('/')
@app.route('/index')
def index():
    """
    Ruta principal de la aplicación.
    Cuando el usuario visita http://127.0.0.1:5000/, verá el siguiente mensaje.
    """
    return "<h1>Página de Inicio</h1>"

@app.route('/hello/')
@app.route('/hello/<string:name>')
def hello(name = None):
    if name == None:
        return "<h1>Hola Mundo!</h1>"
    else:
        return f"<h1> Hola, {name}!</h1>"

# Comprobamos si este archivo se ejecuta directamente (no cuando es importado)
if __name__ == '__main__':
    """
    Ejecutamos la aplicación en modo de desarrollo.
    debug=True permite ver errores en tiempo real sin reiniciar el servidor manualmente.
    """
    app.run(debug=True)