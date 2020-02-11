#calculating monthly payment for loan

while True:
    try:
        principal_amount = int(input("Enter the principal amount :"))
        year =int(input("Enter how many year you take to repay :"))
        rate = int(input("Enter the rate of interest :"))
        if principal_amount>0 and year>0 and rate>0:
            break
        else:
            print("Invalid input")
    except:
        print("Invalid details!!")

def monthly_payment(P,Y,R):
    n=12*Y
    r=R/(12*100)
    payment=P*r/(1-(1+r)**(-n))
    print(f"Monthly payment you would have to make is = {payment}")

monthly_payment(principal_amount,year,rate)