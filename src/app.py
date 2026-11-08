from flask import render_template, request, redirect, url_for

# se inicializa la app o dentro de tu Blueprint
@app.route('/client/new', methods=['GET', 'POST'])
def new_client():
    if request.method == 'POST':
        # se captura los datos que viajan desde el formulario cuando se da clic en "Guardar"
        nombre = request.form.get('nombre')
        id_type = request.form.get('idType')
        id_number = request.form.get('idNumber')
        phone = request.form.get('phone')
        email = request.form.get('email')
        adress = request.form.get('adress')
        
        # se simula el guardado imprimiéndolo en la terminal
        print(f"Registrando cliente: {nombre} - {id_type}: {id_number}")
        
        # Redirecciona al panel de control principal tras guardar
        return redirect(url_for('index')) 
        
    # Si entran por primera vez haciendo clic (método GET), les muestra la vista del formulario
    return render_template('form_clients.html')
