from PIL import Image
from PIL import ImageDraw

o_img = Image.open("cat.jpg")
img = o_img.convert('L')

threshold = 20
circle_size = 4

features = []

for i in range(circle_size, img.width - circle_size):
    for j in range(circle_size, img.height - circle_size):
        pixel = img.getpixel((i, j))
        brighter = 0
        darker = 0
        for k in range(1, circle_size):
            if img.getpixel((i+k, j)) - pixel > threshold:
                brighter += 1
            elif pixel - img.getpixel((i+k, j)) > threshold:
                darker += 1
            if img.getpixel((i-k, j)) - pixel > threshold:
                brighter += 1
            elif pixel - img.getpixel((i-k, j)) > threshold:
                darker += 1
            if img.getpixel((i, j+k)) - pixel > threshold:
                brighter += 1
            elif pixel - img.getpixel((i, j+k)) > threshold:
                darker += 1
            if img.getpixel((i, j-k)) - pixel > threshold:
                brighter += 1
            elif pixel - img.getpixel((i, j-k)) > threshold:
                darker += 1
                
        if brighter >= 9 or darker >= 9:
            features.append((i, j))
            
draw = ImageDraw.Draw(o_img)

for feature in features:
    draw.ellipse((feature[0]-3, feature[1]-3, feature[0]+3, feature[1]+3), outline='green')

o_img.show()