x=int(input('enter the x cordinate :'))
y=int(input('enter the y cordinate :'))


def distance_from_origin(x,y):
    distance=(x*x+y*y)**0.5
    return distance

print(f"Distance of ({x},{y}) from origin (0,0) is :{distance_from_origin(x,y)}")

