from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__) 


info_usuarios = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


@app.route("/list")
def tabla():
    return render_template("index.html", usuarios= info_usuarios)


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True) 