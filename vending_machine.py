#vending machine problem
changing_amount=int(input("Enter the amount returned by Vanding machine :"))
avilable_notes=[1000,500,100,50,10,5,2,1]

def vending_machine(avilable_notes,changing_amount):
    i=0
    total_notes=0
    while changing_amount>0:
        notes=changing_amount//avilable_notes[i]
        if(notes>0):
            print(f"{notes} notes of {avilable_notes[i]} rupess")
            changing_amount=changing_amount%avilable_notes[i]
            total_notes+=notes
        i+=1
    return total_notes

print(f"Total number of notes ={vending_machine(avilable_notes,changing_amount)}")
