from PIL import Image
import os

def reduce_image_size(folder_path):
    # Recorre todas las subcarpetas de la carpeta principal
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Verifica que el archivo sea una imagen
            if file.endswith(".jpg") or file.endswith(".png"):
                # Carga la imagen
                image_path = os.path.join(root, file)
                image = Image.open(image_path)
                # Reduce el tamaño de la imagen
                new_size = tuple([int(x/2) for x in image.size])
                image = image.resize(new_size, Image.ANTIALIAS)
                # Guarda la imagen reducida en el mismo archivo
                image.save(image_path, optimize=True, quality=85)
                print("Imagen reducida:", image_path)

# Llama a la función para reducir el tamaño de las imágenes en una carpeta y sus subcarpetas
reduce_image_size("/Users/mateoherasvera/Library/CloudStorage/OneDrive-Personal/GitHub/USA-J4-Home-Improvements/images")
