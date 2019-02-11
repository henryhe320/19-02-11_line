f = open('pic.ppm','w')
pixels = []

#makes 500 by 500 black
for row in range(500):
    rowList = []
    for col in range(500):
        rowList.append('0 0 0 ')
    pixels.append(rowList)

#make a line

def plot(x,y):
    pixels[y][x] = '255 255 255 '

def line(xa, ya, xb, yb):
    if xa < xb:
        x = xa
        y = ya
    else:
        x = xb
        y = yb
        xb = xa
        yb = ya
    A = yb - y
    B = -(xb - x)
    d = 2*A + B
    if -A/B > 0:
        if -A/B <= 1: #Octant I
            while x <= xb:
                if y > yb: break
                plot(x,y)
                if d > 0:
                    y += 1
                    d += 2*B
                x += 1
                d += 2*A
        else: #Octant II
            while y <= yb:
                if x > xb: break
                plot(x,y)
                if d < 0:
                    x += 1
                    d += 2*A
                y += 1
                d += 2*B
    else:
        if -A/B <= -1: #Octant III
            while y >= yb:
                if x > xb: break
                plot(x,y)
                if d < 0:
                    x += 1
                    d -= 2*A
                y -= 1
                d += 2*B
            
        else: #Octanc IV
            while x <= xb:
                if y < yb: break
                plot(x,y)
                if d > 0:
                    y -= 1
                    d += 2*B
                x += 1
                d -= 2*A
            

line(0,0,499,250)
line(0,0,250,499)
line(499,0,0,250)
line(499,0,250,499)

#putting list into ppm
final = 'P3 500 500 255 '
for row in pixels:
    for col in row:
        final += col

f.write(final)