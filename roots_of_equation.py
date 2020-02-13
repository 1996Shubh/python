def roots_of_equation(a,b,c):
    delta=b*b-4*a*c
    if delta>=0:
        root1=round((-b+(delta**0.5))/(2*a),4)
        root2=round((-b-(delta**0.5))/(2*a),4)
        print(f"root1={root1}")
        print(f"root2={root2}")

    else:
        print(f"root1=({-b}+{round((-1*delta)**0.5,4)}i)/{2*a}")
        print(f"root2=({-b}-{round((-1*delta)**0.5,4)}i)/{2*a}")

while(True):
    try:
        a=int(input("enter the value of a in a*x*x+b*x+c:"))
        b=int(input("enter the value of b in a*x*x+b*x+c:"))
        c=int(input("enter the value of c in a*x*x+b*x+c:"))
        break
    except ValueError:
        print("Please enter valid input")

roots_of_equation(a,b,c)



