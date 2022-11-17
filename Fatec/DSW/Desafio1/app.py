from flask import Flask,request,render_template,url_for
from flask_mysqldb import MySQL
import funcs

config = funcs.LoadConfig()
app = Flask("__name__")

# Conexão ao banco de dados
app.config['MYSQL_HOST'] = config['host']
app.config['MYSQL_PORT'] = config['port'] #Caso a porta seja a padrão, comentar linha.
app.config['MYSQL_USER'] = config['user']
app.config['MYSQL_PASSWORD'] = config['password']
app.config['MYSQL_DB'] = config['db']

mysql = MySQL(app)

@app.route("/")
def index(): 
    return render_template('index.html')

@app.route("/quemsomos.html")
def quemsomos(): 
    return render_template('quemsomos.html')

@app.route("/contatos.html", methods = ['POST', 'GET'])
def contatos(): 
    resultado = ''
    if request.method == 'POST': 
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cursor = mysql.connection.cursor()
        textoSQL = f"INSERT INTO contatos (assunto, email, descricao) VALUES ('{assunto}', '{email}', '{descricao}');"
        cursor.execute(textoSQL)
        mysql.connection.commit()
        cursor.close()

        resultado = 'sucesso'

    return render_template('contatos.html',resultado=resultado)

@app.route("/users.html")
def users(): 
    cursor = mysql.connection.cursor()
    textoSQL = f"SELECT * FROM contatos;"
    cursor.execute(textoSQL)
    userDetails = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('users.html',userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)