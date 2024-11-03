from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """
  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 3), "Drew a 3\n")
    self.assertEqual(get_print(print_card_name, 14), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 12), "Drew a Queen\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 0), "BAD CARD\n")

  def test_draw_card(self):
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([4], draw_card), 4)
    self.assertEqual(mock_random([2], draw_card), 2)
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([10], draw_card), 10)

  def test_print_header(self):
    self.assertEqual(get_print(print_header, "Jake"), "-----------\nJake\n-----------\n")
    self.assertEqual(get_print(print_header, "jaCk"), "-----------\njaCk\n-----------\n")
    self.assertEqual(get_print(print_header, "DEALER"), "-----------\nDEALER\n-----------\n")
    self.assertEqual(get_print(print_header, "USER"), "-----------\nUSER\n-----------\n")
    self.assertEqual(get_print(print_header, ""), "-----------\n\n-----------\n")

  def test_draw_starting_hand(self):
    self.assertEqual(mock_random([7, 5], draw_starting_hand, "DEALER"), 12)
    self.assertEqual(mock_random([1, 1], draw_starting_hand, "DEALER"), 22)
    self.assertEqual(mock_random([11, 1], draw_starting_hand, "DEALER"), 21)
    self.assertEqual(mock_random([10, 9], draw_starting_hand, "DEALER"), 19)
    self.assertEqual(mock_random([2, 2], draw_starting_hand, "DEALER"), 4)
    self.assertEqual(mock_random([1, 2], draw_starting_hand, "YOUR"), 13)

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status, 22), "Final hand: 22.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status, 11), "Final hand: 11.\n")
    self.assertEqual(get_print(print_end_turn_status, 4), "Final hand: 4.\n")
    self.assertEqual(get_print(print_end_turn_status, 17), "Final hand: 17.\n")
    self.assertEqual(get_print(print_end_turn_status, 29), "Final hand: 29.\nBUST.\n")

  def test_print_end_game_status(self):
    self.assertEqual(get_print(print_end_game_status, 17, 21), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 21), "-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 22, 27), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 16, 17), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 17), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 21, 22), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 11, 22), "-----------\nGAME RESULT\n-----------\nYou win!\n")
    self.assertEqual(get_print(print_end_game_status, 17, 17), "-----------\nGAME RESULT\n-----------\nPush.\n")
    self.assertEqual(get_print(print_end_game_status, 22, 21), "-----------\nGAME RESULT\n-----------\nDealer wins!\n")

if __name__ == '__main__':
    unittest.main()