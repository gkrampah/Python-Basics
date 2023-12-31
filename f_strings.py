from enum import Enum
import random
import sys
person = "Dave"
coins = 3

#################
# Concatenating strings

print("\n" + person + " has " + str(coins) + " coins left.")

#################
# Previous %s formatting

message = "\n%s has %s coins left." % (person, coins)
print(message)

#################
# Previous string.format() method

# message = "\n{} has {} coins left.".format(person, coins)
# print(message)

# message = "\n{1} has {0} coins left.".format(coins, person)
# print(message)

# message = "\n{person} has {coins} coins left.".format(
#     coins=coins, person=person
# )
# print(message)

# player = {'person': 'Dave', 'coins': 3}

# message = "\n{person} has {coins} coins left.".format(**player)
# print(message)

##################
# f-Strings! This is the way.

# message = f"\n{person} has {coins} coins left."
# print(message)

# message = f"\n{person} has {2 * 5} coins left."
# print(message)

# message = f"\n{person.lower()} has {2 * 5} coins left."
# print(message)

# message = f"\n{player['person']} has {2 * 5} coins left."
# print(message)

##################
# You can pass formatting options

# num = 10
# print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

# for num in range(1, 11):
#     print(f"2.25 times {num} is {2.25 * num:.2f}")

# for num in range(1, 11):
#     print(f"{num} divided by 4.52 is {num / 4.52:.2%}")


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")

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

    return play_rps


play = rps()

play()
