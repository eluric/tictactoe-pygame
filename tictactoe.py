import pygame

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
    num_rows: int, num_columns: int,
    x_boundaries: list[str], y_boundaries: list[str],
    state: list[list[str]], x_turn: bool
) -> bool:
    mouse_x, mouse_y = mouse_pos

    for i in range(num_rows):
        if mouse_y >= y_boundaries[i] and mouse_y < y_boundaries[i+1]:
            for j in range(num_columns):
                if mouse_x >= x_boundaries[j] and mouse_x < x_boundaries[j+1]:
                    if state[i][j] != "":
                        return
                    
                    if x_turn:
                        state[i][j] = "X"
                        return False, (i, j)
                    else:
                        state[i][j] = "O"
                        return True, (i, j)

def xo_coords(
    row: int, column: int,
    top_left_x: int, top_left_y: int,
    grid_line_length: int
) -> tuple:
    x = top_left_x + grid_line_length * column/3
    y = top_left_y + grid_line_length * row/3

    return x, y

# checks if either player has won
# returns a tuple of two booleans
# (x_wins, o_wins)
# if return value is (True, False), then x has won
def check_win(state: list[list[str]], last_move: tuple[int, int], num_rows: int, num_columns: int) -> tuple:
    # list of all the conditions where a player can win
    # win_conditions = [
    #     # horizontal wins
    #     [(0, 0), (0, 1), (0, 2)],
    #     [(1, 0), (1, 1), (1, 2)],
    #     [(2, 0), (2, 1), (2, 2)],

    #     # vertical wins
    #     [(0, 0), (1, 0)]
    # ]

    # only need to check the horizontal, vertical and diagonal of the last move
    # if no player has won until that point, then none of the previous moves were winning moves
    # therefore, if a player has won this round, then only the last move placed will result in a win
    if not last_move:
        return False, False

    row, column = last_move
    
    horizontal_win = True
    # first, check the row
    for i in range(num_columns - 1):
        if state[row][i] != state[row][i+1]:
            horizontal_win = False
            break
    
    if horizontal_win:
        if state[row][0] == "O":
            return False, True
        else:
            return True, False
    
    
    vertical_win = True
    # check column
    for i in range(num_rows - 1):
        if state[i][column] != state[i+1][column]:
            vertical_win = False
            break

    if vertical_win:
        if state[0][column] == "O":
            return False, True
        else:
            return True, False

    """
    If the row and column are the same, then we know that the last move placed was
    in range of the down diagonal and we need to check the down diagonal.
    e.g (0, 0), (1, 1), (2, 2)
    O| | 
    ------
     |O| 
    ------
     | |O

    If the row and column add up to to equal the total number of rows or total number of columns,
    then we know that the last move was in range of the up diagonal.
    e.g (3, 0), (2, 1), (0, 3). The total number of rows is 3.
     | |O
    ------
     |O| 
    ------
    O| |
    """
    down_diagonal_win = True
    if row == column:
        for i in range(num_rows - 1):
            if state[i][i] != state[i+1][i+1]:
                down_diagonal_win = False
                break

        if down_diagonal_win:
            if state[0][0] == "O":
                return False, True
            else:
                return True, False

    
    up_diagonal_win = True
    if row + column == num_rows:
        for i in range(num_rows - 1):
            if state[i][num_rows-i] != state[i+1][num_rows-i-1]:
                up_diagonal_win = False
                break
    
        if up_diagonal_win:
            if state[num_rows-1][0] == "O":
                return False, True
            else:
                return True, False

    return False, False

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

    num_rows = 3
    num_columns = 3

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

    state = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    x_turn = True
    x_wins = False
    o_wins = False
    last_move = ()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONUP:
                # mouse_x, mouse_y = pygame.mouse.get_pos()
                x_turn, last_move = check_click(
                    pygame.mouse.get_pos(), 
                    num_rows, num_columns, 
                    x_boundaries, y_boundaries, 
                    state, x_turn
                )
        
        # draw the grid lines for tic tac toe
        screen.blit(v_line, (v_line_x1, v_line_y1))
        screen.blit(v_line, (v_line_x2, v_line_y2))
        screen.blit(h_line, (h_line_x1, h_line_y1))
        screen.blit(h_line, (h_line_x2, h_line_y2))

        # draw the circles and crosses
        for i in range(num_rows):
            for j in range(num_columns):
                if state[i][j] == "":
                    continue

                if state[i][j] == "X":
                    screen.blit(cross_img, xo_coords(i, j, h_line_x1, v_line_y1, grid_line_length))
                
                else:
                    screen.blit(circle_img, xo_coords(i, j, h_line_x1, v_line_y1, grid_line_length))

        x_wins, o_wins = check_win(state, last_move, num_rows, num_columns)

        if x_wins:
            print("X wins!")
            return
        elif o_wins:
            print("O wins!")
            return

        pygame.display.update()
        clock.tick(60)

main()