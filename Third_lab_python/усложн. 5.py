from PIL import Image, ImageDraw
import os
from random import randint


def random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def circles_generator(num_of_circles=100):
    radius = 300
    output_dir = "circles"
    try:
        os.mkdir(output_dir)
    except OSError:
        print('Папка "circles" уже существует')

    for i in range(num_of_circles):
        image = Image.new('RGB', (2 * radius, 2 * radius), "white")
        draw = ImageDraw.Draw(image)
        color = random_color()

        draw.ellipse((0, 0, 2 * radius, 2 * radius), fill=color)

        filename = f"{output_dir}/circle_{i + 1}.jpg"
        image.save(filename, "JPEG")

circles_generator()