import pygame, socket, json

# Initialize Pygame
pygame.init()

# Set up the display window
width, height = 1920/4*3, 1080/4*3
winow = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("xyaros")

# Set up a clock to limit the frame rate
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load("img/face.png"), (100,100))
        facing = 1
        touching_ground = True

    def update(self):
        pass

    def draw(self):
        winow.blit(self.img, (self.x, self.y))

player = Player(500,500)
to_draw = [player]

# Main game loop
run = True 
while run:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the screen
    pygame.display.update()
    for entity in to_draw:
        entity.draw()


    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Clean up Pygame
pygame.quit()

