from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pyqrcode
import string
import random
from flask import url_for
allchar = string.ascii_letters + string.digits
min_char = 8
max_char = 12


def pass_gen(name, email):
    img = Image.open("app/static/passes/pass.jpeg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("app/static/Quicksand_Bold.otf", 32)
    s = "".join(random.choice(allchar)
                for x in range(random.randint(min_char, max_char)))
    s_path = "app/static/passes/" + s + ".png"
    if len(name) >= 18:
        name = name.split()
        name = name[0] + " " + name[1][0]
    seat = str(random.randint(1, 99)) + \
        random.choice(string.ascii_letters).upper()
    draw.text((8, 250), name.upper(), (0, 0, 0), font=font)
    draw.text((397, 250), seat, (0, 0, 0), font=font)
    s1 = "Name:{0}\nEmail: {1}\nRoom: B-215\nReach us: http://bit.ly/makebot\n".format(
        name, email)
    dat = pyqrcode.create(s1)
    tp = "app/static/passes/qr_"+s
    dat.png(tp, scale=2)
    img1 = Image.open(tp)
    img.paste(img1, (350, 292))
    img.save(s_path)
    return s+".png"
