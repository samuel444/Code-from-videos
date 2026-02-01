import pygame
pygame.init() 

windowSize = pygame.FULLSCREEN

# Clock object to control the frame rate
clock = pygame.time.Clock()

screen = pygame.display.set_mode((0,0), windowSize)

# Store the screen dimensions
screenSize = (screen.get_size())

# Vertical velocity for gravity / jumping
velocity_Y = 0

# Define Colors
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')
red = pygame.color.Color("#FF0000")

# Initial player position
y = 100
x = 300

done = False
while not done:
    screen.fill(black)

    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()

    # Move right when right arrow is pressed
    if keys[pygame.K_RIGHT]:
        x += 20

    # Move left when left arrow is pressed
    if keys[pygame.K_LEFT]:
        x -= 20

    # Jumping
    if keys[pygame.K_UP] and y >= 600:
        velocity_Y = -30  # Initial upward force
        y = 599           # Slight offset to trigger gravity logic

    # Apply gravity if player is in the air
    if y < 600:
        velocity_Y += 1   # Gravity acceleration
        y += velocity_Y  # Apply gravity
    else:
        y = 600           # Snap player to ground level

    # Draw the player as a white square
    pygame.draw.rect(screen, white, [x, y, 50,50])

    # Draw the ground as a red rectangle
    pygame.draw.rect(screen, red, [0, 650, screenSize[0], screenSize[1]-650])

    # Limit the game to 100 frames per second
    clock.tick(100)

    # Update the display
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
