import numpy as np
import pandas as pd
import gym

from typing import List, Union, Type
from . import utils

class Agent: # Abstract Agent class
    def __init__(self):
        self.id = 0
    def __repr__(self):
        return f"{self.id}"
    def __str__(self):
        return f"{self.id}"
    def place_bet(self) -> float:
        pass
    def add_card(self, card):
        pass
    def decision(self):
        """
        Returns "S" for stand and "H" for hit
        """
        pass

class QAgent(Agent):
    def __init__(self):
        super().__init__()

        # self.Q = np.zeros(shape=(self.env.observation_space.shape, self.env.action_space.shape))
        # print(self.Q)
        self.id = 1
        
        
        
    
    
class ProbAgent(Agent):
    def __init__(self):
        super().__init__()
        self.id = 2
        
class User(Agent):
    def __init__(self):
        self.id = input("Enter a username: ")
        self.cards = []
        self.total = 0
    def __repr__(self):
        return f"{self.id}"
    def place_bet(self) -> float:
        return float(input("Enter how much you would like to bet: "))

    def add_card(self, card):
        self.cards.append(card)
        self.total = utils.compute_total(self.cards)
        print(f"You have been dealt a {card}. Your cards are: {', '.join(map(str, self.cards))}. Your hand total is {self.total}.")

    def decision(self):
        dec = input("Choose H for hit, or S for stand: ").upper()
        while dec not in ["H","S"]:
            dec = input("Choose H for hit, or S for stand: ").upper()
        return dec

    

class LocalPlayer:
    def __init__(self, player: Union[Type[Agent], User]):
        self.player = player
        self.bet = 0
        self.cards = []
        self.total = 0
        self.done = 0 # 0 = playing, 1 = blackjack on first turn, 2 = blackjack after first, 3 = stood, 4 = bust

    def __str__(self):
        return str(self.player)

    def blackjack(self, cards, total: int) -> bool:
        for i, card in enumerate(cards):
            if card == 1:
                return self.blackjack(cards[i+1:], total + 1) or self.blackjack(cards[i+1:], total + 11)
            else:
                total += card
        if total == 21:
            return True
        else:
            return False

    def playing(self):
        return self.done == 0

    def place_bet(self):
        self.bet = self.player.place_bet()

    def get_bet(self) -> float:
        return float(self.bet)
    
    def deal(self, card: int):
        self.player.add_card(card)
        self.cards.append(card)
        self.total = utils.compute_total(self.cards)
        if len(self.cards) == 2 and self.total == 21:
            self.done = 1

    def decision(self):
        d = self.player.decision()
        self.done = 3 if d == "S" else 0
        return d
    
    def hit(self, card: int):
        self.player.add_card(card)
        self.cards.append(card)
        self.total = utils.compute_total(self.cards)
        if self.total == 21:
            self.done = 2
        elif self.total > 21:
            self.done = 4

    def status(self):
        return self.done

if __name__ == "__main__":
    from random import randint
    p = LocalPlayer(User())
    print(p.blackjack([10,1],0))
    p.deal(1)
    p.deal(9)
    p.hit(1)
    while p.playing():
        match p.decision():
            case "S":
                pass
            case "H":
                p.hit(randint(1,13))
    print(p.status())
    pablo = QAgent()