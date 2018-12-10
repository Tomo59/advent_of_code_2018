#/usr/bin/env python3

def get_area(points):
    x_min = min(points, key=lambda p: p[0][0])[0][0]
    x_max = max(points, key=lambda p: p[0][0])[0][0]
    y_min = min(points, key=lambda p: p[0][1])[0][1]
    y_max = max(points, key=lambda p: p[0][1])[0][1]
    return (x_max-x_min)*(y_max-y_min)

def move_points(points):
    return [((x+vx,y+vy),(vx,vy))for ((x,y),(vx,vy)) in points]

def p1and2(points):
    area = get_area(points)
    last_area = area + 1
    seconds = 0
    while last_area > area:
        points = move_points(points)
        last_area = area
        area = get_area(points)
        seconds += 1
    x_min = min(points, key=lambda p: p[0][0])[0][0]
    x_max = max(points, key=lambda p: p[0][0])[0][0]
    y_min = min(points, key=lambda p: p[0][1])[0][1]
    y_max = max(points, key=lambda p: p[0][1])[0][1]
    # shift back points to previous position and keep only points themselves
    points = [(x-vx,y-vy) for ((x,y),(vx,vy)) in points]
    seconds -= 1
    for y in range(y_min, y_max+1):
        line = ""
        for x in range(x_min, x_max+1):
            if (x,y) in points:
                line += '#'
            else:
                line += '.'
        print(line)
    return seconds

if __name__ == "__main__":
    f = open('input.txt', 'r')
    points=[((int(l[10:16]),int(l[18:24])),(int(l[36:38]),int(l[40:42])))for l in f.readlines()]
    print("part1:")
    print("part2: {}".format(p1and2(points)))
