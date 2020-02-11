#anagram program
string1=input("Enter first string :")
string2=input("Enter second string:")


def check_anagram(string1,string2):
    if sorted(string1)==sorted(string2):
        print("Strings are anagram")
    else:
        print("Strings are not anagram")

check_anagram(string1,string2)
