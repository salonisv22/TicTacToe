import pygame

from TicTacToe import TicTacToe
cell_size = 200
pygame.init()
OPEN_SANS = "OpenSans-Regular.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 40)
BOMB = pygame.image.load("mine.png")
BOMB = pygame.transform.scale(BOMB, (cell_size, cell_size))
FLAG = pygame.image.load("flag.png")
FLAG = pygame.transform.scale(FLAG, (cell_size, cell_size))


class TicTacToeUI:
    def __init__(self,board:TicTacToe):
        self.board=board
        self.screen = pygame.display.set_mode((600,700))
        pygame.display.set_caption("Tic Tac Toe")
        self.whose_turn="X"


    def display_Turn(self):
        message = smallFont.render("Player "+self.whose_turn, True, (0,0,0))
        self.screen.blit(message,(180,40))

    def make_board(self):
        self.screen.fill((150, 150, 150))
        self.reset_button()
        heading = smallFont.render("Tic Tac Toe", True, (0, 0, 0))
        self.screen.blit(heading, (180, 0))
        self.display_Turn()
        for i in range(3):
            for j in range(3):
                rect = pygame.Rect(  j * cell_size, 100+i * cell_size,cell_size, cell_size)
                pygame.draw.rect(self.screen, (200,200,200), rect)
                pygame.draw.rect(self.screen, (0,0,0), rect, 3)

                if self.board.get_board()[i][j]==['X']:
                    self.screen.blit(BOMB,rect)
                elif self.board.get_board()[i][j]==['O']:
                    self.screen.blit(FLAG, rect)

    # def make_the_board(self):
    #     # making horizontal line
    #     pygame.draw.line(self.screen,(200,200,200),(0,300),(600,300),10)
    #     pygame.draw.line(self.screen,(200,200,200),(0,500),(600,500),10)
    #     # making vertical line
    #     pygame.draw.line(self.screen, (200, 200, 200), (200, 100), (200, 700),10)
    #     pygame.draw.line(self.screen, (200, 200, 200), (400, 100), (400, 700),10)

    def make_the_move(self,pos):

        (x, y) = pos
        if not self.board.correct_move(self.whose_turn,(y-100)//200,x//200):
            return

        # print("x",x,"y",y)
        self.board.make_a_move((y-100)//200,x//200,self.whose_turn)
        # self.screen.blit(BOMB,)
        print(self.board.get_board())
        temp=self.board.is_win()
        iswon_whowon = self.board.is_win()
        if iswon_whowon[0]:
            self.whose_turn=iswon_whowon[1][0]+" Won"
        elif self.board.game_over():
            self.whose_turn = " Game Over"
        elif self.whose_turn == "X":
            self.whose_turn = "O"
        else:
            self.whose_turn = "X"

    def reset_button(self):
        resetButton = pygame.Rect(450,40,130,50)
        buttonText = smallFont.render("Reset", True, (0,0,0))
        buttonRect = buttonText.get_rect()
        buttonRect.center = resetButton.center
        pygame.draw.rect(self.screen, (255,255,255), resetButton)
        self.screen.blit(buttonText, buttonRect)
        mouse = pygame.mouse.get_pos()
        if resetButton.collidepoint(*mouse) and pygame.mouse.get_pressed(3)[0]:
            self.board.__init__()


def main():
    running = True
    board = TicTacToe()
    my_board = TicTacToeUI(board)
    whose_turn="X"
    while running:
        my_board.make_board()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                my_board.make_the_move(mouse)





main()