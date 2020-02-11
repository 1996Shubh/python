#prime number between a range

while True:
    try:
        starting_range=int(input("Enter the starting range :"))
        end_range=int(input("Enter the end of range :"))
        if starting_range>=0 and end_range>=0:
            break
        print("Invalid input! Enter positive range  ")
    except:
        print("Invalid input ")

def prime_in_range(start,end):
    prime_numbers=[]
    for number in range(start,end+1):
        if number==0 or number==1:
            continue
        temp=0
        for number2 in range(2,number//2):
            if number%number2==0:
                temp=1
                break
        if(temp==0):
            prime_numbers.append(number)
    print(f"prime numbers in range of {start}-{end} = {prime_numbers}")

prime_in_range(starting_range,end_range)