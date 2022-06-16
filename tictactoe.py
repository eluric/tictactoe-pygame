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

def main():
    pygame.init()
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()

    grid_line_length = 720
    grid_line_width = 5

    
    v_line = pygame.Surface((grid_line_width, grid_line_length))
    v_line.fill("White")

    h_line = pygame.Surface((grid_line_length, grid_line_width))
    h_line.fill("White")

    v_line_x1, v_line_y1 = v_line_coords(1, screen_width, screen_height, grid_line_length)
    v_line_x2, v_line_y2 = v_line_coords(2, screen_width, screen_height, grid_line_length)

    h_line_x1, h_line_y1 = h_line_coords(1, screen_width, screen_height, grid_line_length)
    h_line_x2, h_line_y2 = h_line_coords(2, screen_width, screen_height, grid_line_length)

    # describes the coordinates at the top left of each of the grid squares
    grid_pos = [
        [(i, j) for i in range(4) for j in range(k, k+1)] for k in range(4)
    ]

    y_boundaries = [
        v_line_y1 + grid_line_length * i/3 for i in range(4)
    ]

    x_boundaries = [
        h_line_x1 + grid_line_length * i/3 for i in range(4)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.blit(v_line, (v_line_x1, v_line_y1))
        screen.blit(v_line, (v_line_x2, v_line_y2))
        screen.blit(h_line, (h_line_x1, h_line_y1))
        screen.blit(h_line, (h_line_x2, h_line_y2))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for i in range(3):
            if mouse_y >= y_boundaries[i] and mouse_y < y_boundaries[i+1]:
                for j in range(3):
                    if mouse_x >= x_boundaries[j] and mouse_x < x_boundaries[j+1]:
                        print(grid_pos[i][j])

        pygame.display.update()
        clock.tick(60)

main()