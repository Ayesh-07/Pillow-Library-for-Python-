# Drawing on Images
# Pillow also allows you to draw shapes and text on images using the ImageDraw module.


from PIL import Image
from PIL import ImageDraw, ImageFont

# Draw a rectangle:

image = Image.open("car.jpg")
draw = ImageDraw.Draw(image)
draw.rectangle([(50, 50), (150, 150)], outline="red", width=5)
image.show()


# Draw a circle:

image = Image.open("car.jpg")
draw = ImageDraw.Draw(image)
draw.ellipse([(20, 20), (150, 150)], outline="yellow", width=9)
image.show()


# Add text to an image:

image = Image.open("car.jpg")
draw = ImageDraw.Draw(image)

# Load a font (optional)
font = ImageFont.truetype("arial.ttf", 36)  # You can specify font size

#font = None   # Use defult font

# Add text at position (x, y)
draw.text((20 ,20) , "Design By Ayesh" , fill="white", font=font)
image.show()

