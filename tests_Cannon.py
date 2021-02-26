import unittest
from XiangqiGame import XiangqiGame

class TestCase(unittest.TestCase):
    # TESTS VERTICAL MOVEMENT NO CAPTURE UNTIL JUMP
    def test1(self):
        game = XiangqiGame()
        # red - 
        game.make_move('b3', 'b7')
        # black - 
        game.make_move('h8', 'h5')
        # red - 
        game.make_move('b7', 'b8')
        location = game.get_board_location('b', 8)
        expected = "BCAN"
        self.assertEqual(location, expected)

    # TESTS HORIZONTAL MOVEMENT & NOT MOVING INTO SPACE W/ SAME COLOR PIECE
    def test2(self):
        game = XiangqiGame()
        # red - 
        game.make_move('b3', 'g3')
        # black - 
        game.make_move('h8', 'h5')
        # red - 
        game.make_move('g3', 'h3')
    
        location = game.get_board_location('h',3)
        expected = "RCAN"
        self.assertEqual(location, expected)

    # TEST CORRECT PIECE CAPTURE
    def test3(self):
        game = XiangqiGame()
        # red - 
        game.make_move('b3', 'c3')
        # black - 
        game.make_move('h8', 'h5')
        # # red - 
        game.make_move('c3', 'c7')
        location = game.get_board_location('c', 7)
        expected = "RCAN"
        self.assertEqual(location, expected)

    # TEST MOVE OFF BOARD
    def test4(self):
        game = XiangqiGame()
        # red - move the horse piece 
        game.make_move('b1', 'c3')
        # black - move some piece 
        game.make_move('h8', 'h5')
        # # red - move cannon off board (0)
        game.make_move('b3', 'b0')
        location = game.get_board_location('b', 3)
        expected = "RCAN"
        self.assertEqual(location, expected)

    # TEST JUMPING OVER SAME COLOR PIECE AND NO CAPTURE (SHOULDN'T JUMP)
    def test5(self):
        game = XiangqiGame()
        # red - 
        game.make_move('b3', 'g3')
        # black - 
        game.make_move('h8', 'h5')
        # # red - 
        game.make_move('g3', 'i3')
    
        location = game.get_board_location('g',3)
        expected = "RCAN"
        self.assertEqual(location, expected)
    
    # TEST JUMPING OVER DIFFERENT COLOR PIECE AND NO CAPTURE (SHOULDN'T JUMP)
    def test6(self):
        game = XiangqiGame()
        # red - 
        game.make_move('b3', 'b9')
    
        location = game.get_board_location('b',3)
        expected = "RCAN"
        self.assertEqual(location, expected)


if __name__ == '__main__':
    unittest.main()