# run pip install pillow to install
from PIL import Image


def main():
    # Open image
    image = Image.open('jump.jpeg')
    # Show image
    image.show()

    # get the height and width
    width, height = image.size
    new_image = Image.new("RGB", (image.size), "white")

    alt_formula = input("Which filter?: ")

    if alt_formula == "grayscale":
        gray_scale(new_image, width, height, image)
    if alt_formula == "rgbscale":
        rgb_scale(new_image, width, height, image)

    new_image.show()

def rgb_scale(new_image, width, height, image):
    for x in range(width):
        for y in range(height):
            r, b, g = image.getpixel((x, y))
            new_image.putpixel((x, y), (r, b, g))
    return new_image

def gray_scale(new_image, width, height, image):
    for x in range(width):
        for y in range(height):
            r, b, g = image.getpixel((x, y))
            grey = (r + b + g)/3
            new_image.putpixel((x, y), (grey))
    return new_image

if __name__ == "__main__":
    main()