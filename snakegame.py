import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 400, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
green = (0, 128, 0)  # Change to green for background color
black = (0, 0, 0)    # Change to black for snake color
red = (255, 0, 0)    # Food color

# Snake properties
snake_size = 20
initial_speed = 10
speed_increment = 1

# Initialize snake
snake = [(width // 2, height // 2)]
snake_dir = (1, 0)

# Initialize food
food = (random.randrange(1, width // snake_size) * snake_size,
        random.randrange(1, height // snake_size) * snake_size)

# Game state
game_over = False
snake_speed = initial_speed

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                # Restart the game
                snake = [(width // 2, height // 2)]
                snake_dir = (1, 0)
                food = (random.randrange(1, width // snake_size) * snake_size,
                        random.randrange(1, height // snake_size) * snake_size)
                game_over = False
                snake_speed = initial_speed

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake_dir != (0, 1):
            snake_dir = (0, -1)
        if keys[pygame.K_DOWN] and snake_dir != (0, -1):
            snake_dir = (0, 1)
        if keys[pygame.K_LEFT] and snake_dir != (1, 0):
            snake_dir = (-1, 0)
        if keys[pygame.K_RIGHT] and snake_dir != (-1, 0):
            snake_dir = (1, 0)

        # Move the snake
        x, y = snake[0]
        x += snake_dir[0] * snake_size
        y += snake_dir[1] * snake_size
        snake.insert(0, (x, y))

        # Check if the snake eats the food
        if snake[0] == food:
            food = (random.randrange(1, width // snake_size) * snake_size,
                    random.randrange(1, height // snake_size) * snake_size)
            snake_speed += speed_increment  # Increase speed

        else:
            snake.pop()

        # Check if the snake collides with the walls or itself
        if (x < 0 or x >= width or y < 0 or y >= height or
                len(snake) != len(set(snake))):
            game_over = True

        # Draw the game window
        win.fill(green)  # Set background color
        pygame.draw.rect(win, red, (*food, snake_size, snake_size))

        for segment in snake:
            pygame.draw.rect(win, black, (*segment, snake_size, snake_size))

    else:
        # Game over screen
        font = pygame.font.Font(None, 36)
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        restart_text = font.render("Press SPACE to Restart", True, (255, 255, 255))
        win.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 20))
        win.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 20))

    pygame.display.flip()

    # Control the game speed
    pygame.time.Clock().tick(snake_speed)