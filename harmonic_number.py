terms=int(input("Enter upto how many terms you want to print:"))

def harmonic_number(terms):
    value=0
    for i in range(1,terms+1):
        print(f"1/{i}",end="+")
        value+=1/i
    print("")
    print(value)

harmonic_number(terms)