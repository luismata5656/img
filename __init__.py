# Import the Images module from pillow
from PIL import Image
import sys

# Get the image name from the command line
img = sys.argv[1]
img_name = img.split(".")[0]

# Create a list of tuples with the sizes
sizes = [(1920,1080),
         (1600,900),
         (1024,1024),
         (1280,720),
         (960,540),
         (64,64),]

# Open the image
im = Image.open(f"{img}")

# Loop through the sizes and save the image
for size in sizes:
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(f"{img_name}_{size[0]}x{size[1]}.png", "PNG")
