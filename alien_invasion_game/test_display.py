import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Test Display")

# Load image
try:
    ship_image = pygame.image.load('images/ship.bmp')
    print(f"Image loaded successfully: {ship_image.get_size()}")
except Exception as e:
    print(f"Error loading image: {e}")
    sys.exit()

# Get rects
screen_rect = screen.get_rect()
ship_rect = ship_image.get_rect()
ship_rect.midbottom = screen_rect.midbottom

print(f"Screen size: {screen.get_size()}")
print(f"Ship position: {ship_rect}")

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw
    screen.fill((230, 230, 230))
    screen.blit(ship_image, ship_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Program ended normally")
