from flask import Flask
from flask_mysqldb import MySQL

# Inicializamos la aplicación Flask
app = Flask(__name__)  # __name__ indica que este es el punto de entrada del programa

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'  # Servidor MySQL
app.config['MYSQL_USER'] = 'root'  # Usuario de MySQL
app.config['MYSQL_PASSWORD'] = 'contraseña'  # Cabiar por contraseña de MySQL
app.config['MYSQL_DB'] = 'user_management'  # Nombre de la base de datos

mysql = MySQL(app)  # Inicializamos la extensión MySQL

# Definimos la ruta principal ("/") que devuelve un mensaje al acceder
@app.route('/')
@app.route('/test-db')
def test_db():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    cursor.close()
    return f"Conectado a la base de datos: {db_name[0]}"

# Comprobamos si este archivo se ejecuta directamente (no cuando es importado)
if __name__ == '__main__':
    """
    Ejecutamos la aplicación en modo de desarrollo.
    debug=True permite ver errores en tiempo real sin reiniciar el servidor manualmente.
    """
    app.run(debug=True)