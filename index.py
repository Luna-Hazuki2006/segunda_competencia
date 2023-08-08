import requests
from PIL import Image

url = input('Escribe el url:\n')

data = requests.get(url).content

with open('nueva.png', 'wb') as handler:
    handler.write(data)

imagen = Image.open('nueva.png')
imagen.show()