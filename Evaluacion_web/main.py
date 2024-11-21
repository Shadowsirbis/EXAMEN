from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/funcionamiento')
def funcionamiento():
    return render_template('funcionamiento.html')

@app.route('/contactanos')
def contacto():
    return render_template('contactanos.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# ejercicio N°1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio = 9000
        total_sin_descuento = precio * cantidad

        # Determinar descuento según la edad
        if edad >= 18 and edad <= 30:
            descuento = 0.15  # 15% de descuento
        elif edad > 30:
            descuento = 0.25  # 25% de descuento
        else:
            descuento = 0.0  # Sin descuento si es menor de 18

        total_con_descuento = total_sin_descuento * (1 - descuento)  # Aplicar descuento

        # Pasar todos los valores a la plantilla HTML
        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               descuento=descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html', methods=['GET', 'POST'])


usuarios = {
    'juan': {'contraseña': 'admin', 'rol': 'administrador'},
    'pepe': {'contraseña': 'user', 'rol': 'usuario'}
}

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Verificar si el usuario existe y la contraseña es correcta
        if usuario in usuarios and usuarios[usuario]['contraseña'] == contrasena:
            # Mensaje de bienvenida según el rol
            if usuarios[usuario]['rol'] == 'administrador':
                mensaje = f'Bienvenido administrador {usuario}'
            elif usuarios[usuario]['rol'] == 'usuario':
                mensaje = f'Bienvenido usuario {usuario}'
        else:
            # Mensaje de error si usuario o contraseña son incorrectos
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)