import pygame.image
import pygame.transform

pygame.init()
pygame.key.start_text_input()

# Setting game window dimensions
# I probably need to use sys to figure out the screen dimensions to make this right on every device.
refactor = 0.65
window_width = 720*refactor
window_height = 1346*refactor
game_display = pygame.display.set_mode((window_width, window_height))

# Loading the image
#Credit: https://gamedevacademy.org/pygame-background-image-tutorial-complete-guide/#Implementing_Static_Background_Images
bg_image = pygame.image.load("Pictures/Bible Verse I want to display in an Android app.jpg")

#Credit: https://www.geeksforgeeks.org/how-to-rotate-and-scale-images-using-pygame/
bg_image = pygame.transform.scale(bg_image, (window_width, window_height))
# Main game loop
running = True
pygame.mixer.init()
pygame.mixer.music.load("Music/amazing_grace_sung_by_Elvis_Presly.mp3")
pygame.mixer.music.play()
restart = 123
pygame.mixer.music.set_endevent(pygame.QUIT)
show_text = False
#Credit: https://stackoverflow.com/questions/10077644/how-to-display-text-with-font-and-color-using-pygame
myfont = pygame.font.SysFont("monospace", 18)
text = myfont.render("Reminder: God is stronger than Satan!", 1, (64, 0, 128))
#hi
#import time
#time.sleep(57)
pygame.key.stop_text_input()
show_text_ticks = pygame.time.get_ticks()
num_taps = 0
while running:
    for event in pygame.event.get():
        if event.type == restart:
            num_taps = 0
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(pygame.QUIT)

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            num_taps = num_taps + 1
            if num_taps >= 5:
                pygame.mixer.music.set_endevent(restart)
            #Credit: https://stackoverflow.com/questions/70996802/pygame-pop-up-text-how-to-show-an-image-only-for-a-period-of-time
            show_text = True
            show_text_ticks = pygame.time.get_ticks()

    # Drawing image at position specified
    game_display.blit(bg_image, (0, 0))
    if pygame.time.get_ticks() - show_text_ticks > 2000:
        show_text = False
    if show_text:
        #Credit: https://stackoverflow.com/questions/10077644/how-to-display-text-with-font-and-color-using-pygame
        game_display.blit(text, (window_width*(1-0.9), window_height*(1-0.180)))
    pygame.display.update()
pygame.quit()