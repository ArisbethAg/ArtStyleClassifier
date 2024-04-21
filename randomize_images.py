import os
import random
import shutil

def separar_imagenes_aleatorias(ruta_origen, ruta_destino, numero_imagenes):
    # Obtener la lista de archivos en la carpeta de origen
    archivos = os.listdir(ruta_origen)

    # Seleccionar de forma aleatoria el número especificado de imágenes
    imagenes_seleccionadas = random.sample(archivos, numero_imagenes)

    for imagen in imagenes_seleccionadas:
        ruta_imagen_origen = os.path.join(ruta_origen, imagen)
        ruta_imagen_destino = os.path.join(ruta_destino, imagen)

        shutil.move(ruta_imagen_origen, ruta_imagen_destino)

ruta_origen = '/Users/arisbethaguirre/Downloads/PaintingsDataset/train/NonImpressionism'
ruta_destino = '/Users/arisbethaguirre/Downloads/PaintingsDataset/validation/NonImpressionism'
numero_imagenes = 108  # Número de imágenes aleatorias que quieres seleccionar y mover

separar_imagenes_aleatorias(ruta_origen, ruta_destino, numero_imagenes)
