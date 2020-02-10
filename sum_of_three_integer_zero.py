#sum of three integer add to zero
terms=int(input("How many terms you want to input:"))
numbers=[]
for i in range(terms):
    number=int(input("Enter number:"))
    numbers.append(number)

def sum_of_integer_zero(numbers,terms):
    count=0
    x=1
    y=2
    for i in range(terms-2):
        for j in range(x,terms-1):
            for k in range(y,terms):
                if numbers[i]+numbers[j]+numbers[k]==0:
                    count+=1
                    print(f"Triplet is ({numbers[i]},{numbers[j]},{numbers[k]})")
            y=y+1
        x=x+1
        y=x+1
    return count
count=sum_of_integer_zero(numbers,terms)
print(f"Total numbner of triplets are :{count}")