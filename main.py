import pygame
import sys

# -----------------------
# Settings
# -----------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

GRID_COLS = 16
GRID_ROWS = 12

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# -----------------------
# Initialize PyGame
# -----------------------
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Perfectly Centered Grid")
clock = pygame.time.Clock()

# -----------------------
# Calculate cell size to fit grid
# -----------------------
cell_width = WINDOW_WIDTH / GRID_COLS
cell_height = WINDOW_HEIGHT / GRID_ROWS

# Use the smaller to make square cells
cell_size = int(min(cell_width, cell_height))

# Total grid size in pixels
grid_width = cell_size * GRID_COLS
grid_height = cell_size * GRID_ROWS

# Offsets to center grid (round to int)
offset_x = (WINDOW_WIDTH - grid_width) // 2
offset_y = (WINDOW_HEIGHT - grid_height) // 2

# -----------------------
# Main loop
# -----------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw grid
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(
                offset_x + col * cell_size,
                offset_y + row * cell_size,
                cell_size,
                cell_size
            )
            pygame.draw.rect(screen, GRAY, rect, 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
