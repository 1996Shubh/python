
print("Temperature should be less then 50F and wind speed is between (3,120)miles per hour")
temperature=int(input("Enter the temperature in fahrenheit :"))
wind_speed=int(input("Enter the wind speed in miles per hour :"))

while temperature>50 or wind_speed>120 or wind_speed<3:
    print("Temperature should be less then 50F and wind speed is between (3,120)miles per hour")
    temperature = int(input("Enter the temperature in fahrenheit :"))
    wind_speed = int(input("Enter the wind speed in miles per hour :"))

def wind_chill(temp,speed):
    return round(35.74+0.6215*temp+(0.4275*temp-35.75)*(wind_speed**0.16),4)

print(f"wind_chill={wind_chill(temperature,wind_speed)}")
