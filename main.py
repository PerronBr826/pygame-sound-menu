# Pygame game template

import pygame
import sys
import random
import draw # Import the drawing module

# Color constants (RGB)
WHITE = (200, 200, 200)
BLACK = (28, 28, 28)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)

# Game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Menu Button Dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

# Game window title
TITLE = "Pygame Template"

# Frame rate (frames per second)
FPS = 60

def init_game ():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config

    pygame.display.set_caption(TITLE)
    return screen

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    char_pose = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
    char_radius = 50

    sound1 = pygame.mixer.Sound("Sounds/Coins.ogg")
    sound2 = pygame.mixer.Sound("Sounds/WindowBreak.ogg")
    gameover = pygame.mixer.Sound("Sounds/GameOver.ogg")
    scream = pygame.mixer.Sound("Sounds/ScreamMale.ogg")

    def darken(color, dark):
        return [pygame.math.clamp(color[0] * dark, 0, 255),pygame.math.clamp(color[1] * dark, 0, 255),pygame.math.clamp(color[2] * dark, 0, 255),]

    buttons = [{"text" : "Play Sound", "hover" : 0, "color" : (155,155,0), "purpose" : "sound1"}, {"text" : "Play Sound 2", "hover" : 0, "color" : (155,155,0), "purpose" : "sound2"}, {"text" : "Close", "hover" : 0, "color" : (155,55,50), "purpose" : "close"},
               {"text" : "Close", "hover" : 0, "color" : (155,55,50), "purpose" : "close"},
               ]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button_i = 0
                for button in buttons:
                    button_x = BUTTON_WIDTH/2 + 30
                    button_y = 40 + (65 * button_i)
                    faux_buttonx = BUTTON_WIDTH + button["hover"]
                    faux_buttony = BUTTON_HEIGHT + button["hover"] / 2

                    button_box = pygame.Rect(button_x - faux_buttonx/ 2, button_y - faux_buttony/2, faux_buttonx, faux_buttony)

                    if button_box.collidepoint(event.pos):
                        button["hover"] = 0
                        if button["purpose"] == "close":
                            scream.set_volume(1)
                            scream.play()
                            running = False
                        elif button["purpose"] == "sound1":
                            sound1.play()
                        elif button["purpose"] == "sound2":
                            sound2.play()

                        print(button["text"])


                    button_i += 1
            
        screen.fill(WHITE) # Use color from config

        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_i = 0

        for button in buttons:
            button_x = BUTTON_WIDTH/2 + 30
            button_y = 40 + (65 * button_i)

            faux_buttonx = BUTTON_WIDTH + button["hover"]
            faux_buttony = BUTTON_HEIGHT + button["hover"] / 2

            original_color = button["color"]

            button_box = pygame.Rect(button_x - faux_buttonx/ 2, button_y - faux_buttony/2, faux_buttonx, faux_buttony)



            if button_box.collidepoint(mouse_x, mouse_y):
                button_color = darken(button["color"], 0.5)
                button["hover"] = pygame.math.clamp((button["hover"] + 1) * 1.2, 0, 30)

            else:
                button_color = darken(button["color"], 0.6)
                button["hover"] = pygame.math.clamp((button["hover"] + 1) * 0.9, 0, 30)


            button_font = pygame.font.SysFont("Comic Sans MS", round(pygame.math.clamp((20 + button["hover"] * 0.9), 40, 76)))
            button_font2 = pygame.font.SysFont("Comic Sans MS", round(pygame.math.clamp((20 + button["hover"] * 0.7), 40, 76)))
                
            button_label = button_font.render(button["text"], True, darken(button_color, 0.8))
            button_label2 = button_font2.render(button["text"], True, darken(button_color, 0.5))

            faux_buttonx = BUTTON_WIDTH + button["hover"]
            faux_buttony = BUTTON_HEIGHT + button["hover"] / 2
            
            button_box.size = [faux_buttonx, faux_buttony]
            button_box.center = [button_x, button_y]

            text_rect = button_label.get_rect()
            text_rect.center = button_box.center

            text_rect2 = button_label2.get_rect()
            text_rect2.center = button_box.center


            pygame.draw.rect(screen, original_color, button_box)
            screen.blit(button_label2, text_rect2)
            screen.blit(button_label, text_rect)

            button_i += 1
     

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(FPS) # Use the clock to control the frame rate

    pygame.time.delay(560)
    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()