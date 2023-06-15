import unittest
from unittest.mock import patch
from io import StringIO
import sys

from random import seed
from game import get_player_choice, print_outcome, play_again, game_loop

class RockPaperScissorsTest(unittest.TestCase):

    def setUp(self):
        seed(42)

    @patch('builtins.input', side_effect=['rock'])
    def test_get_player_choice_valid_input(self, mock_input):
        player_choice = get_player_choice()
        self.assertEqual(player_choice, 'Rock')

    @patch('builtins.input', side_effect=['invalid', 'rock'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_player_choice_invalid_input(self, mock_stdout, mock_input):
        player_choice = get_player_choice()
        self.assertEqual(player_choice, 'Rock')
        self.assertEqual(mock_stdout.getvalue().strip(), "That's not a valid play. Please choose from Rock, Paper, or Scissors.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_outcome(self, mock_stdout):
        print_outcome("Rock", "Paper", "lose")
        self.assertEqual(mock_stdout.getvalue().strip(), "You lose! Rock loses to Paper!")

    @patch('builtins.input', side_effect=['Y'])
    def test_play_again_yes(self, mock_input):
        play_again_result = play_again()
        self.assertTrue(play_again_result)

    @patch('builtins.input', side_effect=['N'])
    def test_play_again_no(self, mock_input):
        play_again_result = play_again()
        self.assertFalse(play_again_result)

if __name__ == '__main__':
    unittest.main()
