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

    print(f"x: {h_line_x}, y: {h_line_y}")

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.blit(v_line, (v_line_x1, v_line_y1))
        screen.blit(v_line, (v_line_x2, v_line_y2))
        screen.blit(h_line, (h_line_x1, h_line_y1))
        screen.blit(h_line, (h_line_x2, h_line_y2))

        pygame.display.update()
        clock.tick(60)

main()