import unittest
from XiangqiGame import XiangqiGame

class TestCase(unittest.TestCase):
    # TESTS IMPROPER MOVEMENT - ONE DIAGONAL 
    def test1(self):
        game = XiangqiGame()
        # red - 
        game.make_move('c1', 'd2')
        location = game.get_board_location('c', 1)
        expected = " RE "
        self.assertEqual(location, expected)
    # TESTS PROPER MOVEMENT - TWO DIAGONAL 
    def test2(self):
        game = XiangqiGame()
        # red - 
        game.make_move('c1', 'e3')
        location = game.get_board_location('e', 3)
        expected = " RE "
        self.assertEqual(location, expected)


if __name__ == '__main__':
    unittest.main()