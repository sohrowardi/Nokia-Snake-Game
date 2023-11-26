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
black = (0, 0, 0)
green = (0, 255, 0)  # Snake color
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
        win.fill(black)
        pygame.draw.rect(win, red, (*food, snake_size, snake_size))

        for segment in snake:
            pygame.draw.rect(win, green, (*segment, snake_size, snake_size))
            pygame.draw.rect(win, (0, 100, 0), (*segment, snake_size, snake_size), 3)  # Add border

    else:
        # Game over screen
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over - Press SPACE to Restart", True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        win.blit(text, text_rect)

    pygame.display.flip()

    # Control the game speed
    pygame.time.Clock().tick(snake_speed)
