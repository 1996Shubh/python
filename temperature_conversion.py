#temoerature conversion

print("Enter 1 for Celcius to Fahrenheit conversion !")
print("Enter 2 for Fahrenheit to Celcius conversion !")
while True:
    try:
        choice=int(input("Enter your choice:"))
        temp = int(input("Enter the temperature:"))
        if choice==1 or choice==2:
            break;
        print("wrong choice!! choice should be 1 or 2")
    except:
        print("invalid input!! choice should be 1 or 2 and temperature should be a number !")

def conversion_of_temperature(choice,temp):
    if choice==1:
        celcius_to_fehrenheit=round((temp*9/5)+32,4)
        print(f"Temperature {temp}C ={celcius_to_fehrenheit}F ")
    elif choice==2:
        fahrenheit_to_celcius=round((temp-32)*5/9,4)
        print(f"Temperature {temp}F ={fahrenheit_to_celcius}C")

conversion_of_temperature(choice,temp)