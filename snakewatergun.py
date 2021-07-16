import random
swg = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
print("Snake,Water,Gun Game \n")
print("s for snake \nw for water \ng for gun \n")
#making the game while
while no_of_chance < chance:
    input1 = input("Snake, Water, Gun : ")
    random1 = random.choice(swg)
    if input1 == random1:
        print(" OOPS Match Draw!\n ")

    elif input1=="s" and random1=="g":
        computer_point =computer_point + 1
        print(f"your guess {input1} and computer guess is {random1} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")


    elif input1=="s" and random1=="w":
        human_point =  human_point + 1
        print(f"your guess {input1} and computer guess is {random1} \n")
        print("you wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif input1=="w" and random1 == "s":
        computer_point = computer_point + 1
        print(f"your guess {input1} and computer guess is {random1} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif input1=="w" and random1 == "g":
        human_point = human_point + 1
        print(f"your guess {input1} and computer guess is {random1} \n")
        print("you wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif input1=="g" and random1=="w":
        computer_point = computer_point + 1
        print(f"your guess {input1} and computer guess is {random1} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif input1=="g" and random1=="s":
        human_point = human_point + 1
        print(f"your guess {input1} and computer guess is {random1} \n")
        print("you wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("Please enter the correct input")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}\n")


print("Game Over")

if computer_point == human_point:
    print("Match Draw")

elif computer_point > human_point:
    print("Computer Wins the game!!!")

else:
    print("You win!!!")

print(f"your point is {human_point} and computer point is {computer_point}")




