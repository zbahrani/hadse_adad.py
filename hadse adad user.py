import random
goal = random.randint(1, 100)
user_num = int(input("enter your number(1, 100): "))
user_name = input("enter your name: ")
while goal != user_num:
    if goal > user_num :
        print("your number is small ")
        user_num = int(input("enter your number: "))
    elif goal < user_num :
        print("your number is large")
        user_num = int(input("enter your number: "))
print("woooowww, you did it ")


