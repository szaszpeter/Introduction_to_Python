from PIL import Image
from PIL import ImageFilter

#Open a simple image
img_king = Image.open("king.png")

# Print some basic details
print(img_king.size)
print(img_king.format)


# Crop out a portion of an image
area = (400, 100, 700, 375)
cropped_king = img_king.crop(area)

# Paste in a piece of cropped image into another one
img_me = Image.open("me.jpg")
img_me.paste(cropped_king, area)
# img_me.show()

# Break up image in three individual channels
img_bike = Image.open("bike.png")
print(img_bike.mode)
r,g,b,a = img_bike.split()
# r.show()

# Merge image channels into a new image
img_bike_new = Image.merge("RGB", (g,r,b))
# img_bike_new.show()

# Resize image into square size
square_img_bike_new = img_bike_new.resize((250,250))
# square_img_bike_new.show()

# Flip image
flipped_img_bike_new = square_img_bike_new.transpose(Image.FLIP_LEFT_RIGHT)
# flipped_img_bike_new.show()

# Rotate image
spinned_img_bike_new = flipped_img_bike_new.transpose(Image.ROTATE_90)
# spinned_img_bike_new.show()

# Convert image to black an white
black_and_white_king = cropped_king.convert("L")
# black_white_me.show()

# Blur image
blur = black_and_white_king.filter(ImageFilter.BLUR)
# blur.show()

# Sharpen image
detail = black_and_white_king.filter(ImageFilter.DETAIL)
# detail.show()

# Edges effect
edges = black_and_white_king.filter(ImageFilter.FIND_EDGES)
edges.show()

