# Transformando imagem para escala cinza

from PIL import Image

# Abrindo uma imagem
imagem = Image.open('/home/may/Code/Pillow/images/image.jpeg')

imagem_cinza = imagem.convert('L')

# Salvando a imagem em outro formato
imagem_cinza.save('/home/may/Code/Pillow/images/imagemCinza.png')