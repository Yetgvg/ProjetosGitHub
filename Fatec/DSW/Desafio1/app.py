from flask import Flask,render_template,url_for

app = Flask("__name__")

@app.route("/")
def index(): 
    return render_template('index.html')

@app.route("/quemsomos.html")
def quemsomos(): 
    return render_template('quemsomos.html')

@app.route("/contatos.html")
def contatos(): 
    return render_template('contatos.html')

if __name__ == "__main__":
    app.run(debug=True)