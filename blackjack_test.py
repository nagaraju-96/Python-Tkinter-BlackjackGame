import unittest
import tkinter as tk
from blackjackgame import BlackjackGame 


class TestBlackjackGame(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.game = BlackjackGame(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_get_deck(self):
        deck = self.game.get_deck()
        self.assertEqual(len(deck), 52)  

    #deal_cards() method test cases
    def test_deal_cards(self):
        deck = self.game.get_deck()
        self.game.deck = deck
        player_hand = self.game.deal_cards()
        self.assertEqual(len(player_hand), 2)

    def test_deal_cards(self):
        deck = self.game.get_deck()
        self.game.deck = deck
        dealer_hand = self.game.deal_cards()
        self.assertEqual(len(dealer_hand), 2)

    #calculate_hand_value() methode without any ACE card
    def test_calculate_hand_value_no_aces1(self):
        hand1 = [{"rank": "K", "suit": "Hearts"}, {"rank": "Q", "suit": "Diamonds"}]
        value1 = self.game.calculate_hand_value(hand1)
        self.assertEqual(value1, 20)

    def test_calculate_hand_value_no_aces2(self):
        hand2 = [{"rank": "2", "suit": "Hearts"}, {"rank": "3", "suit": "Diamonds"}]
        value2 = self.game.calculate_hand_value(hand2)
        self.assertEqual(value2, 5)

    def test_calculate_hand_value_no_aces3(self):
        hand3 = [{"rank": "A", "suit": "Hearts"}, {"rank": "7", "suit": "Diamonds"}]
        value3 = self.game.calculate_hand_value(hand3)
        self.assertEqual(value3, 18)

    def test_calculate_hand_value_no_aces4(self):
        hand4 = [{"rank": "10", "suit": "Hearts"}, {"rank": "10", "suit": "Diamonds"}]
        value4 = self.game.calculate_hand_value(hand4)
        self.assertEqual(value4, 20)

    def test_calculate_hand_value_no_aces5(self):
        hand5 = [{"rank": "6", "suit": "Hearts"}]
        value5 = self.game.calculate_hand_value(hand5)
        self.assertEqual(value5, 6)

    #calculate_hand_value() methode with ACE card
    def test_calculate_hand_value_with_aces1(self):
        hand1 = [{"rank": "A", "suit": "Hearts"}, {"rank": "K", "suit": "Diamonds"}]
        value1 = self.game.calculate_hand_value(hand1)
        self.assertEqual(value1, 21)

    def test_calculate_hand_value_with_aces2(self):
        hand2 = [{"rank": "A", "suit": "Hearts"}, {"rank": "Q", "suit": "Diamonds"}]
        value2 = self.game.calculate_hand_value(hand2)
        self.assertEqual(value2, 21)

    def test_calculate_hand_value_with_aces3(self):
        hand3 = [{"rank": "A", "suit": "Hearts"}, {"rank": "2", "suit": "Diamonds"}]
        value3 = self.game.calculate_hand_value(hand3)
        self.assertEqual(value3, 13)

    def test_calculate_hand_value_with_aces4(self):
        hand4 = [{"rank": "A", "suit": "Hearts"}, {"rank": "A", "suit": "Diamonds"}, {"rank": "K", "suit": "Spades"}]
        value4 = self.game.calculate_hand_value(hand4)
        self.assertEqual(value4, 12)

    def test_calculate_hand_value_with_aces5(self):
        hand5 = [{"rank": "A", "suit": "Hearts"}, {"rank": "A", "suit": "Diamonds"}, {"rank": "2", "suit": "Spades"}]
        value5 = self.game.calculate_hand_value(hand5)
        self.assertEqual(value5, 14)

    #reset game methode
    def test_reset_game(self):
        self.game.reset_game()
        self.assertEqual(len(self.game.deck), 48)  
        self.assertEqual(len(self.game.player_hand), 2)
        self.assertEqual(len(self.game.dealer_hand), 2)


if __name__ == '__main__':
    unittest.main()
