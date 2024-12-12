import os
import qrcode

img = qrcode.make("https://www.instagram.com/nathankx01/")

img.save("instagramqrcode.png", "PNG")

os.system("xdg-open instagramqrcode.png")