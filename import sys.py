import sys
import pygame
def run_game():
    pygame.display.set_caption("Alien Invasion")
    # Set the background color.
    bg_color = (230, 230, 230)
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
    # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        run_game()