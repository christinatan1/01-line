from display import *

def draw_line(x0, y0, x1, y1, screen, color):

    if x0 > x1:
        x0, x1 = x1, y0
        y0, y1 = y1, y0

    dx = -1 * (x1 - x0)
    dy = y1 - y0

    # #vertical line
    # if x0 == x1:
    #     if y0 < y1:
    #         while y0 < y1:
    #             plot(screen, color, int(x0), int(y0))
    #             y0 += 1
    #         if y0 > y1:
    #             while y0 > y1:
    #                 plot(screen, color, int(x0), int(y0))
    #                 y0 -= 1
    #
    # #horizontal lines
    # if y0 == y1:
    #     if x0 < x1:
    #         while x0 > x1:
    #             plot(screen, color, int(x0), int(y0))
    #             x += 1
    #     if x0 > x1:
    #         while x0 > x1:
    #             plot(screen, color, int(x0), int(y0))
    #             x -= 1


    if x0 < x1:
        m = -1 * float(dy) / float(dx)
        # 1st and 5th
        if m >= 0 and m <= 1:
                d = 2 * dy + dx
                while x0 <= x1:
                    plot(screen, color, int(x0), int(y0))
                    if d > 0:
                        y0 += 1
                        d += 2 * dx
                    x0 += 1
                    d += 2 * dy

        # 2nd and 6th
        elif m > 1:
            d = dy + 2 * dx
            while y0 <= y1:
                plot(screen, color, int(x0), int(y0))
                if d < 0:
                    x0 += 1
                    d += 2 * dy
                y0 += 1
                d += 2 * dx

        # 3rd and 7th
        elif m <= 0 and m <= -1:
                d = dy - (2 * dx)
                while y0 >= y1:
                    plot(screen, color, int(x0), int(y0))
                    if d > 0:
                        x0 += 1
                        d += 2 * dy
                    y0 -= 1
                    d -= 2 * dx

        # 4th and 8th
        elif m <= 0 and m >= -1:
                d = 2 * dy + dx
                while x0 <= x1:
                    plot(screen, color, int(x0), int(y0))
                    if d < 0:
                        y0 -= 1
                        d -= 2 * dx
                    x0 += 1
                    d += 2 * dy
    else:
        if y0 < y1:
            while y0 < y1:
                plot(screen, color, int(x0), int(y0))
                y0 += 1
        else:
            while y0 > y1:
                plot(screen, color, int(x0), int(y0))
                y0 -= 1
