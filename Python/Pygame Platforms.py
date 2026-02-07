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

platform_level = 600

done = False
while not done:
    screen.fill(black)

    # Checking what platform our character is above
    if y <= 50 and x > 175 and x < 225 + (screenSize[0]/8):
        platform_level = 50
    elif y <= 120 and x > 400 and x < 450 + (screenSize[0]/8):
        platform_level = 120
    elif y <= 250 and x > 100 and x < 150 + (screenSize[0]/8):
        platform_level = 250
    elif y <= 250 and x > 1150 and x < 1200 + (screenSize[0]/8):
        platform_level = 250
    elif y <= 350 and x > 550 and x < 600 + (screenSize[0]/8):
        platform_level = 350
    elif y <= 450 and x > 850 and x < 900 + (screenSize[0]/8):
        platform_level = 450
    else:
        platform_level = 600

    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()

    # Move right when right arrow is pressed
    if keys[pygame.K_RIGHT]:
        x += 10

    # Move left when left arrow is pressed
    if keys[pygame.K_LEFT]:
        x -= 10

    # Jumping
    if keys[pygame.K_UP] and y >= platform_level:
        velocity_Y = -21  # Initial upward force
        y = platform_level - 1           # Slight offset to trigger gravity logic

    # Apply gravity if player is in the air
    if y < platform_level:
        velocity_Y += 1   # Gravity acceleration
        y += velocity_Y  # Apply gravity
    if y >= platform_level:
        y = platform_level
        velocity_Y = 0         

    # Draw the player as a white square
    pygame.draw.rect(screen, white, [x, y, 50,50])

    # Draw the ground and platforms as red rectangles
    pygame.draw.rect(screen, red, [0, 650, screenSize[0], screenSize[1]-650])
    pygame.draw.rect(screen, red, [150, 300, screenSize[0]/8, 10])
    pygame.draw.rect(screen, red, [225, 100, screenSize[0]/8, 10])
    pygame.draw.rect(screen, red, [450, 170, screenSize[0]/8, 10])
    pygame.draw.rect(screen, red, [600, 400, screenSize[0]/8, 10])
    pygame.draw.rect(screen, red, [1200, 300, screenSize[0]/8, 10])
    pygame.draw.rect(screen, red, [900, 500, screenSize[0]/8, 10])

    # Limit the game to 100 frames per second
    clock.tick(100)

    # Update the display
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()



