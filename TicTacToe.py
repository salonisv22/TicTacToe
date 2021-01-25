import copy
SIZE_OF_BOARD=9


class TicTacToe:
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(["_"])
        self.no_moves_by_X=0
        self.no_moves_by_O=0


    def make_a_move(self,row,col,move_maker):
        if not self.game_over() and not self.is_win()[0]:
            if move_maker=="X":
                self.no_moves_by_X+=1
            elif move_maker=="O":
                self.no_moves_by_O+=1
            self.board[row][col]=[move_maker]

    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j],end="\t")
            print()

    def get_board(self):
        return copy.deepcopy(self.board)

    def correct_move(self,move_maker,row,col):

        if self.board[row][col]==["_"]:
            return True
        return False
        # correct = False
        # if move_maker not in ("X","O") or row not in (1,2,0) and col not in (1,2,0) or self.board[row][col]!=["_"]:
        #     return correct
        # temp_x = self.no_moves_by_X
        # temp_y = self.no_moves_by_O
        # if move_maker=="X":
        #     temp_x+=1
        # elif move_maker=="O":
        #     temp_y+=1
        # if abs(temp_x-temp_y) in (0,1):
        #     correct = True
        # return correct

    def is_win(self):
        for x in range(3):
            if ["_"]!=self.board[x][0]==self.board[x][1]==self.board[x][2]:
                return True,self.board[x][0]
            elif ["_"]!=self.board[0][x]==self.board[1][x]==self.board[2][x]:
                return True,self.board[0][x]
        if (["_"]!=self.board[0][0]==self.board[1][1]==self.board[2][2]
                or ["_"]!=self.board[0][2]==self.board[1][1]==self.board[2][0]):
            return True,self.board[1][1]
        return False,

    def game_over(self):
        if self.no_moves_by_O+self.no_moves_by_X==SIZE_OF_BOARD:
            return True
        return False





def main():
    my_board = TicTacToe()
    while not my_board.game_over():
        pos=input("make a move row col MOVE_MAKER").split()

        if my_board.correct_move(pos[2],int(pos[0]),int(pos[1])):
            my_board.make_a_move(pos[2],int(pos[0]),int(pos[1]))
        else:
            print("Wrong move")

        my_board.display()
        result= my_board.is_win()
        if result[0]:
            print("winner is",result[1])
            break

if __name__=="__main__":
    main()
    # my_board=TicTacToe()
    # my_board.display()
    # print(my_board.board)










