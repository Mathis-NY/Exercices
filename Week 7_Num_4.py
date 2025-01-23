import sys
from PIL import Image, ImageOps

if len(sys.argv)== 3:
    try:
        user_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('File does not exit')

    shirt = Image.open("shirt.png")
    taille = shirt.size
    user_image = ImageOps.fit(user_image, taille)
    user_image.paste(shirt, shirt)
    user_image.save(sys.argv[2])

elif len(sys.argv) > 3:
    sys.exit ("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit ("Too fee command-line arguments")
