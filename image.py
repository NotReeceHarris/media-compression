from PIL import Image
import os

def get_image_size(image_path):
    try:
        # Get the size of the image file in bytes
        size_in_bytes = os.path.getsize(image_path)

        # Convert bytes to kilobytes
        size_in_kb = size_in_bytes / 1024

        return size_in_kb
    except FileNotFoundError:
        print(f"Error: File not found - {image_path}")
        return None

def process_image(image_path):
    img = Image.open(image_path)
    img.save('compressed.jpg', optimize = True, quality = 25)

    start_size = get_image_size('example.jpg')
    compressed_size = get_image_size('compressed.jpg')

    print('\nStarter image:', round(start_size, 2), 'KB')
    print('Compressed image:', round(compressed_size, 2), 'KB')

    print('Image size reduced by:', round((start_size - compressed_size), 2), 'KB')
    print('Percent of original size:', round((compressed_size / start_size * 100), 2), '%')

image_path = 'example.jpg'
process_image(image_path)