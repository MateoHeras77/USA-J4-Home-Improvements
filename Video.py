import os
import moviepy.editor as mp
from PIL import Image

# Define la ruta de la carpeta que contiene los videos
ruta_videos = '/Users/mateoherasvera/Library/CloudStorage/OneDrive-Personal/GitHub/USA-J4-Home-Improvements/images/test/'

# Define la ruta de la carpeta de salida para los GIFs
ruta_gifs = '/Users/mateoherasvera/Library/CloudStorage/OneDrive-Personal/GitHub/USA-J4-Home-Improvements/images/test/'

# Duración objetivo del GIF (en segundos)
duracion_gif = 15

# Recorre todos los archivos en la carpeta de videos y subcarpetas
for directorio_raiz, directorios, archivos in os.walk(ruta_videos):
    for archivo in archivos:
        # Comprueba si el archivo es un video
        if archivo.endswith('.mp4') or archivo.endswith('.avi') or archivo.endswith('.mov'):
            # Carga el video utilizando la biblioteca moviepy
            ruta_archivo = os.path.join(directorio_raiz, archivo)
            video = mp.VideoFileClip(ruta_archivo)

            # Recorta el video a la duración deseada
            duracion_real = video.duration
            if duracion_real > duracion_gif:
                inicio = (duracion_real - duracion_gif) / 2
                final = inicio + duracion_gif
                video = video.subclip(inicio, final)

            # Comprueba si el video es vertical u horizontal
            ancho, alto = video.size
            print(alto)
            print(ancho)
            orientacion = 'vertical' if alto < ancho else 'horizontal'
            print(orientacion)

            # Crea un archivo GIF a partir del video
            nombre_gif = archivo.split('.')[0] + '.gif'
            ruta_gif = os.path.join(ruta_gifs, nombre_gif)
            video.write_gif(ruta_gif)

            # Ajusta la relación de aspecto del GIF para que coincida con el video original
            imagen = Image.open(ruta_gif)
            w, h = imagen.size
            if orientacion == 'vertical':
                nueva_w = int((h / w) * w)
                nueva_imagen = imagen.resize((nueva_w, h), Image.ANTIALIAS)
                nueva_imagen.save(ruta_gif)
            elif orientacion == 'horizontal':
                nueva_h = int((w / h) * h)
                nueva_imagen = imagen.resize((w, nueva_h), Image.ANTIALIAS)
                nueva_imagen.save(ruta_gif)