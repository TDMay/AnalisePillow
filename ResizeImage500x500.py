# Salvando uma imagem com a rezolução de 500x500

from PIL import Image

# Abrindo uma imagem
imagem = Image.open('/home/may/Code/Pillow/images/image.jpeg')

# Transformando em 500x500
nova_dimensão = (500,500)
imagem_mudada = imagem.resize(nova_dimensão)

# Salvando a imagem em outro formato
imagem_mudada.save('/home/may/Code/Pillow/images/imagem500x500.png')