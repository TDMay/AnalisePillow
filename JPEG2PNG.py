# Salvando uma imagem JPEG como PNG

from PIL import Image

# Abrindo uma imagem
imagem = Image.open('/home/may/Code/Pillow/images/image.jpeg')

# Salvando a imagem em outro formato
imagem.save('/home/may/Code/Pillow/images/nova_imagem.png')