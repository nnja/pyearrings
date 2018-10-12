import time

import board
import neopixel

pixpin = board.D1
numpix = 21

pixels = neopixel.NeoPixel(pixpin, numpix, brightness=0.5, auto_write=False)

gamma = [
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
    1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
    2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
    5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
    10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
    17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
    25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
    37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
    51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
    69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
    90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 109, 110, 112, 114,
    115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 133, 135, 137, 138, 140, 142,
    144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 167, 169, 171, 173, 175,
    177, 180, 182, 184, 186, 189, 191, 193, 196, 198, 200, 203, 205, 208, 210, 213,
    215, 218, 220, 223, 225, 228, 231, 233, 236, 239, 241, 244, 247, 249, 252, 255]


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - pos * 3), 0, int(pos * 3))

    pos -= 170
    return (0, int(pos * 3), int(255 - pos * 3))


while True:

    for marker in range(11, 0, -1):
        for x in range(0, marker+1):

            mult_r = x / 12
            mult_g = (x + 5) / 12
            mult_b = (x + 10) / 12

            r = gamma[wheel(int((x / 12) * 150))[0]]
            g = gamma[wheel(int((x / 12) * 150))[1]]
            b = gamma[wheel(int((x / 12) * 150))[2]]
            pixels[x] = (r, g, b)

            r = gamma[wheel(int((x-1 / 12) * 150))[0]]
            g = gamma[wheel(int((x-1 / 12) * 150))[1]]
            b = gamma[wheel(int((x-1 / 12) * 150))[2]]
            pixels[x-1] = (r, g, b)

            pixels.write()
            time.sleep(0.05)

    for x in range(12, -1, -1):
        time.sleep(0.05)
        pixels[x] = (0, 0, 0)
        pixels.write()

    for i in range(0, 255, 100):
        for x in range(12, numpix):
            pixels[x] = (gamma[i], gamma[i], gamma[i])
            pixels.write()

    for i in range(255, 0, -30):
        for x in range(12, numpix):
            pixels[x] = (gamma[i], gamma[i], gamma[i])
        pixels.write()

    pixels.write()
    time.sleep(1)
