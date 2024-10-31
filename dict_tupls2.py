stocks = {
    "info": [600,630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}


def print_all():
    average_value = 0
    for key, value in stocks.items():
        for item in value:
            average_value += item
        mit = round(average_value/len(value), 2)
        print(f"{key}==> {value}==>{mit}")
        average_value = 0
    
print_all()

def add():
    s = input("Enter a stock ticker to add:")
    p = input("Enter price of this stock:")
    p=float(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    print_all()


def main():
    op=input("Enter operation (print, add or amend):")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print("Unsupported operation:",op)

import math
def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter
if __name__ == '__main__':
    main()
    r = input('Enter a radius:')
    r=float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")