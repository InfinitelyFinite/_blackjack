from unittest import TestCase, main
from unittest.mock import patch
from test_helper_1 import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 1
    def test_user_dealer_blackjack(self, input_mock, randint_mock):
        '''
        Both the user and the dealer end up with a hand value of 21 at the end of the round.
        User hits once after drawing 2 initial cards. Since the dealer and user both have equal value, the end result is Push.
        '''
        output = run_test([1, 2, 8], ['y', 'n'], [3, 5, 7, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 2\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 7\n" \
                   "Dealer has 15.\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 2
    def test_dealer_blackjack(self, input_mock, randint_mock):
        '''
        The user ends up with a hand value of 20 at the end of the round, and the dealer ends up with 21.
        
        User hits once and then stands. Since the dealer has 21 and the user does not, the end result is a dealer win.
        '''
        output = run_test([1, 2, 7], ['y', 'n'], [3, 5, 7, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 2\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 7\n" \
                   "Dealer has 15.\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 3
    def test_user_invalid_input_loss(self, input_mock, randint_mock):
        '''
        User inputs 'p' twice instead of 'y' or 'n'. At the end, user has a total of 17 and dealer has a total of 18.
        As a result, dealer wins.
        '''
        output = run_test([6, 7, 2, 2], ['y', 'p', 'p', 'y', 'n'], [9, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 7\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 15. Hit (y/n)? p\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? p\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 4
    def test_user_blackjack(self, input_mock, randint_mock):
        '''
        The user ends up with a hand value of 21 at the end of the round, and the dealer ends up with 18.
        
        Since the user has 21 and the dealer does not, the end result is a user win.
        '''
        output = run_test([3, 5, 9, 4], ['y', 'y', 'n'], [6, 5, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "Dealer has 11.\n" \
                   "Drew a 7\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 5
    def test_user_stand_dealer_win(self, input_mock, randint_mock):
        '''
        The user stands after drawing the initial two cards adding up to 11.
        The dealer gets a total of 17 and wins the game.
        '''
        output = run_test([5, 6], ['n'], [7, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 6\n" \
                   "You have 11. Hit (y/n)? n\n" \
                   "Final hand: 11.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 10\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 6
    def test_user_busts_dealer_win(self, input_mock, randint_mock):
        '''
        The user hits continuously for 2 times resulting in a total of 25.
        Since the user busts, dealer wins.
        '''
        output = run_test([2, 5, 10, 8], ['y', 'y', 'n'], [7, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 5\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 10\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 7
    def test_dealer_busts_user_win(self, input_mock, randint_mock):
        '''
        The user stands after drawing the initial cards resulting in a total of 19.
        The dealer busts. Since the dealer busts, user wins.
        '''
        output = run_test([1, 8], ['n'], [5, 10, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an 8\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Dealer has 15.\n" \
                   "Drew a 7\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 8
    def test_user_wins(self, input_mock, randint_mock):
        '''
        The user ends up with a hand value of 19 at the end of the round, and the dealer ends up with 18.
        
        Since the user has 19 and the dealer has 18, the end result is a user win since 19 > 18.
        '''
        output = run_test([3, 5, 9, 2], ['y', 'y', 'n'], [6, 5, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "Dealer has 11.\n" \
                   "Drew a 7\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 9
    def test_user_wins_dealer_bust(self, input_mock, randint_mock):
        '''
        The user ends up with a hand value of 19 at the end of the round, and the dealer ends up with 23.
        
        Since the user has 19 and the dealer busts, the end result is a user win.
        '''
        output = run_test([3, 5, 9, 2], ['y', 'y', 'n'], [6, 5, 4, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "Dealer has 11.\n" \
                   "Drew a 4\n" \
                   "Dealer has 15.\n" \
                   "Drew an 8\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 10
    def test_user_dealer_17_push(self, input_mock, randint_mock):
        '''
        The user ends up with a hand value of 17 at the end of the round, and the dealer ends up with 17 as well.
        
        Since the user has 17 and the dealer also has 17, the end result is push.
        '''
        output = run_test([3, 5, 9], ['y', 'n'], [6, 5, 4, 2], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "Dealer has 11.\n" \
                   "Drew a 4\n" \
                   "Dealer has 15.\n" \
                   "Drew a 2\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 11
    def test_dealer_wins(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user has 16 and the dealer has 17. The dealer wins by having a hand greater than the user.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 9\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 12
    def test_user_dealer_bust_dealer_win(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand more than 21.
        The user has 23 and the dealer has 22. Since the user busts, dealer automatically wins.
        '''
        output = run_test([3, 5, 8, 7], ['y', 'y', 'n'], [3, 5, 8, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew an 8\n" \
                   "Dealer has 16.\n" \
                   "Drew a 6\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 13
    def test_user_busts_dealer_blackjack(self, input_mock, randint_mock):
        '''
        The user hits continuously for 2 times resulting in a total of 25 (BUST).
        Since the user busts, dealer wins with a total of 21 (BLACKJACK).
        '''
        output = run_test([2, 5, 10, 8], ['y', 'y', 'n'], [6, 10, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 5\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 10\n" \
                   "Dealer has 16.\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    # test 14
    def test_dealer_busts_user_blackjack(self, input_mock, randint_mock):
        '''
        The user hits continuously for 2 times resulting in a total of 21.
        The user has BLACKJACK, but the dealer busts with a total of 22.
        '''
        output = run_test([2, 5, 10, 4], ['y', 'y', 'n'], [6, 10, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 5\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 10\n" \
                   "Dealer has 16.\n" \
                   "Drew a 6\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()