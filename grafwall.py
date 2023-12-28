import pygame
import random
import math

# Function to create a spray effect
def spray_effect(screen, color, position, size):
    for _ in range(size * 2):  # Number of dots
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0, size)
        x = position[0] + int(radius * math.cos(angle))
        y = position[1] + int(radius * math.sin(angle))
        pygame.draw.circle(screen, color, (x, y), 1)  # Draw small dot

# Initialize Pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

# Default brush settings
brush_color = (0, 0, 0)  # Default color: black
brush_size = 5  # Default brush size

# Variables for gradient effect
gradient = False
color_change_rate = [1, 1, 1]  # Change rate for RGB

# List to store drawing positions
drawings = []

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change brush color with keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                brush_color = (255, 0, 0)  # Red
            elif event.key == pygame.K_g:
                brush_color = (0, 255, 0)  # Green
            elif event.key == pygame.K_b:
                gradient = not gradient  # Toggle gradient effect
            # Add more colors as needed

            # Change brush size with keyboard
            if event.key == pygame.K_1:
                brush_size = 5
            elif event.key == pygame.K_2:
                brush_size = 10
            # Add more sizes as needed

    # Fill the background with white
    screen.fill((255, 255, 255))

    # If left mouse button is pressed, add the position to the drawings list
    if pygame.mouse.get_pressed()[0]: 
        mouse_pos = pygame.mouse.get_pos()
        if gradient:
            brush_color = tuple(min(max(c + rate, 0), 255) for c, rate in zip(brush_color, color_change_rate))
        spray_effect(screen, brush_color, mouse_pos, brush_size)  # Use spray effect
        # Store the drawing information
        drawings.append((brush_color, mouse_pos, brush_size))

    # Draw all circles in the drawings list
    for color, pos, size in drawings:
        pygame.draw.circle(screen, color, pos, size)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
