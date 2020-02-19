"""
K. Sharsindra Pratheen
Computer Science, Monash University
"""

class Tour:

    def __init__(self):

        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0]]

        self.current_position = [-1, -1]
        self.moved_position = []

    def next_moves(self):
        """
        function return row list of possible next position for the knight
        :return: possible moves
        """

        current_row = self.current_position[0]
        current_column = self.current_position[1]
        self.possible_position = []

        if self.board[current_row + 1][current_column - 2] != '*' and current_column - 2 >= 0 and current_row + 1 <= 7 :
            #Left Left down
            self.possible_position.append([current_row + 1, current_column - 2])
            self.move_1 = True
        else:
            self.move_1 = False

        if self.board[current_row - 1][current_column - 2] != '*' and current_column - 2 >= 0 and current_row - 1 >= 0:
            #left left up
            self.possible_position.append([current_row - 1, current_column - 2])
            self.move_2 = True
        else:
            self.move_2 = False

        if self.board[current_row - 1][current_column + 2] != '*' and current_column + 2 <= 7 and current_row - 1 >= 0 :
            #Right Right Up
            self.possible_position.append([current_row - 1, current_column + 2])
            self.move_3 = True
        else:
            self.move_3 = False

        if self.board[current_row + 1][current_column + 2] != '*' and current_column + 2 <= 7 and current_row + 1 <= 7:
            #Right Right Down
            self.possible_position.append([current_row + 1, current_column + 2])
            self.move_4 = True
        else:
            self.move_4 = False

        if self.board[current_row + 2][current_column + 1] != '*' and current_row + 2 <= 7 and current_column + 1 <= 7:
            #Down Down Right
            self.possible_position.append([current_row + 2, current_column + 1])
            self.move_5 = True
        else:
            self.move_5 = False

        if self.board[current_row + 2][current_column - 1] != '*' and current_row + 2 <= 7 and current_column - 1 >= 0:
            #Down Down Left
            self.possible_position.append([current_row + 2, current_column - 1])
            self.move_6 = True
        else:
            self.move_6 = False

        if self.board[current_row - 2][current_column - 1] != '*' and current_row - 2 >= 0 and current_column - 1 >= 0:
            #up up left
            self.possible_position.append([current_row - 2, current_column - 1])
            self.move_7 = True
        else:
            self.move_7 = False

        if self.board[current_row - 2][current_column + 1] != '*' and current_row - 2 >= 0 and current_column + 1 <= 7:
            #Up Up Right
            self.possible_position.append([current_row - 2, current_column + 1])
            self.move_8 = True
        else:
            self.move_8 = False

        return self.possible_position

"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""