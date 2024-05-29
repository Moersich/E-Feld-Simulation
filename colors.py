from pygame.color import Color

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RED_APPEND = (255, 100, 100)

def __hue_to_rgb_value(p: float, q: float, t: float) -> float:
    if t < 0:
        t += 1
    if t > 1:
        t -= 1
    if t < 1/6:
        return p + (q - p) * 6 * t
    if t < 1/2:
        return q
    if t < 2/3:
        return p + (q - p) * (2/3 - t) * 6
    return p

def hsl_to_rgb(h: float, s: float, l: float) -> Color:
    if s == 0:
        r = g = b = l
    else:
        if l < 0.5:
            q = l * (1 + s)
        else:
            q = l + s - l * s
        p = 2 * l - q
        r = __hue_to_rgb_value(p, q, h + 1/3)
        g = __hue_to_rgb_value(p, q, h)
        b = __hue_to_rgb_value(p, q, h - 1/3)

    return Color(round(r * 255), round(g * 255), round(b * 255))