import requests
from PIL import Image
from PIL import UnidentifiedImageError
from flask import Flask, render_template, request, flash
# EGG jack VISA WALMART MUSIC 2 3 jack { , [ ( GOLF % 5 DRIP 
app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'EjVWM23j{,[(G%5D'

@app.route('/')
def mostrar():
    return render_template('index.html')

@app.route('/descargar', methods=['GET', 'POST'])
def descargar():
    forma = request.form
    if request.method == 'POST':
        print('HOLAAAAAAAAAAAAAAAAAAAA')
        print(forma['imagen'])
        try:
            direccion = 'C:\\Users\\user\\Downloads\\'
            data = requests.get(forma['imagen']).content
            with open(f'{direccion}nueva.png', 'wb') as handler:
                handler.write(data)
            
            imagen = Image.open(f'{direccion}nueva.png')
            imagen.show()
            imagen.save(f'{direccion}nueva.ico', format='ICO')
        except UnidentifiedImageError or TypeError or ValueError or FileNotFoundError:
            flash('Bueh... Parece que algo salió mal... Pero no te preocupes, no es tu culpa (es culpa de tu imagen :V)')
        except Exception:
            flash('Bueh... Parece que algo salió mal... Puede que sea tu culpa... Como puede que sea que no')
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)