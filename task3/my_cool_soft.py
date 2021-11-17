#!/usr/bin/python3
import random


def dice():
    # emulate single dice throw
    return random.randint(1, 6)


def count_scores(scores):
    pass


def trow_dice(amount):
    # trowing given amount of dice
    return [dice() for _ in range(amount)]

if __name__ == "__main__":
    pass
