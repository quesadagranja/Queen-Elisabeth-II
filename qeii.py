from PIL import Image

def create_mirrored_image(input_file, output_file):
    try:
        # Abrir la imagen original
        original = Image.open(input_file)

        # Crear la imagen en espejo horizontal
        mirrored_horizontal = original.transpose(Image.FLIP_LEFT_RIGHT)

        # Crear la imagen en espejo vertical
        mirrored_vertical = original.transpose(Image.FLIP_TOP_BOTTOM)

        # Crear la imagen en espejo horizontal y vertical
        mirrored_both = mirrored_horizontal.transpose(Image.FLIP_TOP_BOTTOM)

        # Obtener las dimensiones de la imagen original
        width, height = original.size

        # Crear una nueva imagen de tamaño 2M x 2N
        new_image = Image.new('RGB', (2 * width, 2 * height))

        # Pegar las imágenes en sus respectivas posiciones
        new_image.paste(original, (0, 0))  # Esquina superior izquierda
        new_image.paste(mirrored_horizontal, (width, 0))  # Esquina superior derecha
        new_image.paste(mirrored_vertical, (0, height))  # Esquina inferior izquierda
        new_image.paste(mirrored_both, (width, height))  # Esquina inferior derecha

        # Guardar la nueva imagen en el archivo de salida
        new_image.save(output_file)
        print(f"Imagen procesada y guardada en: {output_file}")

    except Exception as e:
        print(f"Error procesando la imagen: {e}")

def reorder_image_bands(input_file, output_file, pixel_ratio):
    try:
        # Abrir la imagen procesada
        original = Image.open(input_file)

        # Obtener las dimensiones de la imagen
        width, height = original.size

        # Calcular el número de bandas verticales en función del ancho y pixel_ratio
        V = max(2, width // pixel_ratio)

        # Calcular el ancho de cada banda
        band_width = width // V

        # Crear una lista para almacenar las bandas
        bands = []

        # Dividir la imagen en V bandas verticales
        for i in range(V):
            band = original.crop((i * band_width, 0, (i + 1) * band_width, height))
            bands.append(band)

        # Reordenar las bandas en el orden 1-V, 2-(V-1), 3-(V-2), ...
        reordered_bands = []
        for i in range(V // 2):
            reordered_bands.append(bands[i])  # Banda izquierda
            reordered_bands.append(bands[V - 1 - i])  # Banda derecha

        # Crear una nueva imagen para las bandas reordenadas
        new_image = Image.new('RGB', (width, height))

        # Pegar las bandas reordenadas en la nueva imagen
        for i, band in enumerate(reordered_bands):
            new_image.paste(band, (i * band_width, 0))

        # Guardar la nueva imagen en el archivo de salida
        new_image.save(output_file)
        print(f"Imagen reordenada y guardada en: {output_file}")

    except Exception as e:
        print(f"Error procesando la imagen: {e}")

def reorder_image_horizontal_bands(input_file, output_file, pixel_ratio):
    try:
        # Abrir la imagen procesada
        original = Image.open(input_file)

        # Obtener las dimensiones de la imagen
        width, height = original.size

        # Calcular el número de bandas horizontales en función de la altura y pixel_ratio
        H = max(2, height // pixel_ratio)

        # Calcular la altura de cada banda
        band_height = height // H

        # Crear una lista para almacenar las bandas
        bands = []

        # Dividir la imagen en H bandas horizontales
        for i in range(H):
            band = original.crop((0, i * band_height, width, (i + 1) * band_height))
            bands.append(band)

        # Reordenar las bandas en el orden 1-H, 2-(H-1), 3-(H-2), ...
        reordered_bands = []
        for i in range(H // 2):
            reordered_bands.append(bands[i])  # Banda superior
            reordered_bands.append(bands[H - 1 - i])  # Banda inferior

        # Crear una nueva imagen para las bandas reordenadas
        new_image = Image.new('RGB', (width, height))

        # Pegar las bandas reordenadas en la nueva imagen
        for i, band in enumerate(reordered_bands):
            new_image.paste(band, (0, i * band_height))

        # Guardar la nueva imagen en el archivo de salida
        new_image.save(output_file)
        print(f"Imagen reordenada horizontalmente y guardada en: {output_file}")

    except Exception as e:
        print(f"Error procesando la imagen: {e}")

if __name__ == "__main__":
    input_file = "C:\\Users\\carlos.quesada\\Documents\\qeii\\paisaje.jpg"
    output_file = "C:\\Users\\carlos.quesada\\Documents\\qeii\\paisaje_out.jpg"
    create_mirrored_image(input_file, output_file)

    # Reordenar las bandas de la imagen salida.jpg
    reordered_output_file = "C:\\Users\\carlos.quesada\\Documents\\qeii\\paisaje_reordenada.jpg"
    pixel_ratio = 50  # Relación de píxeles modificable
    reorder_image_bands(output_file, reordered_output_file, pixel_ratio)

    # Reordenar las bandas horizontales de la imagen reordenada.jpg
    horizontal_reordered_output_file = "C:\\Users\\carlos.quesada\\Documents\\qeii\\paisaje_reordenada_horizontal.jpg"
    reorder_image_horizontal_bands(reordered_output_file, horizontal_reordered_output_file, pixel_ratio)
