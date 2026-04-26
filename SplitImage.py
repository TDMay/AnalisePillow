# Separando uma imagem em 3 vertentes: Vermelha Verde e Azul

from PIL import Image

imagem = Image.open("/home/may/Code/Pillow/images/image.jpeg")

red, green, blue = imagem.split()

red.save('/home/may/Code/Pillow/images/imagemVermelha.png')
green.save('/home/may/Code/Pillow/images/imagemVerde.png')
blue.save('/home/may/Code/Pillow/images/imagemAzul.png')