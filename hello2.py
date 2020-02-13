print("Enter 1 for celcius to Fahrenheit conversion !")
print("Enter 2 for Fahrenheit to celcius conversion !")
x=int(input("Enter your choice:"))

def conversion_of_temperature(choice):
    if choice==1:
        temp=int(input("Enter the temperature in celcius:"))
        celcius_to_fehrenheit=(temp_cel*9/5)+32
        print(f"Tempreture in {temp}celsius")
    elif choice==2:
        temp = int(input("enter the temp in fehranite"))
        f_to_celcius=(temp-32)*5/9
        print(f{temp}fera={f_to_celcius}celcius ")
    else:
        print("You entered wrong choice!!")

conversion_of_temperature(x)
