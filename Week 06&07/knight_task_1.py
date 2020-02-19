"""
K. Sharsindra Pratheen
Computer Science, Monash University
"""

from tour_task_1 import Tour

"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
def printboard(board):
    """
    Functions loops through the board and prints it
    :param board:
    :return:prints the chess_object board
    :Complexity: B.C & W.C = O(n)
    """
    for i in range(len(board)):
        print(board[i])

def moved_position(already_moved, i, j):
    """
    Functions returns true if the
    :param already_moved:
    :param i:
    :param j:
    :return: True or False
    """
    for z in range(len(already_moved)):
        if already_moved[z] != [i, j]:
            return False
        else:
            return True

def Print_Menu():
    """
    Function shows the menu
    :return: the list
    :Complexity: O(1)
    """
    print("\nMenu: ")
    print("1. Quit")
    print("2. Position")

"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
The main does the following
The chess_object object points to the class Tour
Then prints the Menu
Then asks the user to enter their desired user_input
Then prints the chess_object board again until the user decides to quit
Complexity :BC & WC O(n^2)
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""

if __name__ == '__main__':

    chess_object = Tour()
    Print_Menu()

    quit = False
    while not quit:

        user_input = int(input("\nEnter user_input: "))
        if user_input == 1:
            quit = True
        if user_input == 2:
            # column
            current_column = chess_object.current_position[1]
            # row
            current_row = chess_object.current_position[1]
            chess_object.board[current_row][current_column] = 'K'

            l = 0
            m = 0
            while l < len(chess_object.board):
                while m < len(chess_object.board):
                    position_visited = moved_position(chess_object.already_moved, l, m)
                    if position_visited == True:
                        chess_object.board[l][m] = '*'
                    m = m + 1
                l = l + 1
            printboard(chess_object.board)

"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""