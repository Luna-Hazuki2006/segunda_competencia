import requests
from PIL import Image
from flask import Flask, render_template
# EGG jack VISA WALMART MUSIC 2 3 jack { , [ ( GOLF % 5 DRIP 
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'EjVWM23j{,[(G%5D'

@app.route('/', methods=['GET'])
def mostrar():
    return render_template('/templates/index.html')

@app.context_processor
def descargar(url):
    try:
        data = requests.get(url).content

        with open('nueva.png', 'wb') as handler:
            handler.write(data)

        imagen = Image.open('nueva.png')
        imagen.show()
    except Exception:
        print('Bueh... Parece que algo salió mal... O tal vez TÚ te equivocaste')

if __name__ == '__main__':
    app.run(debug=True)