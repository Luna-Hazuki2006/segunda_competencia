import requests
from PIL import Image

url = 'https://pbs.twimg.com/media/F2-S13FXsAAet9_?format=jpg&name=900x900'

data = requests.get(url).content

with open('nueva.png', 'wb') as handler:
    handler.write(data)