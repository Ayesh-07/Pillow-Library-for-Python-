
#  Documentation : https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.rotate

# Installation

from PIL import Image


# Opening and Displaying an Image


# Open the image

file_name = "car.jpg"
img = Image.open(file_name)

#print(img)

# Show the image
Image._show(img)


#------------------------------------------------

# Getting Image Information

print(img.format)  # Output the image format (JPEG, PNG, etc.)
print(img.size)    # Output the image size (width, height)
print(img.mode)    # Output the color mode (RGB, L, etc.)



# --------------------------------------------

# make new Image

img = Image.new("RGB" ,(400 , 600 ) , (255, 0, 0) )
Image._show(img)


#--------------------------------------------------

# Image rotation and its Parameters

file = "car.jpg"
img1 = Image.open(file)
# img1 = img1.rotate(angle=90 , expand=True)
img1 = img1.rotate(angle=60 , expand=True , fillcolor="blue")
img1 = img1.rotate(angle=60 , expand=True , fillcolor="blue" , center=(100 ,89)) 
img1.show(img1)


# ---------------------------------------------------

# #  resize an image 
file = "car.jpg"
img = Image.open(file)

# Get the original width and height
w_h = img.width, img.height
print(w_h)

# Resize the image to half its original size
new_size = (img.width // 2, img.height // 2)  # Ensure the dimensions are integers
img_resized = img.resize(new_size)  # Resize the image

# Show the resized image
img_resized.show()


# ---------------------------------------------------------


 # crop an image 
 
img1 = Image.open("car1.jfif")
img = img1.crop((20, 20, 200, 200))
img.show()