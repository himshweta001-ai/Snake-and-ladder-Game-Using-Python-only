
# Project: Snake and Ladder Game
# Class: 11
# Author: Himshweta
# Topic: Python

import random

print("===================================")
print("       SNAKE AND LADDER GAME")
print("===================================")

# Taking number of players

n = int(input("Enter number of players (2-4): "))

while n < 2 or n > 4:
    print("Invalid number of players!")
    n = int(input("Enter number of players (2-4): "))

# Taking player names

players = []

for i in range(n):
    name = input("Enter Player " + str(i + 1) + " name: ")
    players.append(name)

# Initial positions of players

position = [0] * n

# Positions of snakes and ladders

snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

ladders = {
    6: 25,
    11: 40,
    17: 69,
    46: 90,
    60: 85
}

# Starting the game

winner = -1

while winner == -1:

    for i in range(n):

        print("\n-----------------------------------")
        print(players[i], "'s TURN")

        input("Press Enter to roll the dice...")

        # Generating random dice number

        print("\nRolling the dice...")

        dice = random.randint(1, 6)

        print("The number on the dice is:", dice)

        if position[i] + dice <= 100:

            position[i] = position[i] + dice

            print("Current Position:", position[i])

            # Checking for snake bite

            if position[i] in snakes:

                print("Snake Bite")
                position[i] = snakes[position[i]]

                print("New Position:", position[i])

            # Checking for ladder

            elif position[i] in ladders:

                print("Ladder Climbed")
                position[i] = ladders[position[i]]

                print("New Position:", position[i])

        else:

            print("You need an exact number to reach 100.")

        # Displaying positions of all players

        print("\nCURRENT POSITIONS")

        for j in range(n):
            print(players[j], ":", position[j])

        # Checking winner

        if position[i] == 100:

            winner = i
            break

    if winner != -1:
        break

# Displaying winner

print("\n===================================")
print("CONGRATULATIONS!")
print(players[winner], "WINS THE GAME!")
print("===================================")
