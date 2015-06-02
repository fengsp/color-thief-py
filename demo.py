# -*- coding: utf-8 -*-
from urllib.request import urlopen
import io

from colorthief import ColorThief


fd = urlopen('http://lokeshdhakar.com/projects/color-thief/img/photo1.jpg')
f = io.BytesIO(fd.read())
color_thief = ColorThief(f)
print(color_thief.get_color(quality=1))
print(color_thief.get_palette(quality=1))
