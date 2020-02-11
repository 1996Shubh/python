#Square root by newton's method

import math
while True:
    try:
        c = int(input("Enter a nonnegative number:"))
        if c>=0:
            break
        else:
            print("You entered negative number !!")
    except:
        print("Invalid input!! please enter a nonnegative numebr:")


def square_root(c):
    e=pow(10,-15)
    t=c
    if(c==0):
        print(0)
    else:
        while abs(t - c / t) > (e * t):
            t = ((c / t) + t) / 2
        print(f"Squre root of {c}={round(t,4)}")

square_root(c)