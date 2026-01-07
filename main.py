import pygame
import sys
import random
import math
import time

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
FLASH_TIME = 20  # milliseconds

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blue Square Game with Instant Red Flash")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

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
# Game state
# -----------------------
current_square = (random.randint(0, GRID_ROWS - 1), random.randint(0, GRID_COLS - 1))
red_squares = []  # list of red squares flashing
flash_end_times = {}  # when each red square stops flashing
SC = 0  # correct clicks
SI = 0  # incorrect clicks
start_time = time.time()  # game start

# -----------------------
# Helper function
# -----------------------
def draw_grid():
    screen.fill(WHITE)
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(
                offset_x + col * cell_size,
                offset_y + row * cell_size,
                cell_size,
                cell_size
            )
            color = BLUE if (row, col) == current_square else WHITE
            if (row, col) in red_squares:
                color = RED
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 2)  # grid lines

    # Draw score
    elapsed = max(time.time() - start_time, 0.001)
    grid_size = GRID_COLS  # N*N
    bps = max(0, SC - SI) * math.log2(grid_size) / elapsed
    score_text = font.render(f"SC: {SC}  SI: {SI}  BPS: {bps:.2f}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

# -----------------------
# Main loop
# -----------------------
running = True
while running:
    now = pygame.time.get_ticks()

    # Remove red squares whose flash time ended
    for square in list(flash_end_times.keys()):
        if now > flash_end_times[square]:
            red_squares.remove(square)
            del flash_end_times[square]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            col = (mouse_x - offset_x) // cell_size
            row = (mouse_y - offset_y) // cell_size
            clicked_square = (row, col)

            if clicked_square == current_square:
                SC += 1
                current_square = (random.randint(0, GRID_ROWS - 1), random.randint(0, GRID_COLS - 1))
            else:
                SI += 1
                # Add red square to flash
                red_squares.append(clicked_square)
                flash_end_times[clicked_square] = now + FLASH_TIME

    draw_grid()
    clock.tick(60)

pygame.quit()
sys.exit()
