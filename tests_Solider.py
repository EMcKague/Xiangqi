import unittest
from XiangqiGame import XiangqiGame

empty = "____"
soldier = "RSOL"


class TestCase(unittest.TestCase):

    # TESTS HORIZONTAL MOVEMENT ONCE ACROSS RIVER
    def test1(self):
        game = XiangqiGame()

        moves = [('a4', 'a5'), ('c7', 'c6'), ('a5', 'a6'), ('c6', 'c5'), ('a6', 'b6')]
        for el in range(len(moves)):
            game.make_move(moves[el][0], moves[el][1])

        location = game.get_board_location('b6')
        expected = soldier
        self.assertEqual(location, expected)

    # TESTS HORIZONTAL MOVEMENT BEFORE ACROSS RIVER
    def test2(self):
        game = XiangqiGame()

        moves = [('a4', 'a5'), ('c7', 'c6'), ('a5', 'b5')]
        for el in range(len(moves)):
            game.make_move(moves[el][0], moves[el][1])

        location = game.get_board_location('b5')
        expected = empty
        self.assertEqual(location, expected)

    # TESTS BACKWARDS MOVEMENT
    def test3(self):
        game = XiangqiGame()

        # red - move solider one space forward
        game.make_move('a4', 'a3')

        location = game.get_board_location('a3')
        expected = empty
        self.assertEqual(location, expected)

    # TESTS SOLIDER HORIZONTAL MOVEMENT
    def test4(self):
        game = XiangqiGame()

        game.make_move('a4', 'b5')

        location = game.get_board_location('b5')
        expected = empty
        self.assertEqual(location, expected)
    
    # TESTS PIECE CAPTURE
    def test5(self):
        game = XiangqiGame()

        moves = [('a4', 'a5'), ('c7', 'c6'), ('a5', 'a6'), ('c6', 'c5'), ('a6', 'a7')]
        for el in range(len(moves)):
            game.make_move(moves[el][0], moves[el][1])

        location = game.get_board_location('a7')
        expected = soldier
        self.assertEqual(location, expected)

    # TESTS MOVEMENT INTO SPACE WITH SAME COLOR PIECE
    def test6(self):
        game = XiangqiGame()

        moves = [('a4', 'a5'), ('c7', 'c6'), ('a5', 'a6'), ('c6', 'c5'), ('a6', 'b6'), ('e7', 'e6'),
        ('c4', 'c5'), ('e6', 'e5'), ('c5', 'c6'), ('e5', 'f5'), ('c6', 'b6')]
        for el in range(len(moves)):
            game.make_move(moves[el][0], moves[el][1])

        location = game.get_board_location('c6')
        expected = soldier
        self.assertEqual(location, expected)


if __name__ == '__main__':
    unittest.main()
