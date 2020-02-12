string=input("Enter a string :")
string_list=string.split(" ")

def insertion_sort(string_list):
    for word in range(1,len(string_list)):
        temp=string_list[word]
        next_word=word-1
        while next_word>=0 and temp<string_list[next_word]:
            string_list[next_word+1]=string_list[next_word]
            next_word-=1
        string_list[next_word+1]=temp
    print(string_list)

insertion_sort(string_list)
