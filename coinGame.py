
import math

def actions(coins):
    moves = []

    if len(coins) > 0:
        moves.append('L')
        moves.append('R')

    return moves


def result(coins, action):
    newCoins = coins.copy()

    if action == 'L':
        value = newCoins.pop(0)
    else:
        value = newCoins.pop()

    return newCoins, value


def terminal(coins):
    return len(coins) == 0


def maxValue(coins):
    if terminal(coins):
        return 0

    val = -math.inf

    for act in actions(coins):
        newCoins, value = result(coins, act)

        evalValue = value - minValue(newCoins)

        if evalValue > val:
            val = evalValue

    return val


def minValue(coins):
    if terminal(coins):
        return 0

    val = math.inf

    for act in actions(coins):
        newCoins, value = result(coins, act)

        evalValue = value - maxValue(newCoins)

        if evalValue < val:
            val = evalValue

    return val


def minimax(coins):
    bestAct = None
    bestValue = -math.inf

    for act in actions(coins):
        newCoins, value = result(coins, act)

        evalValue = value - minValue(newCoins)

        if evalValue > bestValue:
            bestValue = evalValue
            bestAct = act

    return bestAct


def play():

    coins = [3, 5, 2, 9, 4]

    player = 'X'
    aiScore = 0
    humanScore = 0

    print("Welcome to Coin Picking Game!")
    print("You are O, AI is X.")
    print("Pick left (L) or right (R).\n")

    while not terminal(coins):

        print("Coins:", coins)

        if player == 'O':

            action = input("Pick L or R: ").upper()

            if action not in actions(coins):
                print("Invalid move!\n")
                continue

        else:
            action = minimax(coins)
            print("AI picks:", action)

        coins, value = result(coins, action)

        if player == 'X':
            aiScore += value
        else:
            humanScore += value

        print("Picked coin:", value)
        print("AI Score:", aiScore)
        print("Your Score:", humanScore)
        print()

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    if aiScore > humanScore:
        print("AI wins!")
    elif humanScore > aiScore:
        print("You win!")
    else:
        print("It's a draw!")


play()
