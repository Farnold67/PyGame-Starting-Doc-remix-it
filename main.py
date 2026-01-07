import pygame
import sys
import random

# -----------------------
# Settings
# -----------------------
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

GRID_COLS = 25
GRID_ROWS = 25

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FLASH_TIME = 300  # milliseconds

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Click the Blue Square (Red Flash)")
clock = pygame.time.Clock()

# -----------------------
# Calculate cell size and offsets
# -----------------------
cell_width = WINDOW_WIDTH // GRID_COLS
cell_height = WINDOW_HEIGHT // GRID_ROWS
cell_size = min(cell_width, cell_height)

grid_width = cell_size * GRID_COLS
grid_height = cell_size * GRID_ROWS

offset_x = (WINDOW_WIDTH - grid_width) // 2
offset_y = (WINDOW_HEIGHT - grid_height) // 2

# -----------------------
# Helper function
# -----------------------
def draw_grid(blue_square, red_square=None):
    screen.fill(WHITE)
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(
                offset_x + col * cell_size,
                offset_y + row * cell_size,
                cell_size,
                cell_size
            )
            if (row, col) == blue_square:
                color = BLUE
            elif red_square and (row, col) == red_square:
                color = RED
            else:
                color = WHITE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 2)  # grid lines
    pygame.display.flip()

# -----------------------
# Game state
# -----------------------
current_square = (random.randint(0, GRID_ROWS - 1), random.randint(0, GRID_COLS - 1))
draw_grid(current_square)  # initial blue square

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col = (mouse_x - offset_x) // cell_size
            row = (mouse_y - offset_y) // cell_size
            clicked_square = (row, col)

            if clicked_square == current_square:
                # Correct → pick new blue square
                current_square = (random.randint(0, GRID_ROWS - 1), random.randint(0, GRID_COLS - 1))
                draw_grid(current_square)
            else:
                # Wrong → flash red square while keeping blue
                draw_grid(current_square, red_square=clicked_square)
                pygame.time.delay(FLASH_TIME)
                draw_grid(current_square)

    clock.tick(60)

pygame.quit()
sys.exit()
