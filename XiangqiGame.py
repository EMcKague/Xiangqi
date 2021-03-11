import operator


class XiangqiGame:

    def __init__(self):
        self._game_board = [["____"] * 9 for i in range(10)]
        self._player_turn = "red"
        self._game_state = "UNFINISHED"
        self.set_pieces()
        self._col_conversion = {
                                "a": 0,
                                "b": 1,
                                "c": 2,
                                "d": 3,
                                "e": 4,
                                "f": 5,
                                "g": 6,
                                "h": 7,
                                "i": 8,
                                0: "a",
                                1: "b",
                                2: "c",
                                3: "d",
                                4: "e",
                                5: "f",
                                6: "g",
                                7: "h",
                                8: "i"
                            }
        self._row_conversion = {
                                    10: 0,
                                    9: 1,
                                    8: 2,
                                    7: 3,
                                    6: 4,
                                    5: 5,
                                    4: 6,
                                    3: 7,
                                    2: 8,
                                    1: 9,
                                    0: 10
                                }
        self.printStartMsg()
        self.printBoardWithStyling()

    def set_pieces(self):
        for i in range(len(self._game_board)):

            # Row 1
            if i == 0:
                for ii in range(len(self._game_board[i])):
                    if ii == 0 or ii == 8:
                        self._game_board[i][ii] = Chariot("black", "BCHA")
                        self._game_board[i][ii].update_location([i, ii])
                    if ii == 1 or ii == 7:
                        self._game_board[i][ii] = Horse("black", " BH ")
                        self._game_board[i][ii].update_location([i, ii])
                    if ii == 2 or ii == 6:
                        self._game_board[i][ii] = Elephant("black", " BE ")
                        self._game_board[i][ii].update_location([i, ii])
                    if ii == 3 or ii == 5:
                        self._game_board[i][ii] = Advisor("black", " BA ")
                        self._game_board[i][ii].update_location([i, ii])
                    if ii == 4:
                        self._game_board[i][ii] = General("black", " BG ")
                        self._game_board[i][ii].update_location([i, ii])
            
            # Row 3
            if i == 2:
                for ii in range(len(self._game_board[i])):
                    if ii == 1 or ii == 7:
                        self._game_board[i][ii] = Cannon("black", "BCAN")
                        self._game_board[i][ii].update_location([i, ii])

            # Row 4
            if i == 3:
                for ii in range(len(self._game_board[i])):
                    if ii % 2 == 0:
                        self._game_board[i][ii] = Soldier("black", "BSOL")
                        self._game_board[i][ii].update_location([i, ii])

            # Row 7
            if i == 6:
                for ii in range(len(self._game_board[i])):
                    if ii % 2 == 0:
                        self._game_board[i][ii] = Soldier("red", "RSOL")
                        self._game_board[i][ii].update_location([i, ii])
            
            # Row 8
            if i == 7:
                for ii in range(len(self._game_board[i])):
                    if ii == 1 or ii == 7:
                        self._game_board[i][ii] = Cannon("red", "RCAN")
                        self._game_board[i][ii].update_location([i, ii])

            # Row 10
            if i == 9:
                for ii in range(len(self._game_board[i])):
                    if ii == 0 or ii == 8:
                        self._game_board[i][ii] = Chariot("red", "RCHA")
                        self._game_board[i][ii].update_location([i, ii])
                    if ii == 1 or ii == 7:
                        self._game_board[i][ii] = Horse("red", " RH ")
                        self._game_board[i][ii].update_location([i, ii])
                    if ii == 2 or ii == 6:
                        self._game_board[i][ii] = Elephant("red", " RE ")
                        self._game_board[i][ii].update_location([i, ii])
                    if ii == 3 or ii == 5:
                        self._game_board[i][ii] = Advisor("red", " RA ")
                        self._game_board[i][ii].update_location([i, ii])
                    if ii == 4:
                        self._game_board[i][ii] = General("red", " RG ")
                        self._game_board[i][ii].update_location([i, ii])

    def printBoardWithStyling(self):
        rowNum = 10
        colLetter = ["  a", "  b", "  c", "  d", "  e",
                     "  f", "  g", "  h", "  i"]
        for row in self._game_board:
            temp = []
            for el in row:
                if el != "____":
                    temp.append(el._name)
                else:
                    temp.append(el)
        
            if rowNum == 10:
                print(rowNum, " ", '|'.join(temp[0:]))
            else:
                print(rowNum, "  ", '|'.join(temp[0:]))
            rowNum -= 1
        print("    ", '  '.join(colLetter[0:]))
        print('\n')

    def printStartMsg(self):
        print("\nSTARING THE GAME")
        print("HAVE FUN!\n")

    def make_move(self, starting_pos, ending_pos):

        print("make_move, input =", starting_pos, ending_pos)

        # convert inputs to work with table
        starting_loc = self.parse_input(starting_pos)
        ending_loc = self.parse_input(ending_pos)

        # check if piece is at starting_loc
        self.piece_at_location(starting_loc)

        if self.move_is_valid(starting_loc, ending_loc):
            self.validate_move_game_conditions(starting_loc, ending_loc)

        # if still valid, check conditions involving the generals
        if self.move_is_valid(starting_loc, ending_loc):
            # TO DO - Move will put king in own king check
            pass

        if self.move_is_invalid(starting_pos, ending_pos):
            return False

        # move piece
        self.move_pieces(starting_loc, ending_loc)
        new_piece = self._game_board[ending_loc[0]][ending_loc[1]]
        new_piece.update_location(ending_loc)

        # TO DO - check if game has been won

        self.set_player_turn()
        self.printBoardWithStyling()
        return True

    def move_is_valid(self, starting_loc, ending_loc):
        if starting_loc[0] is not False and ending_loc[0] is not False:
            return True
        else:
            return False

    def move_is_invalid(self, starting_loc, ending_loc):
        if starting_loc[0] is False or ending_loc[0] is False:
            return True
        else:
            return False

    def move_pieces(self, starting_loc, ending_loc):
        """
        """

        self._game_board[ending_loc[0]][ending_loc[1]] = \
            self._game_board[starting_loc[0]][starting_loc[1]]
        self._game_board[starting_loc[0]][starting_loc[1]] = "____"

    def parse_input(self, some_input):

        # breaks apart input
        temp = []
        for el in some_input:
            temp.append(el)

        if len(some_input) == 3:
            temp[1] = str(temp[1] + str(temp[2]))
            temp.pop()

        temp[1] = int(temp[1])

        if self.move_in_boundries(temp):
            print("Try Again")
            return False

        new_loc = []
        new_loc.append(self._row_conversion[temp[1]])
        new_loc.append(self._col_conversion[temp[0]])

        return new_loc

    def reverse_parse_input(self, some_input):

        temp = []

        # print("reverse_parse_input")
        # print(some_input)

        temp.append(self._col_conversion[some_input[1]])
        temp.append(str(self._row_conversion[some_input[0]]))

        output = ''.join(temp[:])
        return output

    def set_player_turn(self):
        if self._player_turn == "red":
            self._player_turn = "black"
        else:
            self._player_turn = "red"

    def move_in_boundries(self, board_loc):
        """
        """
        proposed_col = board_loc[0]
        proposed_row = board_loc[1]

        invalidRow = "is not a valid row"
        invalidCol = "is not a valid column"

        possibleCols = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        possibleRows = list(range(1, 11))

        failure_count = 0

        if proposed_col not in possibleCols:
            print(proposed_col, invalidCol)
            failure_count += 1

        if proposed_row not in possibleRows:
            print(proposed_row, invalidRow)
            failure_count += 1

        if failure_count > 0:
            return False
        else:
            return True

    def validate_move_game_conditions(self, starting_loc, ending_loc):

        count_start = 0
        count_end = 0
        # Proper players turn
        if self.incorrect_color_to_move(starting_loc):
            count_start += 1
            print("It's", self._player_turn + "'s turn. Invalid move")

        # Game hasn't been won
        if self.game_is_over():
            count_start += 1
            count_end += 1
            print("The game is over.", self._game_state)

        # Proposed ending location is an avaiable move
        if not self.proposed_move_is_available(starting_loc, ending_loc):

            possible_moves = self.get_possible_moves(starting_loc)
            og_ending_loc = self.reverse_parse_input(ending_loc)

            print("The move to", og_ending_loc, "is not avaiable to",
                  self._game_board[starting_loc[0]][starting_loc[1]])
            print("Your available moves are: ", ', '.join(possible_moves[:]))

            count_end += 1

        if count_start > 0:
            starting_loc[0] = False
            starting_loc.pop()
        if count_end > 0:
            ending_loc[0] = False
            ending_loc.pop()

    def incorrect_color_to_move(self, starting_loc):
        row, col = starting_loc
        if self._game_board[row][col]._color == self._player_turn:
            return True
        else:
            return False

    def piece_at_location(self, starting_loc):
        row, col = starting_loc

        if self._game_board[row][col] == "____":
            print("No piece at starting location")
            starting_loc[0] = False
            starting_loc.pop()

    def game_is_over(self):
        if self._game_state != "UNFINISHED":
            return True
        else:
            return False

    def proposed_move_is_available(self, starting_loc, ending_loc):
        row, col = starting_loc
        starting_piece = self._game_board[row][col]
        available_moves = starting_piece.avialable_moves(self._game_board)

        if ending_loc not in available_moves:
            return False
        else:
            return True

    def get_possible_moves(self, starting_loc):
        possible_moves = []
        piece = self._game_board[starting_loc[0]][starting_loc[1]]
        for move in piece.avialable_moves(self._game_board):
            possible_moves.append(self.reverse_parse_input(move))

        return possible_moves

    def space_is_empty(self, location):
        row, col = location

        if self._game_board[row][col] == "____":
            return True
        else:
            return False


class Pieces:
    def __init__(self, color, name):
        self._color = color
        self._name = name
        self._col = 0
        self._row = 0
        self._ops = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "<": operator.lt,
                ">": operator.gt,
                ">=": operator.ge,
                "<=": operator.le
                }

    def __str__(self):
        return self._name

    def is_in_bounds(self, location):
        row, col = location
        column_check = col > 8 or col < 0
        row_check = row < 0 or row > 9
        in_bounds = False if column_check or row_check else True

        return in_bounds

    def update_location(self, new_loc):
        self._col = new_loc[1]
        self._row = new_loc[0]

    def get_general_location(self, color, game_board):
        piece_color = color == "red"
        name = " RG " if color else " BG "

        for el in game_board:
            if name in el:
                for space in el:
                    location = game_board[el][space]
                    if location == name:
                        return (location._row, location._col)

        return (11, 11)

    def no_conflict(self, game_board, proposed_end_row, proposed_end_col):

        count = 0

        # check if not in bounds
        if not self.is_in_bounds((proposed_end_row, proposed_end_col)):
            count += 1

        else:
            location = game_board[proposed_end_row][proposed_end_col]
            # if in bounds, check if space is not empty
            if location != "____":
                # then check if space if occupied by a piece of the same color
                if location._color == self._color:
                    count += 1

        # check for flying king
        if not self.see_no_evil(game_board, proposed_end_row, proposed_end_col):
            count += 1

        if count > 0:
            return False
        else:
            return True

    def see_no_evil(self, game_board, proposed_end_row, proposed_end_col):
  
        # get gen locations
        RG_location = self.get_general_location("red", game_board)
        BG_location = self.get_general_location("black", game_board)

        general_piece = self._name == " RG " or self._name == " BG "
        general_in_same_col = RG_location[1] == BG_location[1]
        same_col_as_gen = self._col == RG_location[1]
        count = self.count_other_pieces_in_col(game_board, self._col)
        is_red_gen = self._name == " RG "
        opposing_gen = BG_location if is_red_gen else RG_location
        count = self.count_other_pieces_in_col(game_board, proposed_end_col)
    
        # Check if non general pieces moving out of col
        # and generals in the same col
        if general_in_same_col:
            if not general_piece:
                # check if piece is in that col or gen will be in the same col
                if same_col_as_gen:
                    # check if col has another piece to seperate the gens
                    if count < 3:
                        return False

        # check if general is moving into column
        # with other gen and no other pieces
        if general_piece:
            # then determine if proposed_ending_column is == to other gen col
            if proposed_end_col == opposing_gen[1]:
                # if yes, then count number of pieces in col
                if count < 2:
                    return False 

        return True

    def count_other_pieces_in_col(self, game_board, col):
        for i in range(0, 10):
            count = 0
        if game_board[i][col] != "____" and game_board[i][col] != self._name:
            count += 1

        return count


class Soldier(Pieces):

    def __init__(self, color, name):
        # Fun thing to write article about
        super(Soldier, self).__init__(color, name)
        self._river = self.get_river()
        self._moveForward = self.get_moveForward()
        self._moveBackward = self.get_moveBackward()
        self._compare = self.get_compare()

    def get_river(self):
        color_is_black = self._color == "black"
        river = 6 if color_is_black else 5
        return river

    def get_moveForward(self):
        if self._color == "black":
            return self._ops["+"]
        else:
            return self._ops["-"]

    def get_moveBackward(self):
        if self._color == "black":
            return self._ops["-"]
        else:
            return self._ops["+"]

    def get_compare(self):
        if self._color == "black":
            return self._ops[">"]
        else:
            return self._ops["<"]

    def capture(self, proposed_row, proposed_column):
        return True

    def solider_move_list(self):

        forward = (self._moveForward(self._row, 1), self._col)
        left = (self._row, self._col - 1)
        backward = (self._row, self._moveBackward(self._col, 1))

        # check if piece has passed the river
        if self._compare(self._row, self._river):
            return [forward, left, backward]
        else:
            return [forward]

    def avialable_moves(self, game_board):

        possible_moves = [(starting_row, starting_col) for starting_row,
                          starting_col in self.solider_move_list() if
                          self.no_conflict(game_board,
                          starting_row, starting_col)]

        return possible_moves


class General(Pieces):

    def __init__(self, color, name):
        # Fun thing to write article about
        super(General, self).__init__(color, name)
        self._moveForward = self.get_moveForward()
        self._moveBackward = self.get_moveBackward()
        self._compareForward = self.get_compareForward()
        self._palace_col_left_boundry = 3
        self._palace_col_right_boundry = 5
        self._palace_boundry = self.get_palace_boundry()

    def get_moveForward(self):
        if self._color == "black":
            return self._ops["+"]
        else:
            return self._ops["-"]

    def get_moveBackward(self):
        if self._color == "red":
            return self._ops["+"]
        else:
            return self._ops["-"]

    def get_palace_boundry(self):
        if self._color == "red":
            return 7
        else:
            return 2

    def get_compareForward(self):
        if self._color == "red":
            return self._ops[">"]
        else:
            return self._ops["<"]

    def capture(self, proposed_row, proposed_column):
        """
        
        """
        return True

    def general_move_list(self):
      
        moves = []
        forward_move_in_palace = self._compareForward(self._moveForward(self._row, 1), self._palace_row_boundry)
        forward = (self._moveForward(self._row, 1), self._col)
        # move foward 
        if forward_move_in_palace:
            moves.append(forward)
      
        # move left 
        if self._col - 1 >= self._palace_col_left_boundry:
            moves.append((self._row, self._col -1))

        # move right
        if self._col + 1 <= self._palace_col_right_boundry:
            moves.append((self._row, self._col + 1))

        # move backward - no need to check, no_conflict checks for offboard moves
        moves.append((self._moveBackward(self._row, 1), self._col))

        return moves

    def avialable_moves(self, game_board):

        possible_moves = [(starting_row, starting_column) for starting_row, starting_column in self.general_move_list() if self.no_conflict(game_board, starting_row, starting_column)]

        return possible_moves


class Advisor(Pieces):

    def __init__(self, color, name):
        super(Advisor, self).__init__(color, name)
        self._moveForward = self.get_moveForward()
        self._moveBackward = self.get_moveBackward()
        self._compareForward = self.get_compareForward()
        self._palace_col_left_boundry = 3
        self._palace_col_right_boundry = 5
        self._palace_row_boundry = self.get_palace_boundry()

    def get_moveForward(self):
        if self._color == "black":
            return self._ops["+"]
        else:
            return self._ops["-"]

    def get_moveBackward(self):
        if self._color == "red":
            return self._ops["+"]
        else:
            return self._ops["-"]

    def get_palace_boundry(self):
        if self._color == "red":
            return 7
        else:
            return 2

    def get_compareForward(self):
        if self._color == "red":
            return self._ops[">"]
        else:
            return self._ops["<"]

    def capture(self, proposed_row, proposed_column):
        return True

    def can_move_forward(self):
        if self._compareForward(self._moveForward(self._row, 1),
                                self._palace_row_boundry):
            return True
        else:
            return False

    def can_move_left(self):
        if self._col - 1 >= self._palace_col_left_boundry:
            return True
        else:
            return False

    def can_move_right(self):
        if self._col + 1 <= self._palace_col_right_boundry:
            return True
        else:
            return False

    def advisor_move_list(self):
        moves = []

        # move foward left
        if self.can_move_forward() and self.can_move_left:
            moves.append((self._moveForward(self._row, 1), (self._col - 1)))

        # move forward right
        if self.can_move_forward() and self.can_move_right:
            moves.append((self._moveForward(self._row, 1), self._col + 1))

        # move backwards right
        if self._col + 1 >= self._palace_col_right_boundry:
            moves.append((self._moveBackward(self._row, 1), self._col + 1))

        # move backward - no need to check, no_conflict checks for offboard
        if self._col - 1 >= self._palace_col_left_boundry:
            moves.append((self._moveBackward(self._row, 1), self._col - 1))

        return moves

    def avialable_moves(self, game_board):

        possible_moves = [(starting_row, starting_column) for
                          starting_row, starting_column in
                          self.advisor_move_list() if
                          self.no_conflict(game_board,
                          starting_row, starting_column)]

        return possible_moves


class Elephant(Pieces):

    def __init__(self, color, name):
        # Fun thing to write article about
        super(Elephant, self).__init__(color, name)
        self._river = self.get_river()
        self._moveForward = self.get_moveForward()
        self._moveBackward = self.get_moveBackward()
        self._compare = self.get_compare()

    def get_river(self):
        if self._color == 'black':
            return 5
        else:
            return 4

    def get_moveForward(self):
        if self._color == 'black':
            return self._ops["+"]
        else:
            return self._ops["-"]

    def get_moveBackward(self):
        if self._color == 'black':
            return self._ops["-"]
        else:
            return self._ops["+"]

    def get_compare(self):
        if self._color == 'black':
            return self._ops["<"]
        else:
            return self._ops[">"]

    def capture(self, proposed_row, proposed_column):
        """
        If there are special conditions to capture piece other
        than the piece piece must be an opposing color and in
        the avialable_moves, this will tell if it's possible
        """
        return True

    def not_past_river(self):
        if self._compare(self._moveForward(self._row, 2), self._river):
            return True
        else:
            return False

    def no_piece_in_path(self, location):

        if self.path_is_clear(location[0], location[1], game_board):
            return True
        else:
            return False

    def elephant_move_list(self, game_board):

        moves = []

        forwardRight = (self._moveForward(self._row, 2), self._col + 2)
        forwardLeft = (self._moveForward(self._row, 2), self._col - 2)
        backwardRight = (self._moveBackward(self._row, 2), self._col + 2)
        backwardLeft = (self._moveBackward(self._row, 2), self._col - 2)

        if self.not_past_river():
            if self.no_piece_in_path(forwardRight):
                moves.append(forwardRight)

            if self.no_piece_in_path(forwardLeft):
                moves.append(forwardLeft)

        if self.no_piece_in_path(backwardRight):
            moves.append(backwardRight)

        if self.no_piece_in_path(backwardLeft):
            moves.append(backwardLeft)

        return moves

    def avialable_moves(self, game_board):

        possible_moves = [(starting_row, starting_column) for
                          starting_row, starting_column in
                          self.elephant_move_list(game_board) if
                          self.no_conflict(game_board,
                          starting_row, starting_column)]

        return possible_moves

    def path_is_clear(self, proposed_end_row, proposed_end_col, game_board):
        check_row = 0
        check_col = 0

        # get first diagnoal space
        if(self._row - proposed_end_row == 2):
            check_row = self._row - 1
        else:
            check_row = self._row + 1

        if(self._col - proposed_end_col == 2):
            check_col = self._col - 1
        else:
            check_col = self._col + 1

        # check this space is in bounds
        if not self.is_in_bounds((check_row, check_col)):
            return False

        if game_board[check_row][check_col] != "____":
            return False

        return True


class Cannon(Pieces):
    # def __init__(self, color, name):
    #     # Fun thing to write article about
    #     super(Cannon, self).__init__(color, name)

    def capture(self, proposed_ending_row, proposed_ending_column):
        return True

    def cannon_move_list(self, game_board):
        moves = []

        direction_ops = [self._ops["+"], self._ops["-"],
                         self._ops["+"], self._ops["-"]]

        # for each possible direction
        # print("0 = Towards red, 1 = Towards black, 2 = Right, 3 = Left")
        for oper in range(len(direction_ops)):
            checking_for_capture = False

            # first two el in ops are rows
            if oper <= 1:
                direction = direction_ops[oper](self._row, 1)
                space = (direction, self._col)

            else:
                direction = direction_ops[i](self._col, 1)
                space = (self._row, direction)

            while self.is_in_bounds(space):

                # if space is empty and we aren't trying to capture a peice
                if game_board.space_is_empty(space) and
                not checking_for_capture:
                    moves.append(space)

        # if space is not empty and we are trying to capture a piece 
        if game_board[space[0]][space[1]] != "____" and checking_for_capture:
          # print("attempting caputre", space)
          moves.append(space)
          break
        
        # if space is not empty and we aren't trying to capture a piece
        if game_board[space[0]][space[1]] != "____" and not checking_for_capture:
          # print("we are now looking to capture", space)
          checking_for_capture = True

        # increment or decrement i based on direction
        # EX: if moving right this will increment i, increasing the val of direction

        direction = direction_ops[i](direction, 1)

        if i <= 1:
          space = (direction, self._col)
        else:
          space = (self._row, direction)

    return moves

  def avialable_moves(self, game_board):

    possible_moves = [(starting_row, starting_column) for starting_row, starting_column in self.cannon_move_list(game_board) if self.no_conflict(game_board, starting_row, starting_column)]

    # print(possible_moves)
    return possible_moves

class Chariot(Pieces):
  def __init__(self, color, name):
    # Fun thing to write article about
    super(Chariot, self).__init__(color, name)


  def capture(self, proposed_ending_row, proposed_ending_column):
    return True

  def chariot_move_list(self, game_board):
    moves = []
    direction_ops = [self._ops["+"], self._ops["-"], self._ops["+"], self._ops["-"]]

    # for each possible direction
    for i in range(len(direction_ops)):

      # determine which direction we are checking if i <= 1 it's rows, otherwise columns
      if i <= 1:
        direction = direction_ops[i](self._row, 1)
        space = (direction, self._col)
      else:
        direction = direction_ops[i](self._col, 1)
        space = (self._row, direction)

      # only check if in bounds
      while self.is_in_bounds(space):

        # if space is empty
        if game_board[space[0]][space[1]] == "____" :
          moves.append(space)
        
        # if space is not empty, end here
        if game_board[space[0]][space[1]] != "____" :
          moves.append(space)
          break

        direction = direction_ops[i](direction, 1)

        if i <= 1:
          space = (direction, self._col)
        else:
          space = (self._row, direction)

    return moves

  def avialable_moves(self, game_board):

    possible_moves = [(starting_row, starting_column) for starting_row, starting_column in self.cannon_move_list(game_board) if self.no_conflict(game_board, starting_row, starting_column)]

    # print(possible_moves)
    return possible_moves

class Horse(Pieces):
    def __init__(self, color, name):
        # Fun thing to write article about - super in python
        super(Horse, self).__init__(color, name)

    def capture(self):
        return True

    def horse_move_list(self, game_board):

        moves = []
        direction_ops = [self._ops["+"], self._ops["-"], self._ops["+"], self._ops["-"]]

        for i in range(len(direction_ops)):
        # determine which direction we are checking if i <= 1 it's rows, otherwise columns
            if i <= 1:
                direction = direction_ops[i](self._row, 1)
                space = (direction, self._col)

            else:
                direction = direction_ops[i](self._col, 1)
                diag = self._row
                space = (self._row, direction)

            # check first move is in bounds, then if it's not empty
            if self.is_in_bounds(space):
                if not game_board.space_is_empty(space):
                    moves.append(space)
                    break
        
        # if first move is empty, add diagonal moves
            if i <= 1:
                direction = direction_ops[i](direction, 1)
                diag = self._col - 1
                moves.append((direction, diag))
                diag = self._col + 1
                moves.append((direction, diag))
            else: 
                direction = direction_ops[i](direction, 1)
                diag = self._row - 1
                moves.append((diag, direction))
                diag = self._row + 1
                moves.append((diag, direction))

        return moves

  def avialable_moves(self, game_board):

    possible_moves = [(starting_row, starting_column) for starting_row, starting_column in self.horse_move_list(game_board) if self.no_conflict(game_board, starting_row, starting_column)]

    # print(possible_moves)
    return possible_moves
