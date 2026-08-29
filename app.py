from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vehiculos')
def pagina_vehiculos():
    return render_template('vehiculos.html')

@app.route('/contacto')
def pagina_contacto():
    return render_template('contacto.html')

@app.route('/buscar', methods=['POST'])
def buscar_vehiculos():
    aeropuerto = request.form.get('recogida')
    fecha_inicio = request.form.get('fecha_recogida')
    return redirect(url_for('pagina_vehiculos'))

if __name__ == '__main__':
    app.run(debug=True)