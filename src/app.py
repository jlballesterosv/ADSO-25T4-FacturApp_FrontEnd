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


@app.route('/product/new', methods=['GET', 'POST'])
def new_product():
    if request.method == 'POST':
        # (Aquí va la lógica de captura de datos...)
        return redirect(url_for('index'))
    return render_template('form_products.html')


@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        nombre_completo = request.form.get('nombre_completo')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        rol = request.form.get('rol')
        
        print(f"Creando cuenta de usuario: {username} con Rol: {rol}")
        return redirect(url_for('index'))
        
    # Ajusta a 'users/form_users.html' si lo guardaste dentro de la subcarpeta de usuarios
    return render_template('form_users.html')



# 3. Al final del todo se corre el servidor
if __name__ == '__main__':
    app.run(debug=True)
