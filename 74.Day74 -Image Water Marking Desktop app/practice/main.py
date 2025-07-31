
from PIL import Image, ImageDraw, ImageFont , ImageFilter


# # Used for Viewing size,mode,format of the image
# # print(im.format, im.size, im.mode)


# # CROPING THE IMAGE
# # box = (0, 50, 164, 74)
# # box = (left,upper,right,lower)
# # region = im.crop(box)
# # region.show()


# # Splitting and merging bands
# # r, g, b = im.split()
# # im = Image.merge("RGB", (b, r, g))


# # GEOMETRICAL TRANSFORMS

# # out = im.resize((128, 128))
# # out = im.rotate(45)
# # out.show()

# # draw.line(((0, 100), (200, 100)), "gray")
# # draw.line(((100, 0), (100, 200)), "gray")

# # Create a blank white image
# image = Image.open(r"C:\Users\siddi\OneDrive\Pictures\Saved Pictures\Image 2024-09-16 at 20.57.30_b6e92c18.jpg")

# # Load font

# # Create a drawing object
# draw = ImageDraw.Draw(image)
# # Draw horizontal and vertical lines
# font = ImageFont.truetype("arial.ttf", 15)  # Size = 60 (you can increase it more)

# # Draw centered text
# draw.text((70, 315), "MAAZ SIDDIQUI", fill="gray", anchor="ms", font=font)

# # Show the image
# image.show()


im = Image.open("car.jpg")


text_img = Image.new("RGBA", (300, 100), (0, 0, 0, 0))

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 25)

# Define the text
text = "MAAZ SIDDIQUI"

    
im.show()