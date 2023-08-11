import requests
from cryptography.fernet import Fernet
from PIL import Image
from PIL import UnidentifiedImageError
from flask import Flask, render_template, request, flash
# EGG jack VISA WALMART MUSIC 2 3 jack { , [ ( GOLF % 5 DRIP 
app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'EjVWM23j{,[(G%5D'

@app.route('/')
def mostrar():
    return render_template('index.html')

@app.route('/imagenes', methods=['GET', 'POST'])
def descargar():
    forma = request.form
    if request.method == 'POST':
        try:
            direccion = 'C:\\Users\\user\\Downloads\\'
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
        texto = forma['texto']
    return render_template('/ecriptar/index.html')

if __name__ == '__main__':
    app.run(debug=True)