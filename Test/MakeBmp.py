#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

from PIL import Image
import numpy as np

SIZE = 10
W, H = SIZE, SIZE
data1 = np.full((H, W, 3), 255, dtype=np.uint8)
data2 = np.full((H, W, 3), 255, dtype=np.uint8)

v = np.linspace(0, 255, SIZE, dtype=np.uint8)

color = [0] * 3
color[0] = 0
color[1] = 100
color[2] = 200

for w in range(W):
    for h in range(H):
        # deixa branco
        for i in range(3):
            color[i] = color[i] % 256
            data1[w][h][i] = color[i]
            colorDiff = color[i] - i - 1
            data2[w][h][i] = colorDiff if colorDiff >= 0 else 0
        color[0] += 1
        color[1] += 2
        color[2] += 3



img = Image.fromarray(data1, 'RGB')
img.save('test1.bmp')

img = Image.fromarray(data2, 'RGB')
img.save('test2.bmp')