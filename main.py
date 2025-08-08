import random
'''
1 = snake
-1 = water
0 = gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice : ")
youDict={"s" : 1 , "w" : -1, "g" : 0}
reversedict= {1:"snake", -1: "water", 0 : "gun"}
you = youDict[youstr]

print(f"computer choose {reversedict[computer]}\n*you choose {reversedict[you]}")

if computer == you:
    print("its a draw")
else:
    if(computer == -1 and you == 1):
        print("you Win")
    
    elif(computer == -1 and you == 0):
        print("you Lose")
    
    elif(computer == 1 and you == -1):
        print("you Lose")
    
    elif(computer == 1 and you == 0):
        print("you Win")
    
    elif(computer == 0 and you == 1):
        print("you Lose")
    
    elif(computer == 0 and you == -1):
        print("you Win")
    
    else:
        print("something went wrong")
    
