data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))


def find_pixels(x, y, d, w):
    end_x = abs(x) + abs(d)
    end_y = abs(y) + abs(w)
    coord = []
    for i in range(y, end_y + 1):
        for j in range(x, end_x + 1):
            coord.append((i, j))
    return coord
        
    
x1 = data1[0]
y1 = data1[1]
d1 = data1[2]
w1 = data1[3]
x2 = data2[0]
y2 = data2[1]
d2 = data2[2]
w2 = data2[3]
mass1 = set(find_pixels(x1, y1, d1, w1))
mass2 = set(find_pixels(x2, y2, d2, w2))
if len(mass1 & mass2) >= 1:
    print('YES')
else:
    print('NO')
