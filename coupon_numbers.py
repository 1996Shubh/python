
while True:
    try:
        number_of_coupon = int(input("Enter how many distinct coupons want to generate :"))
        if number_of_coupon > 0:
            break
        else:
            print("Invalid input!!")
    except:
        print("Invalid input !!")

def coupon_number(number_of_coupons):
    import random
    coupons=0
    random_numbers=0
    random_nums=[]
    while coupons!=number_of_coupon:
        number=random.randint(1,number_of_coupon)
        random_numbers+=1
        if number not in random_nums:
            random_nums.append(number)
            coupons+=1
    print(f"Total number of random numbers to generate {number_of_coupon} distinct coupons = {random_numbers}")

coupon_number(number_of_coupon)
