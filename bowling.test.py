
import unittest
from bowling import BowlingGame;

class TestStringMethods(unittest.TestCase):
    
    def _roll_a_game_and_score(self, rolls):
        game = BowlingGame();
        [game.roll(pins_down) for pins_down in rolls]
        return game.score()

    def test_should_be_able_to_score_a_game_with_all_zeros(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 0)

    def test_should_be_able_to_score_a_game_with_no_strikes_or_spares(self):
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 90)

    def test_twelve_strikes_in_a_row_score(self):
        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        
        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 300)

    def test_eleven_spare_score(self):
        rolls = [0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10]
        
        score = self._roll_a_game_and_score(rolls)

        self.assertEqual(score, 200)

    def test_negative_input_raises_valueerror(self):
        rolls = [-10, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10]
        
        self.assertRaises(ValueError, self._roll_a_game_and_score, rolls)

    def test_out_of_bound_input_raises_valueerror(self):
        rolls = [7, 5, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10, 0, 10]

        self.assertRaises(ValueError, self._roll_a_game_and_score, rolls)

        
if __name__ == '__main__':
    unittest.main()