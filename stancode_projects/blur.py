"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: img, the old one.
    :return: img, the blurred one.
    """
    old_img = img
    new_img = SimpleImage.blank(old_img.width, old_img.height)

    for x in range(new_img.width):
        for y in range(new_img.height):
            new_img_p = new_img.get_pixel(x, y)
            total_r = 0
            total_g = 0
            total_b = 0
            num = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < new_img.width:
                        if 0 <= y + j < new_img.height:
                            total_r += old_img.get_pixel(x + i, y + j).red
                            total_g += old_img.get_pixel(x + i, y + j).green
                            total_b += old_img.get_pixel(x + i, y + j).blue
                            num += 1
            new_img_p.red = total_r // num
            new_img_p.green = total_g // num
            new_img_p.blue = total_b // num
    return new_img


def main():
    """
    Blur photos.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
