# Import the Images module from pillow
from PIL import Image
import sys

img = sys.argv[1]
img_name = img.split(".")[0]

sizes = [(1920,1080),
         (1600,900),
         (1280,720),
         (960,540),
         (64,64),]
im = Image.open(f"{img}")

for size in sizes:
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(f"{img_name}_{size[0]}x{size[1]}.png", "PNG")