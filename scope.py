from enum import Enum
import random
import sys
name = "Kwesi"  # global scope

# global scope variable and functions can be accessed from a local scope and not vice versa


# def greeting(name):
#     color = "red"  # local scope
#     print(color)
#     print(name)


# greeting(name)
# greeting("Isaac")
# print(color) #cant access local scope variable


# def another():
#     greeting(name)

# another()


# def another():
#     color = "blue"
#     #this done to stop polluting the global scope
#     def greeting(name):

#         print(color)
#         print(name)

#     greeting("Dave")


# another()

# count = 1


# def another():
#     color = "blue"
#     global count
#     count += 1
#     print(count)
#     print(color)

#     def greeting(name):
#         nonlocal color
#         color = "red"
#         print(color)
#         print(name)

#     greeting("Dave")
#     print(color)


# another()
# print(count)


game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input(
        "\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chose " + str(RPS(computer)
                                ).replace('RPS.', '').title() + ".\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            return "🐍 Python wins!"

    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

    print("\nPlay again?")

    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
