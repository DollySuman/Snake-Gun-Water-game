'''
1 for snake
-1 for water
0 for gun
'''

import random
n = [1,-1,0]

computer = random.choice(n)
youstr = input("Enter your choice: ")
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1:"Snake", -1:"Water", 0:"Gun"}


you = youdict[youstr]
print(f"Computer chose {reversedict[computer]}")

if(computer == you):
    print("Hey it is a draw")

else:
    if(computer == -1 and you ==1):
        print("You win!")

    elif(computer == -1 and you ==0):
        print("You Lose!")

    elif(computer == 1 and you ==-1):
        print("You lose!")

    elif(computer == 1 and you ==0):
        print("You win!")

    elif(computer == 0 and you ==-1):
        print("You win!")

    elif(computer == 0 and you ==1):
        print("You Lose!")
    else:
        print("Something went wrong")



