
from PIL import Image

# Blending two images:

img1 = Image.open("car1.jfif")
img2 =  Image.open("car2.jfif")
# Resize img2 to match img1's size
img2 = img2.resize(img1.size)
img = Image.blend(img1 , img2 , alpha= 0.5)
img.show()




# Pasting an image onto another:

# Open images
image1 = Image.open("car1.jfif").convert("RGBA")
image2 = Image.open("car2.jfif").convert("RGBA")

# Resize image2
image2 = image2.resize((100, 100))

# Paste image2 onto image1
image1.paste(image2, (20, 20))

# Show the result
image1.show()

