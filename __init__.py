# Import the Images module from pillow
from PIL import Image

img_name = input("Enter file name: ")
img_ext = input("Enter file extension: ")

sizes = [(1920,1080),
         (1600,900),
         (1280,720),
         (960,540),
         (64,64),]
im = Image.open(f"{img_name}.{img_ext}")

for size in sizes:
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(f"{img_name}_{size[0]}x{size[1]}.png", "PNG")