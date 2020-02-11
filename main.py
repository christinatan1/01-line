from display import *
from draw import *
import random

s = new_screen()
c = [ 0, 255, 0 ]

for x in range(500):
    if x % 25 == 0 or x % 30 == 0:
        c[RED] = random.randint(150, 250)
        c[GREEN] = random.randint(0, 200)
        c[BLUE] = random.randint(210, 255)
        y = random.randint(25, 420)
        draw_line(x, 500, x, y, s, c)
        #draw star
        c[RED] = 255;
        c[GREEN] = 255;
        c[BLUE] = 0;
        draw_line(x, (y-4), x, (y+10), s, c)
        draw_line((x-5), (y+5), (x+5), y, s, c)
        draw_line((x-5), y, (x+5), (y+5), s, c)

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c)
# draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)
#
# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);
#
# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);
#
# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);
#
# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
# draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
print("image created: img.png")
