# Image Enhancements
# Pillow also allows you to enhance the image’s brightness, contrast, sharpness, 
# and color using the ImageEnhance module.

from PIL import Image
from PIL import ImageEnhance

# Brightness Adjustment:

image = Image.open("car2.jfif")
enhancer = ImageEnhance.Brightness(image)
brighter_image = enhancer.enhance(1.5)  # Increase brightness by 1.5x
brighter_image.show()



# Contrast Adjustment:

image = Image.open("car2.jfif")
enhancer = ImageEnhance.Contrast(image)
contrast_image = enhancer.enhance(2)  # Increase contrast by 2
contrast_image.show()


#  Sharpness Adjustment:

image = Image.open("car2.jfif")
enhancer = ImageEnhance.Sharpness(image)
Sharpness_image = enhancer.enhance(3)  # Increase Sharpness by 3
Sharpness_image.show() 
