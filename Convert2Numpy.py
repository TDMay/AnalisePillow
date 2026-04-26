from PIL import Image

imagem = Image.open("/home/may/Code/Pillow/images/image.jpeg")

import numpy as np

array = np.array(imagem)

print(array)

with open("/home/may/Code/Pillow/images/numpy.txt","w") as texto:
    texto.write(str(array))
