import sys
import random

###############################################################################
# The TicTacToe class starts and controlls a game of tic tac toe.

###############################################################################
class TicTacToe:
    # Initialize a new game state
    def __init__(self):
        self.grid = Grid()
        self.game_state = 0
        self.play_new_game()
    

    def play_new_game(self):
        player = input("Please enter X or O (X player would go first):")

        if(player == 'x' or player == 'X'):
            self.run(1)

        elif(player == 'o' or player == 'O'):
            self.run(0)

        else:
            print("Wrong input.")
            self.play_new_game()

    def run(self, player_first):
        while(self.grid.get_aval() > 0):
            self.grid.print_grid()
            if player_first%2 !=0:
                sel = self.get_user_input()
                self.grid.update_game(sel-1, 1)
                # self.grid.print_grid()

            else:
                print("Running MCTS...")
                ai = MonteCarlo(self.grid, 2)
                ai_sel = ai.selection()
                self.grid.update_game(ai_sel, 2)
                # self.grid.print_grid()

            player_first+=1        
            self.game_state = self.grid.check_game_state()
            if self.game_state != 0:
                self.end_game()



    
    def end_game(self):
        print('{:*^20}'.format(''))
        if self.game_state < 0:
            print('{:*^20}'.format('Draw!'))
        elif self.game_state == 1:
            #print(string.format('You Win!', fill='*', align='^', width=20))
            print('{:*^20}'.format('You Win!'))
        else:
            print('{:*^20}'.format('You Lose!'))
        print('{:*^20}'.format(''))


        value = input("Would you like to play another? Yes/No: ")
        if value.lower() == 'y' or value.lower == 'yes':
            TicTacToe()
        else:
            sys.exit(0)

    def get_user_input(self):
        while True:
            try:
                value=int(input("Please enter the space you want to pick: "))
                if value<1 or value > 9:
                    print("Please enter a number between 0 and 9")
                elif self.grid.get_value(value-1) > 0:
                    print("Please choose an available space")
                else:
                    return value
            except ValueError:
                print("This is not a whole number.")


###############################################################################
# The grid class keeps track and updates the a 3x3 tic tac toe game state

###############################################################################
class Grid:
    def __init__(self):
        self.grid = [0,0,0,0,0,0,0,0,0]
        self.aval = 9

    def available_spaces(self):
        space = []
        for i in range(9):
            if self.grid[i] == 0:
                space.append(i)
        return space

    def get_value(self, position):
        return self.grid[position]

    def get_aval(self):
        return self.aval

    def get_random_play(self):
        space = self.available_spaces()
        return space[random.randint(0, len(space)-1)]

    def update_game(self, position, player):
        self.grid[position] = player
        self.aval -= 1
    #This function checks if a player has won the game or the game results in a draw
    # Return Value: -1 if draw
    #               0 if not complete
    #               1 if player won
    #               2 if AI won
    def check_game_state(self):
        for i in range(0,3):
            # checking every row
            if self.grid[i*3] == self.grid[i*3+1] == self.grid[i*3+2] and self.grid[i*3] > 0:
                return self.grid[i*3]
            # checking every column
            elif self.grid[i] == self.grid[3 + i] == self.grid[6+i] and self.grid[i] > 0:
                return self.grid[i]
        
        # checking every diagonal
        if self.grid[0] == self.grid[4] == self.grid[8] and self.grid[0] > 0:
            return self.grid[0]
        elif self.grid[2] == self.grid[4] == self.grid[6] and self.grid[2] > 0:
            return self.grid[2]

        # if checked all conditions and no more available space. game is draw
        # else game is not complete
        if self.aval == 0:
            return -1
        else:
            return 0

    def print_grid(self):
        rowend = 1
        for i in range(0,9):

            if self.grid[i]==0:
                print('{:^5}'.format(i+1), end =" ")
            elif self.grid[i]==1:
                print('{:^5}'.format('X'), end =" ")
            elif self.grid[i]==2:
                print('{:^5}'.format('O'), end =" ")

            if rowend == 9:
                print()
                print('      |      |      ')

            elif rowend%3 == 0:
                print()
                print('______|______|______')
            else:
                print('|', end = '')
            rowend+=1

###############################################################################

###############################################################################

class MonteCarlo:
    def __init__(self, grid, player):
        self.grid = grid
        self.states = []
        self.max_moves = 2 ** grid.get_aval() 
        self.current_player = player
        self.tree = Tree(grid)

    def selection(self):
        return self.grid.get_random_play()
    
    def expansion(self):
        pass
    
    def simulation(self):
        pass

    def backpropogation(self):
        pass



###############################################################################

###############################################################################

class Node:
    childArray = []
    def __init__(self, grid, parent):
        self.parent = parent
        self.grid = grid

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.childArray

    def get_game(self):
        return self.grid

###############################################################################

###############################################################################
class Tree:
    def __init__(self, grid):
        self.root = Node(grid, None)

    def get_root(self):
        return self.root



if __name__ == "__main__":

    print("Welcome to a game of tic tac toe!")
    TicTacToe()