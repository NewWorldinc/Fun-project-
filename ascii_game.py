import os
import time
import random

CARD_WIDTH = 11

CARD_TEMPLATE = [
    "┌─────────┐",
    "│{rank:<2}       │",
    "│         │",
    "│    {suit}    │",
    "│         │",
    "│       {rank:>2}│",
    "└─────────┘",
]

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def render_card(rank, suit):
    return [line.format(rank=rank, suit=suit) for line in CARD_TEMPLATE]


def clear():
    print("\033[H\033[J", end="")


def print_table(cards):
    lines = ["" for _ in range(len(CARD_TEMPLATE))]
    for card in cards:
        for i, line in enumerate(card):
            lines[i] += line + "  "
    for l in lines:
        print(l)


def deal_animation(num_cards=5, delay=0.5):
    deck = [(r, s) for s in SUITS for r in RANKS]
    random.shuffle(deck)
    table = []
    for _ in range(num_cards):
        rank, suit = deck.pop()
        table.append(render_card(rank, suit))
        clear()
        print("Dealing cards...\n")
        print_table(table)
        time.sleep(delay)


if __name__ == "__main__":
    deal_animation()
