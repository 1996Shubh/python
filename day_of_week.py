
#day_of_week
date=int(input("Enter the date:"))
month=int(input("Enter the month in form of 1-12 :"))
year=int(input("Enter the year :"))
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

def day_of_week(d,m,y,days):
    y0=y-(14-m)//12
    x=y0+(y0//4)-y0//100+y0//400
    m0=m+12*((14-m)//12)-2
    d0=(d+x+(31*m0)//12)%7
    print(f"Day of the week is {days[d0]}")

day_of_week(date,month,year,days)