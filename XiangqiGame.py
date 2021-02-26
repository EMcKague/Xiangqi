# Author: Evan McKague
# Date: 3/3/2020
# Description: Creates a playable game of Xiangqi or Chinese Chess.


class XiangqiGame:

    def __init__(self):
        """
        Initializes game board and places pieces in starting positions, sets the first turn to red
        """
        self._game_board = \
            {10: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                  'h': "____", 'i': "____"},
             9: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"},
             8: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"},
             7: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"},
             6: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"},
             5: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"},
             4: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"},
             3: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"},
             2: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"},
             1: {'a': '____', 'b': "____", 'c': "____", 'd': "____", 'e': "____", 'f': "____", 'g': "____",
                 'h': "____", 'i': "____"}}
        self._player_turn = "red"
        self._unit_dictionary = \
            {"red": {General: " RG ", Advisor: " RA ", Elephant: " RE ", Horse: " RH ", Chariot: "RCHA", Cannon: "RCAN",
                     Solider: " RS "},
             "black": {General: " BG ", Advisor: " BA ", Elephant: " BE ", Horse: " BH ", Chariot: "BCHA",
                       Cannon: "BCAN",
                       Solider: " BS "}}
        self._letters_to_num = {"a": 1,
                                "b": 2,
                                "c": 3,
                                "d": 4,
                                "e": 5,
                                "f": 6,
                                "g": 7,
                                "h": 8,
                                "i": 9}
        self._num_to_letter = {1: "a",
                               2: "b",
                               3: "c",
                               4: "d",
                               5: "e",
                               6: "f",
                               7: "g",
                               8: "h",
                               9: "i"}
        self._game_state = "UNFINISHED"
        self.set_pieces()

    def print_board(self):
        """Displays the game board putting lines between each key of each sub-dictionary"""

        print("| 10|" + str(self._game_board[10]['a']) + "|" + str(self._game_board[10]['b']) + "|" +
              str(self._game_board[10]['c']) + "|" + str(self._game_board[10]['d']) + "|" +
              str(self._game_board[10]['e']) + "|" + str(self._game_board[10]['f']) + "|" +
              str(self._game_board[10]['g']) + "|" + str(self._game_board[10]['h']) + "|" +
              str(self._game_board[10]['i']) + "|")
        print("| 9 |" + str(self._game_board[9]['a']) + "|" + str(self._game_board[9]['b']) + "|" +
              str(self._game_board[9]['c']) + "|" + str(self._game_board[9]['d']) + "|" +
              str(self._game_board[9]['e']) + "|" + str(self._game_board[9]['f']) + "|" +
              str(self._game_board[9]['g']) + "|" + str(self._game_board[9]['h']) + "|" +
              str(self._game_board[9]['i']) + "|")
        print("| 8 |" + str(self._game_board[8]['a']) + "|" + str(self._game_board[8]['b']) + "|" +
              str(self._game_board[8]['c']) + "|" + str(self._game_board[8]['d']) + "|" +
              str(self._game_board[8]['e']) + "|" + str(self._game_board[8]['f']) + "|" +
              str(self._game_board[8]['g']) + "|" + str(self._game_board[8]['h']) + "|" +
              str(self._game_board[8]['i']) + "|")
        print("| 7 |" + str(self._game_board[7]['a']) + "|" + str(self._game_board[7]['b']) + "|" +
              str(self._game_board[7]['c']) + "|" + str(self._game_board[7]['d']) + "|" +
              str(self._game_board[7]['e']) + "|" + str(self._game_board[7]['f']) + "|" +
              str(self._game_board[7]['g']) + "|" + str(self._game_board[7]['h']) + "|" +
              str(self._game_board[7]['i']) + "|")
        print("| 6 |" + str(self._game_board[6]['a']) + "|" + str(self._game_board[6]['b']) + "|" +
              str(self._game_board[6]['c']) + "|" + str(self._game_board[6]['d']) + "|" +
              str(self._game_board[6]['e']) + "|" + str(self._game_board[6]['f']) + "|" +
              str(self._game_board[6]['g']) + "|" + str(self._game_board[6]['h']) + "|" +
              str(self._game_board[6]['i']) + "|")
        print("| 5 |" + str(self._game_board[5]['a']) + "|" + str(self._game_board[5]['b']) + "|" +
              str(self._game_board[5]['c']) + "|" + str(self._game_board[5]['d']) + "|" +
              str(self._game_board[5]['e']) + "|" + str(self._game_board[5]['f']) + "|" +
              str(self._game_board[5]['g']) + "|" + str(self._game_board[5]['h']) + "|" +
              str(self._game_board[5]['i']) + "|")
        print("| 4 |" + str(self._game_board[4]['a']) + "|" + str(self._game_board[4]['b']) + "|" +
              str(self._game_board[4]['c']) + "|" + str(self._game_board[4]['d']) + "|" +
              str(self._game_board[4]['e']) + "|" + str(self._game_board[4]['f']) + "|" +
              str(self._game_board[4]['g']) + "|" + str(self._game_board[4]['h']) + "|" +
              str(self._game_board[4]['i']) + "|")
        print("| 3 |" + str(self._game_board[3]['a']) + "|" + str(self._game_board[3]['b']) + "|" +
              str(self._game_board[3]['c']) + "|" + str(self._game_board[3]['d']) + "|" +
              str(self._game_board[3]['e']) + "|" + str(self._game_board[3]['f']) + "|" +
              str(self._game_board[3]['g']) + "|" + str(self._game_board[3]['h']) + "|" +
              str(self._game_board[3]['i']) + "|")
        print("| 2 |" + str(self._game_board[2]['a']) + "|" + str(self._game_board[2]['b']) + "|" +
              str(self._game_board[2]['c']) + "|" + str(self._game_board[2]['d']) + "|" +
              str(self._game_board[2]['e']) + "|" + str(self._game_board[2]['f']) + "|" +
              str(self._game_board[2]['g']) + "|" + str(self._game_board[2]['h']) + "|" +
              str(self._game_board[2]['i']) + "|")
        print("| 1 |" + str(self._game_board[1]['a']) + "|" + str(self._game_board[1]['b']) + "|" +
              str(self._game_board[1]['c']) + "|" + str(self._game_board[1]['d']) + "|" +
              str(self._game_board[1]['e']) + "|" + str(self._game_board[1]['f']) + "|" +
              str(self._game_board[1]['g']) + "|" + str(self._game_board[1]['h']) + "|" +
              str(self._game_board[1]['i']) + "|")
        print("    ", "  a ", "  b ", "  c ", "  d ", "  e ", "  f ", "  g ", "  h ", "  i ")

    def find_generals(self):
        """
        locates generals on game_board
        called in see_no_evil
        :return: list[row of black general, column of black general,
        row of red general, column of red general]
        """
        pieces_to_check = [" BG ", " RG "]
        general_locations = []
        for row in self._game_board:
            i = 1
            while i <= 9:
                if str(self._game_board[row][self.get_num_to_letter(i)]) in pieces_to_check:
                    general_locations.append(row)
                    general_locations.append(i)
                i += 1

        return general_locations

    def get_game_state(self):
        """
        parameters: None
        returns UNFINISHED, RED_WON, or BLACK_WON
        """
        return self._game_state

    def move_pieces(self, moving_piece_row, moving_piece_col, new_row, new_col):
        """
        move piece to new location, and replaces the previous location of the piece with "____".
        called in data_validation
        :param moving_piece_row: 5
        :param moving_piece_col: "e"
        :param new_row: 6
        :param new_col: "e"
        :return: game_board[5]["e"] = "____" and game_board[6]["e"] = piece that was at e5
        """

        self._game_board[new_row][new_col] = self._game_board[moving_piece_row][moving_piece_col]
        self._game_board[moving_piece_row][moving_piece_col] = "____"

        return

    def get_board_location(self, col, row):
        """
        TO DO
        """
        return str(self._game_board[row][col])

    def check_for_moves_to_not_be_in_check(self, moving_piece_row, moving_piece_col, new_row, new_col, color):
        """
        called in in_checkmate
        :param moving_piece_row: 5
        :param moving_piece_col: "e"
        :param new_row: 6
        :param new_col: "e"
        :param color: "black" or "red"
        :return: True if there is a move to get out of check, otherwise returns False
        """

        storage_container = self._game_board[new_row][new_col]
        self._game_board[new_row][new_col] = self._game_board[moving_piece_row][moving_piece_col]
        self._game_board[moving_piece_row][moving_piece_col] = "____"

        if color == "red":
            if self.red_is_in_check():
                self._game_board[moving_piece_row][moving_piece_col] = self._game_board[new_row][new_col]
                self._game_board[new_row][new_col] = storage_container
                return True
            else:
                self._game_board[moving_piece_row][moving_piece_col] = self._game_board[new_row][new_col]
                self._game_board[new_row][new_col] = storage_container
                return False

        if color == "black":
            if self.black_is_in_check():
                self._game_board[moving_piece_row][moving_piece_col] = self._game_board[new_row][new_col]
                self._game_board[new_row][new_col] = storage_container
                return True
            else:
                self._game_board[moving_piece_row][moving_piece_col] = self._game_board[new_row][new_col]
                self._game_board[new_row][new_col] = storage_container
                return False

    def see_no_evil(self):
        """
        called in data_validation
        checks to make sure generals do not see each other
        ;returns: True if they don't see each other, otherwise returns False
        """

        pieces_to_check = [" BG ", " RG ", "____"]
        if self.find_generals()[1] == self.find_generals()[3]:
            for row in self._game_board:
                if str(self._game_board[row][self.get_num_to_letter(self.find_generals()[1])]) not in pieces_to_check:
                    return True

        return False

    def possible_red_moves(self):
        """
        called in in_stalemate
        :return: list((possible row, possible column), (10, 5), (etc))
        """
        some_list = []
        for row in self._game_board:
            i = 1
            while i <= 9:
                if "R" in str(self._game_board[row][self.get_num_to_letter(i)]):
                    for location in \
                            self._game_board[row][self.get_num_to_letter(i)].available_moves(row, i,
                                                                                             self._game_board):
                        some_list.append(location)
                i += 1

        return some_list

    def possible_black_moves(self):
        """
        called in in_stalemate
        :return: list((possible row, possible column), (10, 5), (etc))
        """
        some_list = []
        for row in self._game_board:
            i = 1
            while i <= 9:
                if "R" in str(self._game_board[row][self.get_num_to_letter(i)]):
                    for location in \
                            self._game_board[row][self.get_num_to_letter(i)].available_moves(row, i,
                                                                                             self._game_board):
                        some_list.append(location)
                i += 1

        return some_list

    # def piece_location_black_check(self):
    #     some_list = []
    #     for row in self._game_board:
    #         i = 1
    #         while i <= 9:
    #             if "R" in str(self._game_board[row][self.get_num_to_letter(i)]):
    #                 for location in \
    #                         self._game_board[row][self.get_num_to_letter(i)].available_moves(row, i, self._game_board):
    #
    #                     placeholder_list = []
    #                     self.reverse_input(location, placeholder_list)
    #                     if str(self._game_board[placeholder_list[0]][placeholder_list[1]]) == " BG ":
    #                         print(self._game_board[placeholder_list[0]][placeholder_list[1]], "is in check by",
    #                               self._game_board[row][self.get_num_to_letter(i)])
    #                         some_list.append((row, self.get_num_to_letter(i)))
    #
    #                 i += 1
    #             else:
    #                 i += 1
    #
    #     return some_list

    def red_is_in_check(self):
        """
        iterates through all black pieces on the board and checks if their available moves have the red general in it
        called in is_in_check & in_checkmate
        :return: True if red king in check
        """

        for row in self._game_board:
            i = 1
            while i <= 9:
                if "B" in str(self._game_board[row][self.get_num_to_letter(i)]):
                    for location in \
                            self._game_board[row][self.get_num_to_letter(i)].available_moves(row, i, self._game_board):
                        placeholder_list = []
                        self.reverse_input(location, placeholder_list)
                        if str(self._game_board[placeholder_list[0]][placeholder_list[1]]) == " RG ":
                            print(self._game_board[placeholder_list[0]][placeholder_list[1]], "is in check by",
                                  self._game_board[row][self.get_num_to_letter(i)])
                            return True

                    i += 1
                else:
                    i += 1

        return False

    def black_is_in_check(self):
        """
        iterates through all red pieces on the board and checks if their available moves have the black general in it
        called in is_in_check & in_checkmate
        :return: True if red king in check
         """

        for row in self._game_board:
            i = 1
            while i <= 9:
                if "R" in str(self._game_board[row][self.get_num_to_letter(i)]):

                    for location in \
                            self._game_board[row][self.get_num_to_letter(i)].available_moves(row, i, self._game_board):

                        placeholder_list = []
                        self.reverse_input(location, placeholder_list)
                        if str(self._game_board[placeholder_list[0]][placeholder_list[1]]) == " BG ":
                            print(self._game_board[placeholder_list[0]][placeholder_list[1]], "is in check by",
                                  self._game_board[row][self.get_num_to_letter(i)])
                            return True

                    i += 1
                else:
                    i += 1

        return False

    def is_in_check(self, color):
        """
        called by user
        parameter: color red or black
        returns: True if in check or False if not in check
        """
        if color == "black":
            if self.black_is_in_check():
                return True
        if color == "red":
            if self.red_is_in_check():
                return True

        return False

    def in_checkmate(self, color):
        """
        called at end of make_move
        :param color: "black" or "red"
        :return: True if opposing color has no moves to get themselves out of check, otherwise returns False
        """

        if color == "black":
            if self.red_is_in_check():
                for row in self._game_board:
                    i = 1
                    while i <= 9:
                        if "R" in str(self._game_board[row][self.get_num_to_letter(i)]):
                            for location in \
                                    self._game_board[row][self.get_num_to_letter(i)].available_moves(row, i,
                                                                                                     self._game_board):
                                placeholder_list = []
                                self.reverse_input(location, placeholder_list)
                                if self.check_for_moves_to_not_be_in_check(row, self.get_num_to_letter(i),
                                                                           placeholder_list[0], placeholder_list[1],
                                                                           "red"):
                                    return False
                        i += 1

                self._game_state = "BLACK_WON"
                return True

        if color == "red":
            if self.black_is_in_check():
                for row in self._game_board:
                    i = 1
                    while i <= 9:
                        if "B" in str(self._game_board[row][self.get_num_to_letter(i)]):
                            for location in \
                                    self._game_board[row][self.get_num_to_letter(i)].available_moves(row, i,
                                                                                                     self._game_board):
                                placeholder_list = []
                                self.reverse_input(location, placeholder_list)
                                if self.check_for_moves_to_not_be_in_check(row, self.get_num_to_letter(i),
                                                                           placeholder_list[0], placeholder_list[1],
                                                                           "black"):
                                    return False
                        i += 1

                print("game state change")
                self._game_state = "RED_WON"
                return True

    def in_stalemate(self, color):
        """
        called at end of make_move
        :param color: "black" or "red"
        :return: True if opposite color has no more moves, False if moves available
        """

        if color == "black":
            possible_red_moves = self.possible_red_moves()
            if len(possible_red_moves) == 0:
                return True

        if color == "red":
            possible_black_moves = self.possible_black_moves()

            if len(possible_black_moves) == 0:
                return True

        return False

    def parse_input(self, some_input, some_list):
        """
        called in make_move
        :param some_input: a10
        :param some_list: an empty list to append input to
        :return: some_list['a', 10]
        """

        for el in some_input:
            some_list.append(el)

        if len(some_input) == 3:
            some_list[1] = str(some_list[1]) + str(some_list[2])
            some_list.pop(2)

        some_list[1] = int(some_list[1])

        return some_list

    def reverse_input(self, two_numbers, placeholder_list):
        """
        called in red_is_in_check, black_is_in_check, & in_checkmate
        :param two_numbers: EX (9, 1)
        :param placeholder_list: empty list to append the numbers to
        :return: placeholder_list[9, 'a']
        """
        i = 0
        for el in two_numbers:
            if i == 0:
                placeholder_list.append(el)
                i += 1
            else:
                placeholder_list.append(str(self.get_num_to_letter(el)))

        return placeholder_list
    
    def make_readable_data(self, possible_moves):
        """
        TO DO
        """
        newlist=[]
        for el in possible_moves:
            temp = [el[1],el[0]]
            temp[0] = self._num_to_letter[temp[0]]
            temp[1] = str(temp[1])
            temp = ''.join(temp[0:2])
            newlist.append(temp)

        newlist = ", ".join(newlist[0:])

        return newlist

    def data_validation(self, starting_row, starting_column, ending_row, ending_column, ending_loc):
        """
        called in make_move
        checks input in make_move for the following:
            within range of board 
            piece is at starting location 
            proper players turn
            proposed move is a legal move 
            game hasn't been won 
            won't cause the players king to be in check
            the kings can't see each other after move
        If any come back false, returns the proper message to display which error.
        :param starting_row: 3
        :param starting_column: "b"
        :param ending_row: 10
        :param ending_column: "b"
        :param ending_loc: (10, 2)
        :return: True if all checks are passed otherwise error message
        """

        # input within range of board
        if ending_row not in range(1, 11) or ending_column not in self._letters_to_num or \
                starting_row not in range(1, 11) or starting_column not in self._letters_to_num:
            print("Input not on board. Valid row range = 1 - 10. Valid column range = a - i")
            return False

        # there is piece at starting location
        if self._game_board[starting_row][starting_column] == str(self._game_board[starting_row][starting_column]):
            print("No valid piece at location " + str(starting_column) + str(starting_row))
            return False

        # turn order
        if self._game_board[starting_row][starting_column].get_color() != self._player_turn:
            print("It's " + str(self._player_turn) + "s turn")
            return False

        # place to move to is in available moves for selected piece
        if ending_loc not in self._game_board[starting_row][starting_column].available_moves(starting_row,
                                                                                             self.get_letters_to_num(
                                                                                                 starting_column),
                                                                                             self._game_board):
            print("\nThat move is not available to " + str(self._game_board[starting_row][starting_column]))
            readableData = self._game_board[starting_row][starting_column].available_moves(starting_row,
                                                                                             self.get_letters_to_num(
                                                                                                 starting_column),
                                                                                             self._game_board)
            PossibleMovesReadable = self.make_readable_data(readableData);     
            print("The available moves are", PossibleMovesReadable)
            return False

        # game state
        if self._game_state != "UNFINISHED":
            print("The game is over, no more valid moves")
            return False

        # moves piece for other tests
        self.move_pieces(starting_row, starting_column, ending_row, ending_column)

        # puts your king in check - red
        if self._game_board[ending_row][ending_column].get_color() == "red":
            if self.red_is_in_check():
                self.move_pieces(ending_row, ending_column, starting_row, starting_column)
                print("This move would put/leave your general in check")
                return False

        # put your king in check - black
        if self._game_board[ending_row][ending_column].get_color() == "black":
            if self.black_is_in_check():
                self.move_pieces(ending_row, ending_column, starting_row, starting_column)
                print("This move would put/leave your general in check")
                return False

        # kings see each other
        if not self.see_no_evil():
            self.move_pieces(ending_row, ending_column, starting_row, starting_column)
            print("The generals can't see each other. There must be a piece between them when in the same column")
            return False

        return True

    def make_move(self, starting_pos, ending_pos):
        """
        called by user
        displays msg explaining how input is wrong via data_validation if input is invalid,
        otherwise moves the piece and sets up for the next turn unless it's the winning move where the game is stopped
        :parameter: (square moved from, square to move to) example: e1, e2
        :returns: True if piece moved successfully or False along with message if piece didn't move
        """
        # print("MAKING MOVE \nFrom:", starting_pos,"\nTo:", ending_pos)

        # separate inputs into workable list indices
        starting_loc = []
        self.parse_input(starting_pos, starting_loc)

        ending_loc = []
        self.parse_input(ending_pos, ending_loc)
        ending_loc.append((ending_loc[1], self.get_letters_to_num(ending_loc[0])))

        # validate the data, if true moves the piece.
        if self.data_validation(starting_loc[1], starting_loc[0], ending_loc[1], ending_loc[0], ending_loc[2]):

            self.set_player_turn()
            self.print_board()
            if self.in_stalemate(self._game_board[ending_loc[1]][ending_loc[0]].get_color()) or \
                    self.in_checkmate(self._game_board[ending_loc[1]][ending_loc[0]].get_color()):
                print("game over")
            return True
        else:
            return False

    def get_letters_to_num(self, letter_in_need_of_converting):
        """
        called in make_move, data_validation,
        turns letters into numbers that correspond to the game board
        :param letter_in_need_of_converting: "a"
        :return: 1
        """
        return self._letters_to_num[letter_in_need_of_converting]

    def get_num_to_letter(self, number_in_need_of_converting):
        """
        called in reverse_input, in_checkmate, red_is_in_check, black_is_in_check, possible_black_moves,
        possible_red_moves, see_no_evil, & find_generals
        turns numbers into letters that correspond to the game board
        :param number_in_need_of_converting:
        :return:
        """
        return self._num_to_letter[number_in_need_of_converting]

    def get_game_board(self):
        return self._game_board

    def set_player_turn(self):
        if self._player_turn == "red":
            self._player_turn = "black"
        else:
            self._player_turn = "red"

    def set_pieces(self):
        """
        Places pieces in their starting position intializing them as classes of Piece
        :parameter: None
        :return: None
        """
        pawn_placement = ["a", "c", "e", "g", "i"]
        chariot_placement = ["a", "i"]
        horse_cannon_placement = ["b", "h"]
        advisor_placement = ["d", "f"]
        elephant_placement = ["c", "g"]
        general_placement = ["e"]

        # place soldiers
        for key in self._game_board:
            if key == 4:
                for el in self._game_board[key]:
                    if el in pawn_placement:
                        self._game_board[key][el] = \
                            Solider("red", self._unit_dictionary["red"][Solider])
            if key == 7:
                for el in self._game_board[key]:
                    if el in pawn_placement:
                        self._game_board[key][el] = \
                            Solider("black", self._unit_dictionary["black"][Solider])
            # place starting row
            if key == 1:
                for el in self._game_board[key]:
                    if el in chariot_placement:
                        self._game_board[key][el] = \
                            Chariot("red", self._unit_dictionary["red"][Chariot])
                    if el in horse_cannon_placement:
                        self._game_board[key][el] = \
                            Horse("red", self._unit_dictionary["red"][Horse])
                    if el in elephant_placement:
                        self._game_board[key][el] = \
                            Elephant("red", self._unit_dictionary["red"][Elephant])
                    if el in advisor_placement:
                        self._game_board[key][el] = \
                            Advisor("red", self._unit_dictionary["red"][Advisor])
                    if el in general_placement:
                        self._game_board[key][el] = \
                            General("red", self._unit_dictionary["red"][General])
            if key == 10:
                for el in self._game_board[key]:
                    if el in chariot_placement:
                        self._game_board[key][el] = \
                            Chariot("black", self._unit_dictionary["black"][Chariot])
                    if el in horse_cannon_placement:
                        self._game_board[key][el] = \
                            Horse("black", self._unit_dictionary["black"][Horse])
                    if el in elephant_placement:
                        self._game_board[key][el] = \
                            Elephant("black", self._unit_dictionary["black"][Elephant])
                    if el in advisor_placement:
                        self._game_board[key][el] = \
                            Advisor("black", self._unit_dictionary["black"][Advisor])
                    if el in general_placement:
                        self._game_board[key][el] = \
                            General("black", self._unit_dictionary["black"][General])
            # place cannons
            if key == 3:
                for el in self._game_board[key]:
                    if el in horse_cannon_placement:
                        self._game_board[key][el] = \
                            Cannon("red", self._unit_dictionary["red"][Cannon])
            if key == 8:
                for el in self._game_board[key]:
                    if el in horse_cannon_placement:
                        self._game_board[key][el] = \
                            Cannon("black", self._unit_dictionary["black"][Cannon])


class Piece:

    def __init__(self, color, name):
        self._color = color
        self._name = name
        self._num_to_letters = {1: "a",
                                2: "b",
                                3: "c",
                                4: "d",
                                5: "e",
                                6: "f",
                                7: "g",
                                8: "h",
                                9: "i"}

    def __str__(self):
        return self._name

    def get_num_to_letters(self, number_in_need_of_converting):
        return self._num_to_letters[number_in_need_of_converting]

    def available_moves(self, starting_row, starting_column, game_board):
        print("Error")

    def is_in_bounds(self, proposed_ending_row, proposed_ending_column):
        """
        :parameter: self, square moving from and square moving to
        :returns: True if move is on game board, False if off game board
        """

        if proposed_ending_column > 9 or proposed_ending_column < 1 \
                or proposed_ending_row < 1 or proposed_ending_row > 10:
            return False
        else:
            return True

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def no_conflict(self, color, starting_row, starting_column, game_board):

        if self.is_in_bounds(starting_row, starting_column):
            if self._name == "RCAN" or self._name == "BCAN":
                if game_board[starting_row][self.get_num_to_letters(starting_column)] != "____":
                    return False
                else:
                    return True
            if game_board[starting_row][self.get_num_to_letters(starting_column)] != \
                    str(game_board[starting_row][self.get_num_to_letters(starting_column)]):
                if game_board[starting_row][self.get_num_to_letters(starting_column)].get_color() != color:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def no_conflict_horse(self, starting_row, starting_column, game_board):
        """
        called in available_moves for Horse
        :param starting_row: 10
        :param starting_column: 2
        :param game_board: self._game_board
        :return: True if valid location to move
        """
        if self.is_in_bounds(starting_row, starting_column):
            if str(game_board[starting_row][self.get_num_to_letters(starting_column)]) == "____":
                return True
            else:
                return False
        else:
            return False

    def non_horizontal_moves_list(self, starting_row, starting_column):
        return [(starting_row + 1, starting_column), (starting_row, starting_column + 1),
                (starting_row - 1, starting_column), (starting_row, starting_column - 1)]

    def horizontal_moves_list(self, starting_row, starting_column):
        return [(starting_row - 1, starting_column + 1), (starting_row - 1, starting_column - 1),
                (starting_row + 1, starting_column - 1), (starting_row + 1, starting_column + 1)]

    def in_palace(self, proposed_ending_row, proposed_ending_column, color):
        if color == "red":
            if proposed_ending_column > 6 or proposed_ending_column < 4 or proposed_ending_row > 3:
                return False
            else:
                return True
        if color == "black":
            if proposed_ending_column > 6 or proposed_ending_column < 4 or proposed_ending_row < 6:
                return False
            else:
                return True

    def no_river_crossing(self, proposed_ending_row, color):

        if color == "red":
            if proposed_ending_row > 5:
                return False
            else:
                return True
        if color == "black":
            if proposed_ending_row < 6:
                return False
            else:
                return True

    def cannon_jump(self, direction, color, starting_row, starting_column, game_board, possible_moves):
        while self.is_in_bounds(starting_row, starting_column):
            if direction == "up":
                if game_board[starting_row][self.get_num_to_letters(starting_column)] != \
                        str(game_board[starting_row][self.get_num_to_letters(starting_column)]):
                    if game_board[starting_row][self.get_num_to_letters(starting_column)].get_color() != color:
                        return possible_moves.append((starting_row, starting_column))
                    else:
                        starting_row += 1
                else:
                    starting_row += 1

            if direction == "down":
                # print("the direction is down")
                if game_board[starting_row][self.get_num_to_letters(starting_column)] != \
                        str(game_board[starting_row][self.get_num_to_letters(starting_column)]):
                    if game_board[starting_row][self.get_num_to_letters(starting_column)].get_color() != color:
                        # print("down", starting_row, starting_column)
                        return possible_moves.append((starting_row, starting_column))
                    else:
                        starting_row -= 1
                else:
                    starting_row -= 1

            if direction == "left":
                # print("the direction is left")
                if game_board[starting_row][self.get_num_to_letters(starting_column)] != \
                        str(game_board[starting_row][self.get_num_to_letters(starting_column)]):
                    if game_board[starting_row][self.get_num_to_letters(starting_column)].get_color() != color:
                        # print("left", starting_row, starting_column)
                        return possible_moves.append((starting_row, starting_column))
                    else:
                        starting_column -= 1
                else:
                    starting_column -= 1

            if direction == "right":
                # print("the direction is right")
                if game_board[starting_row][self.get_num_to_letters(starting_column)] != \
                        str(game_board[starting_row][self.get_num_to_letters(starting_column)]):
                    if game_board[starting_row][self.get_num_to_letters(starting_column)].get_color() != color:
                        # print("right", starting_row, starting_column)
                        return possible_moves.append((starting_row, starting_column))
                    else:
                        starting_column += 1
                else:
                    starting_column += 1

        return possible_moves

    def solider_move_list(self, starting_row, starting_column, color):
        if color == "red":
            if starting_row > 5:
                return [(starting_row + 1, starting_column), (starting_row, starting_column + 1),
                        (starting_row, starting_column - 1)]
            else:
                return [(starting_row + 1, starting_column)]

        if color == "black":
            if starting_row < 6:
                return [(starting_row - 1, starting_column), (starting_row, starting_column + 1),
                        (starting_row, starting_column - 1)]
            else:
                return [(starting_row - 1, starting_column)]


class General(Piece):
    """
    the general can only move horizontally or vertically and must stay in the palace
    """
    def available_moves(self, starting_row, starting_column, game_board):
        possible_moves = [(starting_row, starting_column) for starting_row, starting_column in
                          self.non_horizontal_moves_list(starting_row, starting_column)
                          if self.no_conflict(self._color, starting_row, starting_column, game_board) and
                          self.in_palace(starting_row, starting_column, self._color)]

        return possible_moves


class Advisor(Piece):
    """
    the advisor can only move diagonally and must stay in the palace
    """

    def available_moves(self, starting_row, starting_column, game_board):
        possible_moves = [(starting_row, starting_column) for starting_row, starting_column in
                          self.horizontal_moves_list(starting_row, starting_column)
                          if self.no_conflict(self._color, starting_row, starting_column, game_board) and
                          self.in_palace(starting_row, starting_column, self._color)]

        return possible_moves


class Elephant(Piece):
    """
    Elephants can move exactly two spaces diagonally and they cannot cross the river
    (only 7 available moves)
    """

    def available_moves(self, starting_row, starting_column, game_board):

        possible_moves = []
        # -, -
        i = 1
        if self.no_conflict(self._color, starting_row - i, starting_column - i, game_board) \
                and self.no_river_crossing(starting_row - i, self._color):
            i += 1
            if self.no_conflict(self._color, starting_row - i, starting_column - i, game_board) \
                    and self.no_river_crossing(starting_row - i, self._color):
                possible_moves.append((starting_row - i, starting_column - i))
        # +, -
        i = 1
        if self.no_conflict(self._color, starting_row + i, starting_column - i, game_board) \
                and self.no_river_crossing(starting_row + i, self._color):
            i += 1
            if self.no_conflict(self._color, starting_row + i, starting_column - i, game_board) \
                    and self.no_river_crossing(starting_row + i, self._color):
                possible_moves.append((starting_row + i, starting_column - i))
        # -, +
        i = 1
        if self.no_conflict(self._color, starting_row - i, starting_column + i, game_board) \
                and self.no_river_crossing(starting_row - i, self._color):
            i += 1
            if self.no_conflict(self._color, starting_row - i, starting_column + i, game_board) \
                    and self.no_river_crossing(starting_row - i, self._color):
                possible_moves.append((starting_row - i, starting_column + i))
        # +, +
        i = 1
        if self.no_conflict(self._color, starting_row + i, starting_column + i, game_board) \
                and self.no_river_crossing(starting_row + i, self._color):
            i += 1
            if self.no_conflict(self._color, starting_row + i, starting_column + i, game_board) \
                    and self.no_river_crossing(starting_row + i, self._color):
                possible_moves.append((starting_row + i, starting_column + i))

        return possible_moves


class Horse(Piece):
    """
    Moves one space horizontally or vertically then can move on space diagonally in that same direction
    """

    def available_moves(self, starting_row, starting_column, game_board):

        possible_moves = []
        # down
        i = 1
        if self.no_conflict_horse(starting_row - i, starting_column, game_board):
            i += 1
            if self.no_conflict(self._color, starting_row - i, starting_column + 1, game_board):
                possible_moves.append((starting_row - i, starting_column + 1))
            if self.no_conflict(self._color, starting_row - i, starting_column - 1, game_board):
                possible_moves.append((starting_row - i, starting_column - 1))
        # up
        i = 1
        if self.no_conflict_horse(starting_row + i, starting_column, game_board):
            i += 1
            if self.no_conflict(self._color, starting_row + i, starting_column + 1, game_board):
                possible_moves.append((starting_row + i, starting_column + 1))
            if self.no_conflict(self._color, starting_row + i, starting_column - 1, game_board):
                possible_moves.append((starting_row + i, starting_column - 1))
        # right
        i = 1
        if self.no_conflict_horse(starting_row, starting_column + i, game_board):
            i += 1
            if self.no_conflict(self._color, starting_row - 1, starting_column + i, game_board):
                possible_moves.append((starting_row - 1, starting_column + i))
            if self.no_conflict(self._color, starting_row + 1, starting_column + i, game_board):
                possible_moves.append((starting_row + 1, starting_column + i))
        # left
        i = 1
        if self.no_conflict_horse(starting_row, starting_column - i, game_board):
            i += 1
            if self.no_conflict(self._color, starting_row - 1, starting_column - i, game_board):
                possible_moves.append((starting_row - 1, starting_column + i))
            if self.no_conflict(self._color, starting_row + 1, starting_column - i, game_board):
                possible_moves.append((starting_row + 1, starting_column - i))

        return possible_moves


class Chariot(Piece):
    """
    Moves horizontally and vertically until it hits the end of the board or another piece
    """

    def available_moves(self, starting_row, starting_column, game_board):
        possible_moves = []
        i = 1
        proposed_row = starting_row
        while self.no_conflict(self._color, proposed_row + i, starting_column, game_board):
            possible_moves.append((proposed_row + i, starting_column))
            i += 1
        proposed_row = starting_row
        i = 1
        while self.no_conflict(self._color, proposed_row - i, starting_column, game_board):
            possible_moves.append((proposed_row - i, starting_column))
            i += 1
        proposed_row = starting_row
        i = 1
        while self.no_conflict(self._color, proposed_row, starting_column + i, game_board):
            possible_moves.append((proposed_row, starting_column + i))
            i += 1
        proposed_row = starting_row
        i = 1
        while self.no_conflict(self._color, proposed_row, starting_column - i, game_board):
            possible_moves.append((proposed_row, starting_column - i))
            i += 1

        return possible_moves


class Cannon(Piece):
    """
    Moves like Chariot, however when the cannon wants to take a piece
    it has to jump over one piece of any color before taking the unit
    """
    def available_moves(self, starting_row, starting_column, game_board):
        possible_moves = []

        # checks up moves
        proposed_row = starting_row
        i = 1
        while self.no_conflict(self._color, proposed_row + i, starting_column, game_board):
            possible_moves.append((proposed_row + i, starting_column))
            proposed_row += i
        self.cannon_jump("up", self._color, proposed_row + 2, starting_column, game_board, possible_moves)

        # checks down moves
        proposed_row = starting_row
        i = 1
        while self.no_conflict(self._color, proposed_row - i, starting_column, game_board):
            possible_moves.append((proposed_row - i, starting_column))
            proposed_row -= i
        self.cannon_jump("down", self._color, proposed_row - 2, starting_column, game_board, possible_moves)

        # checks right moves
        proposed_column = starting_column
        i = 1
        while self.no_conflict(self._color, starting_row, proposed_column + i, game_board):
            possible_moves.append((starting_row, proposed_column + i))
            proposed_column += 1
        self.cannon_jump("right", self._color, starting_row, proposed_column + 2, game_board, possible_moves)

        # checks left moves
        proposed_column = starting_column
        i = 1
        while self.no_conflict(self._color, starting_row, proposed_column - i, game_board):
            proposed_column -= 1
        self.cannon_jump("left", self._color, starting_row, proposed_column - 2, game_board, possible_moves)

        # print("Cannon, possible moves:",possible_moves)
        return possible_moves


class Solider(Piece):
    """
    can only move towards opposing color's side until it crosses the river. Then it can move horizontally.
    It can never move towards its own side
    """
    def available_moves(self, starting_row, starting_column, game_board):
        possible_moves = [(starting_row, starting_column) for starting_row, starting_column in
                          self.solider_move_list(starting_row, starting_column, self._color)
                          if self.no_conflict(self._color, starting_row, starting_column, game_board)]

        return possible_moves

