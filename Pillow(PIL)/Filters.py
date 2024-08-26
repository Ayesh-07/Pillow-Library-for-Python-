# 1. Applying Filters
# You can apply various filters like blurring, contouring, and more using the ImageFilter module.


from PIL import Image
from PIL import ImageFilter


# Blur Filter:

image = Image.open("car1.jfif")
blur_image = image.filter(ImageFilter.BLUR)
blur_image.show()

# Sharpen Filter:

image = Image.open("car1.jfif")
blur_image = image.filter(ImageFilter.SHARPEN)
blur_image.show()

# Edge Enhance Filter:

image = Image.open("car1.jfif")
blur_image = image.filter(ImageFilter.EDGE_ENHANCE)
blur_image.show()


