import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 600
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Puzzle Game")

# Set up the puzzle pieces
piece_size = WIDTH // 3
pieces = []
solved_pieces = []
for i in range(3):
    for j in range(3):
        x = j * piece_size
        y = i * piece_size
        piece = pygame.Rect(x, y, piece_size, piece_size)
        pieces.append(piece)
        solved_pieces.append(piece)

# Shuffle the pieces
random.shuffle(pieces)

# Load and split the image
image = pygame.image.load("D:\puzzlegame\marguerite-729510_1280.jpg")
image = pygame.transform.scale(image, (WIDTH, HEIGHT))
image_pieces = []
for i in range(3):
    for j in range(3):
        x = j * piece_size
        y = i * piece_size
        piece = pygame.Surface((piece_size, piece_size))
        piece.blit(image, (0, 0), (x, y, piece_size, piece_size))
        image_pieces.append(piece)

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                for i, piece in enumerate(pieces):
                    if piece.collidepoint(pos):
                        # Check if the clicked piece can move
                        if (
                            i % 3 != 0 and pieces[i - 1] == solved_pieces[i - 1] or
                            i % 3 != 2 and pieces[i + 1] == solved_pieces[i + 1] or
                            i // 3 != 0 and pieces[i - 3] == solved_pieces[i - 3] or
                            i // 3 != 2 and pieces[i + 3] == solved_pieces[i + 3]
                        ):
                            # Swap the clicked piece with the empty piece
                            pieces[i], pieces[solved_pieces.index(None)] = pieces[solved_pieces.index(None)], pieces[i]

    # Update the game state

    # Draw the game
    win.fill((255, 255, 255))  # White background
    for i, piece in enumerate(pieces):
        if piece != solved_pieces[i]:
            win.blit(image_pieces[i], piece)
        pygame.draw.rect(win, (0, 0, 0), piece, 1)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
