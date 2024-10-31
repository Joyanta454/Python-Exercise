def rectangle_area(base, height):
    result =base*height
    return result

print('Rectangle Area',rectangle_area(10,12))

def triangle_area(base, height):
    result = 0.5*base*height
    return result

print('Triangle Area',triangle_area(10,12))

def print_pattern(n):
    for i in range(n+1):
        for j in range(i):
            print("*", end='')
        print()

print_pattern(4)

