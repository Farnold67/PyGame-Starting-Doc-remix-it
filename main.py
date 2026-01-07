import pygame
import sys

# -----------------------
# 1️⃣ Settings
# -----------------------
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 67  # <-- Change this to set how many rows/columns

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# -----------------------
# 2️⃣ Initialize PyGame
# -----------------------
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Grid Example")
clock = pygame.time.Clock()

# -----------------------
# 3️⃣ Calculate cell size
# -----------------------
cell_width = WINDOW_WIDTH // GRID_SIZE
cell_height = WINDOW_HEIGHT // GRID_SIZE

# -----------------------
# 4️⃣ Main loop
# -----------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(WHITE)

    # Draw grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, GRAY, rect, 1)  # 1 pixel border

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()