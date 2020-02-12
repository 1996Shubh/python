
while True:
    try:
        total_numbers = int(input("Enter how many numbers you want to insert in to the list:"))
        if total_numbers>0:
            break
        print("invalid input!!")
    except:
        print("Invalid input!!")
numbers_list=[]
while True:
    try:
        for i in range(total_numbers):
            numbers_list.append(int(input("Enter number:")))
        break
    except:
        print("Invalid input!!please enter only numbers ")

def bubble_sort(numbers_list):
    for number in range(len(numbers_list)-1):
        for next in range(number+1,len(numbers_list)):
            if numbers_list[next]<numbers_list[number]:
                temp=numbers_list[number]
                numbers_list[number]=numbers_list[next]
                numbers_list[next]=temp
    print(f"Sorted list ={numbers_list}")

bubble_sort(numbers_list)
