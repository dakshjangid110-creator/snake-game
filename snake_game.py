import tkinter as tk
import pygame
import random
import sys

# Constants for pygame window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


def run_snake_game():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 36)

    def draw_text(text, color, x, y):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

    def draw_snake(snake):
        for segment in snake:
            pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def random_food():
        return (
            random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        )

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = RIGHT
    food = random_food()
    score = 0

    running = True
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx * CELL_SIZE, head_y + dy * CELL_SIZE)

        # Check collisions
        if (
            new_head in snake or
            new_head[0] < 0 or new_head[0] >= WINDOW_WIDTH or
            new_head[1] < 0 or new_head[1] >= WINDOW_HEIGHT
        ):
            draw_text("Game Over", RED, WINDOW_WIDTH // 2 - 80, WINDOW_HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        snake.insert(0, new_head)

        # Check food
        if new_head == food:
            food = random_food()
            score += 1
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))
        draw_text(f"Score: {score}", WHITE, 10, 10)
        pygame.display.flip()


# --- Tkinter GUI for launching the game ---
def start_gui():
    root = tk.Tk()
    root.title("Snake Game Launcher")

    label = tk.Label(root, text="Welcome to Snake Game!", font=("Arial", 16))
    label.pack(pady=10)

    play_button = tk.Button(root, text="Play Game", font=("Arial", 14), command=lambda: [root.destroy(), run_snake_game()])
    play_button.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", font=("Arial", 14), command=root.quit)
    quit_button.pack(pady=10)

    root.mainloop()


# --- Start the application ---
if __name__ == "__main__":
    start_gui()
