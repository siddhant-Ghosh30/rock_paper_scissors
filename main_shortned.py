'''
-1 for rock
1 for paper
0 for scissors

'''
import random
computer = random.choice([0,1,-1])
youstr = input("Enter your choice: ")
youDict = {
    "r" : -1,
    "p" : 1,
    "s" : 0
}
reverseDict = {
    -1 : "rock",
    1 : "paper",
    0 : "scissor"
}

you = youDict[youstr]

# by now we have 2 numbers (variables), you and computer

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]} ")

if(computer == you):
    print("It's a draw")
# else:   # computer - you pattern calculation
#     if(computer == -1 and you ==1): # -2
#         print("you win!!")
#     elif(computer == -1 and you ==0):# -1 
#         print("you lose:(")
#     elif(computer == 1 and you == -1):# 2
#         print("you lose:(")
#     elif(computer == 1 and you == 0):# 1
#         print("you win!!")
#     elif(computer == 0 and you == -1):# 1
#         print("you win!!")
#     elif(computer == 0 and you == 1):# -1
#         print("you lose:(")

    # else:
    #     print("something went wrong")

# the below logic is eritten on the basis of (computer - you)
else:
    if((computer - you) == -1 or (computer - you == 2)):
        print("you lose")
    else:
         print("you win")