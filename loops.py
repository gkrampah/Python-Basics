from enum import Enum
import random
import sys
value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break #stops the loop if the condition is met
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else: #it is executed when the loop has completed and the condition of the while loop fails
#     print("Value is now equal to " + str(value))

# names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(2, 4):
#     print(x)


# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Glad that\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:

    playerchoice = input(
        "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! 👋")
