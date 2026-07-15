from flask import Flask, render_template, request 
from models.logica import *

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/combustivel', methods = ['GET', 'POST'])
def combustivel():
    total = None
    mensagem = None

    if request.method == 'POST':
        litros = float(request.form['litros'])
        preco = float(request.form['preco'])
        total, mensagem = calcular_combustivel(litros,preco)

    return render_template('combustivel.html', total=total, mensagem=mensagem)

@app.route('/joias', methods = ['GET', 'POST'])
def joias():
    resultado = None

    if request.method == 'POST':
        valor = float(request.form['valor'])
        percentual = float(request.form['percentual'])
        resultado = calcular_joias(valor, percentual)

    return render_template('joias.html', resultado=resultado)


@app.route('/educacao', methods = ['GET', 'POST'])
def educacao():
    media = None
    status = None

    if request.method == 'POST':
        n1 = float(request.form['nota1'])
        n2 = float(request.form['nota2'])
        media, status = calcular_media(n1, n2)

    return render_template('educacao.html', media=media, status=status)

if __name__ == '__main__':
    app.run(debug=True)
