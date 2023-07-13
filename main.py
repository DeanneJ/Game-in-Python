import pygame
import time
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"),(WIDTH,HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 50)


# displaying the background image
def draw(player,elapsed_time,stars):
    WIN.blit(BG, (0, 0))  # co-ordinates- upper corner left

    pygame.draw.rect(WIN,"red",player)# drawing a rectangle as a player in red

    for star in stars:
        pygame.draw.rect(WIN,"white",star)# drawing a rectangle as a star in white
        

    pygame.display.update()

def main():
    run = True
    #moving characters
    player = pygame.Rect(200,HEIGHT - PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000 # first star will be add 2000ms
    star_count = 0 #when we should add another star

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)# delay the while loop - 60 times per sec (max)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

                star_add_increment = max(200, star_add_increment - 50) #generating another star
                star_count = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you press the x button
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL #moving them to the left
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL #moving to the right 

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):#checking whether the star is colliding with the player
                stars.remove(star)
                hit = True
                break  

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
    
        draw(player,elapsed_time,stars)

    pygame.quit()

if __name__ == "__main__":  # checking whether the file is directly running without importing
    main()
