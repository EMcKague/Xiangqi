import unittest
from XiangqiGame import XiangqiGame


class TestCase(unittest.TestCase):
    # TESTS HORIZONTAL MOVEMENT ONCE ACROSS RIVER
    def test1(self):
        game = XiangqiGame()
        # red - move solider one space forward
        game.make_move('a4', 'a5')
        # black - move solider one space forward
        game.make_move('c7', 'c6')
        # # red - move solider one space forward, across river
        game.make_move('a5', 'a6')
        # # black - move solider one space forward, across river
        game.make_move('c6', 'c5')
        # # red - test horizontal movement
        game.make_move('a6', 'b6')
        location = game.get_board_location('b', 6)
        expected = " RS "
        self.assertEqual(location, expected)

    # TESTS HORIZONTAL MOVEMENT BEFORE ACROSS RIVER
    def test2(self):
        game = XiangqiGame()
        # red - move solider one space forward
        game.make_move('a4', 'a5')
        # black - move solider one space forward
        game.make_move('c7', 'c6')
        # # red - move solider one space forward, across river
        game.make_move('a5', 'b5')
        location = game.get_board_location('b', 5)
        expected = "____"
        self.assertEqual(location, expected)

    # TESTS BACKWARDS MOVEMENT
    def test3(self):
        game = XiangqiGame()
        # red - move solider one space forward
        game.make_move('a4', 'a3')
        location = game.get_board_location('a', 3)
        expected = "____"
        self.assertEqual(location, expected)

    # TESTS SOLIDER HORIZONTAL MOVEMENT
    def test4(self):
        game = XiangqiGame()
        game.make_move('a4', 'b5')
        location = game.get_board_location('b', 5)
        expected = "____"
        self.assertEqual(location, expected)
    
    # TESTS PIECE CAPTURE
    def test5(self):
        game = XiangqiGame()
        # red - move solider one space forward
        game.make_move('a4', 'a5')
        # black - move solider one space forward
        game.make_move('c7', 'c6')
        # red - move solider one space forward
        game.make_move('a5', 'a6')
        # black - move solider one space forward
        game.make_move('c6', 'c5')
        # red - move solider one space forward take black solider
        game.make_move('a6', 'a7')
        location = game.get_board_location('a', 7)
        expected = " RS "
        self.assertEqual(location, expected)

    # TESTS MOVEMENT INTO SPACE WITH SAME COLOR PIECE
    def test6(self): 
        game = XiangqiGame()
        # red - move solider one space forward
        game.make_move('a4', 'a5')
        # black - move solider one space forward
        game.make_move('c7', 'c6')
        # red - move solider one space forward, across river
        game.make_move('a5', 'a6')
        # black - move solider one space forward, across river
        game.make_move('c6', 'c5')
        # red - test horizontal movement
        game.make_move('a6', 'b6')
        # black -
        game.make_move('e7', 'e6')
        # red - 
        game.make_move('c4', 'c5')
        # black -
        game.make_move('e6', 'e5')
        # red - 
        game.make_move('c5', 'c6')
        # black -
        game.make_move('e5', 'f5')
        # red - 
        game.make_move('c6', 'b6')
        location = game.get_board_location('c', 6)
        expected = " RS "
        self.assertEqual(location, expected)


if __name__ == '__main__':
    unittest.main()
