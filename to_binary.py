#decimal to binary
while True:
    try:
        number=int(input("Enter a number :"))
        if number>=0:
            break
        print("Invalid input")
    except:
        print("Invalid input")

def decimal_to_binary(number):
    for num in range(31,-1,-1):
        binary_number=number >> num
        if(binary_number &1):
            print("1",end="")
        else:
            print("0",end="")

decimal_to_binary(number)
