from flask import Flask  
app = Flask(__name__)    
@app.route('/')         
def hola_mundo():
    return 'Hola Mundo!'


@app.route('/dojo')
def success():
  return "dojo"
app.run(debug=True) 


@app.route('/say/<string:benja>', methods=['GET'])
def saludar(nombre):
    return f"Hola {nombre}"


@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id




if __name__=="__main__":   
    app.run(debug=True)    