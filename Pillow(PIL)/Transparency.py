
# Pillow supports transparency in images that use an alpha channel (such as PNG images).
# You can manipulate the transparency of an image or blend multiple images together.


# Convert an image to have transparency (RGBA):

from PIL import Image
image =Image.open("car1.jfif")
rgba_image = image.convert("RGBA")   # for transparency
rgba_image.show()

# Change the transparency of the image:


rgba_image.putalpha(128)  # Set opacity to 50% (128 out of 255)
rgba_image.show()