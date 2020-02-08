user_name=input("enter your name:")
while len(user_name)<3:
    print("Name should have min three character")
    user_name=input("enter your name:")

print(f"Hello {user_name},how are you?")