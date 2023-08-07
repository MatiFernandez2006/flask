from flask import Flask, render_template  # agregado render_template!
app = Flask(__name__)                     
    
@app.route('/')                           
def hola_mundo():
    # En lugar de devolver una cadena, 
    # devolveremos el resultado del método render_template, pasando el nombre de nuestro archivo HTML
    return render_template('index.html')  
    
if __name__=="__main__":
    app.run(debug=True)                   
