from flask import render_template, request, redirect, url_for
from src import create_app

# 1. Primero se inicializa la aplicación
app = create_app()

# 2. SEGUNDO colocas la ruta del formulario DEBAJO de 'app = create_app()'
@app.route('/client/new', methods=['GET', 'POST'])
def new_client():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        id_type = request.form.get('idType')
        id_number = request.form.get('idNumber')
        phone = request.form.get('phone')
        email = request.form.get('email')
        adress = request.form.get('adress')
        
        print(f"Registrando cliente: {nombre} - {id_type}: {id_number}")
        return redirect(url_for('index')) # O 'home' según tu ruta principal
        
    return render_template('clients/form_clients.html')

# 3. Al final del todo se corre el servidor
if __name__ == '__main__':
    app.run(debug=True)
