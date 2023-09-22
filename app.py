from flask import Flask, render_template, request

app = Flask(__name__, static_folder='styles')

@app.route('/', methods=['GET', 'POST'])
def calcular_suma_pares():
    if request.method == 'POST':
        numero_inicio = int(request.form['numero_inicio'])
        numero_fin = int(request.form['numero_fin'])
        suma_pares = sum(x for x in range(numero_inicio, numero_fin + 1) if x % 2 == 0)
        return render_template('index.html', suma_pares=suma_pares)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
