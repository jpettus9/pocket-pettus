pool_game.py:
```python
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define game constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 200, 20
BALL_RADIUS = 20

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define game classes
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 2
        self.vy = 2

    def move(self):
        # Update ball position
        self.x += self.vx
        self.y += self.vy

        # Collision with the edge of the pool table
        if self.x - BALL_RADIUS < 0:
            self.vx = -self.vx
        elif self.x + BALL_RADIUS > WIDTH:
            self.vx = -self.vx

        if self.y - BALL_RADIUS < 0:
            self.vy = -self.vy
        elif self.y + BALL_RADIUS > HEIGHT:
            self.vy = -self.vy

    def draw(self, screen):
        # Draw the ball on the screen
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), BALL_RADIUS)

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx):
        # Move the paddle
        self.x += dx

    def draw(self, screen):
        # Draw the paddle on the screen
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Create a ball and a paddle
ball = Ball(100, 100)
paddle = Paddle(100, 550)

# Game loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move(-5)
    if keys[pygame.K_RIGHT]:
        paddle.move(5)

    # Move the ball
    ball.move()

    # Draw everything
    screen.fill((100, 100, 100))
    paddle.draw(screen)
    ball.draw(screen)
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)
