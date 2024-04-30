from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def  web_simple():
   
    return render_template('index.html')

@app.route('/busca')
def  web_simple_busca():
   
    return render_template('busca.html')


if __name__ == '__main__':
    app.run()