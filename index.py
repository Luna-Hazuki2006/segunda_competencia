import requests
from PIL import Image

url = 'https://pbs.twimg.com/media/F2_dSQDXwAAh4s_?format=jpg&name=small'

data = requests.get(url).content

with open('nueva.png', 'wb') as handler:
    handler.write(data)

imagen = Image.open('nueva.png')
imagen.show()