"""
K. Sharsindra Pratheen
Computer Science, Monash University
"""

from tour_task_2 import Tour

"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
def search_moved_pos(moved_position, i, j):
    """
    Function Searches moved position
    :param moved_position:
    :param i:
    :param j:
    :return: True if position already moved, else False
    @complexity best case: O(1)
    @complexity worst case: O(N)
    """
    for z in range(len(moved_position)):
        if moved_position[z] == [i, j]:
            return True
        else:
            return False

def print_menu():
    """
    Function prints the menu
    :return: prints menu
    :Complexity: Best Case & Worst Case O(1) l.e Constant time
    """
    print("1. Start")
    print("2. Exit")


def print_board(board):
    """
    Function prints the chess_object board
    :param board:
    :return: board printed row by row
    @post
    @complexity: O(N)
    """
    for i in range(len(board)):
        print(board[i])

def clear_board(board):
    """
    :param board:
    @post board gets cleared
    @complexity O(N^2)
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'O':
                board[i][j] = 'O'

"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
if __name__ == '__main__':
    """
    Main function prints board after every move
    user then inputs row user_input
    the respective user_input is executed
    """

    chess_object = Tour()
    print_menu()
    user = int(input("\nEnter your option: "))
    quit = False
    while not quit:
        if user == 2:
            quit = True

        if user == 1:

            clear_board(chess_object.board)

            # try and except for the column
            t_r_y = False
            column = -1
            row = -1
            while t_r_y == False:
                try:
                    column = int(input("column: "))
                    row = int(input("Row: "))
                    if column <= 7 and column >= 0 and row <= 7 and row >= 0:
                        t_r_y = True
                    else:
                        print("Enter row value within the range (0-7)")
                except ValueError:
                    print("Error")
            chess_object.current_position[1] = column
            chess_object.current_position[0] = row

            chess_object.board[chess_object.current_position[0]][chess_object.current_position[1]] = 'K'
            print_board(chess_object.board)
            chess_object.board[chess_object.current_position[0]][chess_object.current_position[1]] = '*'


            while not quit:
                chess_object.next_moves()
                print("\nPossible moves: ")
                if chess_object.move_1 != False:
                    print("1. Left Left Down")
                if chess_object.move_2 != False:
                    print("2. Left Left Up")
                if chess_object.move_3 != False:
                    print("3. Right Right Up")
                if chess_object.move_4 != False:
                    print("4. Right Right Down")
                if chess_object.move_5 != False:
                    print("5. Down Down Right")
                if chess_object.move_6 != False:
                    print("6. Down Down Left")
                if chess_object.move_7 != False:
                    print("7. Up Up Left")
                if chess_object.move_8 != False:
                    print("8. Up Up Right")
                print("9. Exit")


                user_input = int(input("\nEnter Your Next move: "))

                if user_input == 9:
                    quit = True
                if user_input == 1:
                    if (chess_object.current_position[0] + 1) <= 7:
                        chess_object.current_position[0] += 1
                        if (chess_object.current_position[1] - 2) >= 0:
                            chess_object.current_position[1] -= 2
                    else:
                        print("Invalid move,Try Again")

                if user_input == 2:
                    if (chess_object.current_position[0] - 1) >= 0:
                        chess_object.current_position[0] -= 1
                        if(chess_object.current_position[1] - 2) >= 0:
                            chess_object.current_position[1] -= 2
                    else:
                        print("Invalid move")

                if user_input == 3:
                    if (chess_object.current_position[0] - 1) >= 0 and (chess_object.current_position[1] + 2) <= 7:
                        chess_object.current_position[0] -= 1
                        chess_object.current_position[1] += 2
                    else:
                        print("Invalid move,Try Again")

                if user_input == 4:
                    if (chess_object.current_position[0] + 1) <= 7 and (chess_object.current_position[1] + 2) <= 7:
                        chess_object.current_position[0] += 1
                        chess_object.current_position[1] += 2
                    else:
                        print("Invalid move,Try Again")

                if user_input == 5:
                    if (chess_object.current_position[0] + 2) <= 7:
                        chess_object.current_position[0] += 2
                        if (chess_object.current_position[1] + 1) <= 7:
                            chess_object.current_position[1] += 1
                    else:
                        print("Invalid move,Try Again")

                if user_input == 6:
                    if (chess_object.current_position[0] + 2) <= 7:
                        chess_object.current_position[0] += 2
                        if (chess_object.current_position[1] - 1) >= 0:
                            chess_object.current_position[1] -= 1
                    else:
                        print("Invalid move,Try Again")

                if user_input == 7:
                    if (chess_object.current_position[0] - 2) >= 0:
                        chess_object.current_position[0] -= 2
                        if (chess_object.current_position[1] - 1) >= 0:
                            chess_object.current_position[1] -= 1
                    else:
                        print("Invalid move,Try Again")

                if user_input == 8:
                    if (chess_object.current_position[0] - 2) >= 0:
                        chess_object.current_position[0] -= 2
                        if (chess_object.current_position[1] + 1) <= 7:
                            chess_object.current_position[1] += 1
                    else:
                        print("Invalid move,Try Again")

                #Printing * in the previous K position
                chess_object.moved_position.append(chess_object.current_position)
                chess_object.board[chess_object.current_position[0]][chess_object.current_position[1]] = '*'
                # Printing K in the current position
                chess_object.board[chess_object.current_position[0]][chess_object.current_position[1]] = 'K'
                print_board(chess_object.board)


"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""