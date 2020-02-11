
import prime
prime_number=prime.primes

def prime_palindrom(prime_number):
    palindroms=[]
    for numbers in prime_number:
        ver=0
        ver1=numbers
        while ver1 > 0:
            remainder=ver1%10
            ver= ver*10+remainder
            ver1=ver1//10
        if (ver==numbers):
            palindroms.append(numbers)
    print(f"Palindrom numbers are = {palindroms}")

def prime_anagram(prime_numebr):
    anagrams=[]
    for start0 in range(len(prime_number) - 2):
        for start1 in range(start0+1,len(prime_number)-1):
            num1=str(prime_number[start0])
            num2=str(prime_number[start1])
            if sorted(num1)==sorted(num2):
                anagrams.append(prime_number[start0])
                anagrams.append(prime_number[start1])
    print(f"Anagrams numbers are = {anagrams}")

prime_palindrom(prime_number)
prime_anagram(prime_number)

