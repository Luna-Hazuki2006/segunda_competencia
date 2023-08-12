import requests
from cryptography.fernet import Fernet
from PIL import Image
from PIL import UnidentifiedImageError
from flask import Flask, render_template, request, flash
# EGG jack VISA WALMART MUSIC 2 3 jack { , [ ( GOLF % 5 DRIP 
app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'EjVWM23j{,[(G%5D'
direccion = 'C:\\Users\\d\\Downloads\\'

@app.route('/')
def mostrar():
    return render_template('index.html')

@app.route('/imagenes', methods=['GET', 'POST'])
def descargar():
    forma = request.form
    if request.method == 'POST':
        try:
            direccion = forma['direccion']
            data = requests.get(forma['imagen']).content
            nombre = forma['nombre']
            with open(f'{direccion}{nombre}.png', 'wb') as esto:
                esto.write(data)
            imagen = Image.open(f'{direccion}{nombre}.png')
            imagen.show()
            size = imagen.size
            ico = Image.new(mode="RGBA", size=(max(size), max(size)), color=(0, 0, 0, 0))
            ico.paste(imagen, (int((max(size)-size[0])/2), int((max(size)-size[1])/2)))
            ico.save(f"{direccion}{nombre}.ico", format='ICO', quality=1000)
            ico.show()
        except UnidentifiedImageError or TypeError or ValueError or FileNotFoundError:
            flash('Bueh... Parece que algo salió mal... Pero no te preocupes, no es tu culpa (es culpa de tu imagen :V)')
        except Exception:
            flash('Bueh... Parece que algo salió mal... Puede que sea tu culpa... Como puede que sea que no')
    return render_template('/imagenes/index.html') 

@app.route('/encriptar', methods=['GET', 'POST'])
def encriptar():
    forma = request.form
    if request.method == 'POST':
        direccion = forma['direccion']
        texto = forma['texto']
        secreto = Fernet.generate_key()
        encriptador = Fernet(secreto)
        encriptado = encriptador.encrypt(bytes(texto, 'utf-8'))
        with open(f'{direccion}contraseña.txt', 'w+') as esto:
            esto.writelines([
                'Texto encriptado: \n', 
                str(encriptado, 'utf-8'), 
                '\nClave: \n', 
                str(secreto, 'utf-8')
            ])
        flash('Se creó el archivo de texto con la información encriptada con éxito')
        render_template('/encriptar/index.html')
    return render_template('/encriptar/index.html')

@app.route('/desencriptar', methods=['GET', 'POST'])
def desencriptar():
    if request.method == 'POST':
        encriptado = ''
        llave = ''
        with open(f'{direccion}contraseña.txt', 'r') as esto:
            esto.readline()
            encriptado = esto.readline()
            esto.readline()
            llave = esto.readline()
        llave = bytes(llave, 'utf-8')
        encriptador = Fernet(llave)
        texto = encriptador.decrypt(encriptado)
        with open(f'{direccion}desencriptado.txt', 'w+') as esto:
            esto.writelines([
                'Texto desencriptado: \n', 
                str(texto, 'utf-8'), 
                '\nClave: \n', 
                str(llave, 'utf-8')
            ])
        flash('Se creó el archivo con la información desencriptada con éxito')
        render_template('/desencriptar/index.html')
    return render_template('/desencriptar/index.html')

if __name__ == '__main__':
    app.run(debug=True)