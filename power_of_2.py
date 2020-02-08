power=int(input("Enter how many power you want to print :"))

def power_of_2(max_power):
    for i in range(max_power+1):
        print(f"2^{i}={2**i}")

power_of_2(power)
