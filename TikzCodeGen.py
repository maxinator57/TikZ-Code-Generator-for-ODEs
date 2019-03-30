import math

def get_ends(x, y, cx, cy, length):
    if cy == 0:
        return [x, y - length * 0.5, x, y + length * 0.5]
    else:
        tan = -cx / cy
        cos = 1 / math.sqrt(tan * tan + 1)
        sin = tan * cos
        return [x - length * 0.5 * cos, y - length * 0.5 * sin, x + length * 0.5 * cos, y + length * 0.5 * sin]
    

def is_defined(f, x, y):
    try:
        res = f(x, y)
    except:
        return False
    return True
        
        
def diff_one_form_field(x1, x2, y1, y2, move_x, move_y, f, g, length, filename, show_undefined_points=True):
    out = open(filename, 'w')
    x = x1
    while abs(x - x2) >= move_x:
        y = y1
        while abs(y - y2) >= move_y:
            cx = f(x, y)
            cy = g(x, y)
            if cx == 0 and cy == 0:
                print('No field at point', x, y)
                if show_undefined_points:
                    out.write('\u005C' + 'filldraw[blue] (' + str(x) + ',' + str(y) + ') circle (2pt);\n')
            else:
                ends = get_ends(x, y, cx, cy, length)
                out.write('\draw[red, thick] (' + str(ends[0]) + ',' +                                                       str(ends[1]) + ') -- (' +                 
                str(ends[2]) + ',' + str(ends[3]) + ');\n')
            y += move_y
        x += move_x
    out.close()
    
    
def diff_eq_field(x1, x2, y1, y2, move_x, move_y, f, length, filename, show_undefined_points=True):
    out = open(filename, 'w')
    x = x1
    while abs(x - x2) >= move_x:
        y = y1
        while abs(y - y2) >= move_y:
            if is_defined(f, x, y):
                der = f(x, y)
                ends = get_ends(x, y, der, -1, length)
                out.write('\draw[red, thick] (' + str(ends[0]) + ',' +                                                       str(ends[1]) + ') -- (' +                 
                str(ends[2]) + ',' + str(ends[3]) + ');\n')
            else:
                if show_undefined_points:
                    out.write('\u005C' + 'filldraw[blue] (' + str(x) + ',' + str(y) + ') circle (2pt);\n')
                print('No field at point', x, y)
            y += move_y
        x += move_x
    out.close()