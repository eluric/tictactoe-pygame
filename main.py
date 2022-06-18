import pygame
from TicTacToe import TicTacToe
from Player import AI

def v_line_coords(
    line_num: int,
    screen_width: int, screen_height: int,
    grid_line_length: int
) -> tuple:
    v_line_x = (screen_width - grid_line_length)/2 + grid_line_length * line_num/3
    v_line_y = (screen_height - grid_line_length)/2

    return v_line_x, v_line_y

def h_line_coords(
    line_num: int,
    screen_width: int, screen_height: int,
    grid_line_length: int
) -> tuple:
    h_line_x = (screen_width - grid_line_length)/2
    h_line_y = (screen_height - grid_line_length)/2 + grid_line_length * line_num/3

    return h_line_x, h_line_y

# checks if the player is clicking in a grid and which grid they're clicking on
def check_click(
    mouse_pos: tuple, 
    size: int,
    x_boundaries: list[str], y_boundaries: list[str]
) -> tuple[int, int]:
    mouse_x, mouse_y = mouse_pos

    for i in range(size):
        if mouse_y >= y_boundaries[i] and mouse_y < y_boundaries[i+1]:
            for j in range(size):
                if mouse_x >= x_boundaries[j] and mouse_x < x_boundaries[j+1]:
                    # if state[i][j] != " ":
                    #     return
                    
                    # if x_turn:
                    #     state[i][j] = "X"
                    #     return (i, j)
                    # else:
                    #     state[i][j] = "O"
                    #     return (i, j)

                    return (i, j)
    
    return (-1, -1)

def xo_coords(
    row: int, column: int,
    top_left_x: int, top_left_y: int,
    grid_line_length: int
) -> tuple:
    x = top_left_x + grid_line_length * column/3
    y = top_left_y + grid_line_length * row/3

    return x, y

def main():
    pygame.init()
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()

    circle_img = pygame.image.load("circle.png")
    cross_img = pygame.image.load("cross.png")

    # scale images
    circle_img = pygame.transform.scale(circle_img, (240, 240))
    cross_img = pygame.transform.scale(cross_img, (240, 240))

    grid_line_length = 720
    grid_line_width = 5

    size = 3

    v_line = pygame.Surface((grid_line_width, grid_line_length))
    v_line.fill("White")

    h_line = pygame.Surface((grid_line_length, grid_line_width))
    h_line.fill("White")

    v_line_x1, v_line_y1 = v_line_coords(1, screen_width, screen_height, grid_line_length)
    v_line_x2, v_line_y2 = v_line_coords(2, screen_width, screen_height, grid_line_length)

    h_line_x1, h_line_y1 = h_line_coords(1, screen_width, screen_height, grid_line_length)
    h_line_x2, h_line_y2 = h_line_coords(2, screen_width, screen_height, grid_line_length)

    y_boundaries = [
        v_line_y1 + grid_line_length * i/3 for i in range(4)
    ]
    x_boundaries = [
        h_line_x1 + grid_line_length * i/3 for i in range(4)
    ]

    ttt = TicTacToe(size, True)
    x_wins = False
    o_wins = False
    game_over = False

    ai = AI()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                return
            
            if game_over:
                break

            elif event.type == pygame.MOUSEBUTTONUP:
                if not ttt.is_x_turn():
                    break

                row, column = check_click(
                    pygame.mouse.get_pos(),
                    size, x_boundaries, y_boundaries
                )

                ttt.make_move(row, column)
                x_wins, o_wins = ttt.check_win()

                if x_wins and o_wins:
                    pygame.display.set_caption("Draw")
                    game_over = True
                elif x_wins:
                    pygame.display.set_caption("X wins!")
                    game_over = True
                elif o_wins:
                    pygame.display.set_caption("O wins!")
                    game_over = True

        if not ttt.is_x_turn():
            row, column = ai.make_best_move(ttt)
            ttt.make_move(row, column)
            x_wins, o_wins = ttt.check_win()

            if x_wins and o_wins:
                pygame.display.set_caption("Draw")
                game_over = True
            elif x_wins:
                pygame.display.set_caption("X wins!")
                game_over = True
            elif o_wins:
                pygame.display.set_caption("O wins!")
                game_over = True

        # draw the grid lines for tic tac toe
        screen.blit(v_line, (v_line_x1, v_line_y1))
        screen.blit(v_line, (v_line_x2, v_line_y2))
        screen.blit(h_line, (h_line_x1, h_line_y1))
        screen.blit(h_line, (h_line_x2, h_line_y2))

        state = ttt.get_state()

        for i in range(size):
            for j in range(size):
                if state[i][j] == "X":
                    screen.blit(cross_img, xo_coords(i, j, h_line_x1, v_line_y1, grid_line_length))
                
                elif state[i][j] == "O":
                    screen.blit(circle_img, xo_coords(i, j, h_line_x1, v_line_y1, grid_line_length))

        pygame.display.update()
        clock.tick(60)

main()