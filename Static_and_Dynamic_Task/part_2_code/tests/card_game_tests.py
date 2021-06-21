import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.c_ace = Card('clubs', 1)
        self.c_2 = Card('clubs', 2)
        self.c_3 = Card('clubs', 3)
        self.c_4 = Card('clubs', 4)
        self.c_5 = Card('clubs', 5)
        self.c_6 = Card('clubs', 6)
        self.c_7 = Card('clubs', 7)
        self.c_8 = Card('clubs', 8)
        self.c_9 = Card('clubs', 9)
        self.c_10 = Card('clubs', 10)
        self.c_J = Card('clubs', 10)
        self.c_Q = Card('clubs', 10)
        self.c_K = Card('clubs', 10)
        
        self.card_game = CardGame()
        



    def test_check_for_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.c_ace))

    def test_highest_card(self):
        self.assertEqual(self.c_10, self.card_game.highest_card(self.c_10, self.c_3))

    def test_cards_total(self):
        hand = [self.c_ace, self.c_9, self.c_7]
        self.assertEqual(f"You have a total of {17}", self.card_game.cards_total(hand))    
