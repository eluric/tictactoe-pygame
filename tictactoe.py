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

    # describes the coordinates at the top left of each of the grid squares
    # grid_pos = [
    #     [(j, i) for i in range(4) for j in range(k, k+1)] for k in range(4)
    # ]

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                done = False
                for i in range(num_rows):
                    if mouse_y >= y_boundaries[i] and mouse_y < y_boundaries[i+1]:
                        for j in range(num_columns):
                            if mouse_x >= x_boundaries[j] and mouse_x < x_boundaries[j+1]:
                                if state[i][j] != "":
                                    done = True
                                    break
                                
                                if x_turn:
                                    state[i][j] = "X"
                                    x_turn = False
                                else:
                                    state[i][j] = "O"
                                    x_turn = True

                                done = True

                                print(state)
                        
                        if done:
                            break
        
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

        pygame.display.update()
        clock.tick(60)

main()