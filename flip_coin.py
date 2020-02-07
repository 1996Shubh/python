import random
number_of_flips=int(input("How many times you want toflip coin:"))

def flip_coin(number_of_flips):
    head=0
    tail=0
    for i in range(number_of_flips):
        num=random.random()
        if num<0.5:
            head+=1
        else:
            tail+=1
    head_percentage=(head/number_of_flips)*100
    tail_percentage=(tail/number_of_flips)*100
    return head_percentage ,tail_percentage

head_percent,tail_percent=flip_coin(number_of_flips)
print(f"Head percent is {head_percent}% and tail percent is {tail_percent}%")