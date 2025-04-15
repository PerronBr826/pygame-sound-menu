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
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Use constants from config

    pygame.display.set_caption(TITLE)
    return screen

def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    char_pose = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
    char_radius = 50

    def darken(color, dark):
        return (pygame.math.clamp(color[0] * dark, 0, 255),pygame.math.clamp(color[1] * dark, 0, 255),pygame.math.clamp(color[2] * dark, 0, 255),)

    buttons = [{"text" : "Play", "hover" : 0, "color" : (155,155,0)}, {"text" : "Awards", "hover" : 0, "color" : (155,155,0)}, {"text" : "Close", "hover" : 0, "color" : (155,55,50)}]

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
                    button_x = WINDOW_WIDTH // 2
                    button_y = 300 + (65 * button_i)
                    faux_buttonx = BUTTON_WIDTH + button["hover"]
                    faux_buttony = BUTTON_HEIGHT + button["hover"] / 2

                    button_box = pygame.Rect(button_x - faux_buttonx/ 2, button_y - faux_buttony/2, faux_buttonx, faux_buttony)

                    if button_box.collidepoint(event.pos):
                        button["hover"] = 0
                        if button["text"] == "Close":
                            running = False
                        else:
                            print(button["text"])


                    button_i += 1
            
        screen.fill(WHITE) # Use color from config

        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_i = 0

        for button in buttons:
            button_x = WINDOW_WIDTH // 2
            button_y = 300 + (65 * button_i)
            faux_buttonx = BUTTON_WIDTH + button["hover"]
            faux_buttony = BUTTON_HEIGHT + button["hover"] / 2

            button_box = pygame.Rect(button_x - faux_buttonx/ 2, button_y - faux_buttony/2, faux_buttonx, faux_buttony)



            if button_box.collidepoint(mouse_x, mouse_y):
                button_color = darken(button["color"], 0.5)
                button["hover"] = pygame.math.clamp((button["hover"] + 1) * 1.2, 0, 30)

            else:
                button_color = darken(button["color"], 0.6)
                button["hover"] = pygame.math.clamp((button["hover"] + 1) * 0.9, 0, 30)


            button_font = pygame.font.SysFont("Comic Sans MS", round(pygame.math.clamp((40 + button["hover"] * 0.8), 40, 76)))
            button_font2 = pygame.font.SysFont("Comic Sans MS", round(pygame.math.clamp((40 + button["hover"] * 0.4), 40, 76)))
                
            button_label = button_font.render(button["text"], True, darken(button["color"], 0.6))
            button_label2 = button_font2.render(button["text"], True, darken(button["color"], 0.6))

            faux_buttonx = BUTTON_WIDTH + button["hover"]
            faux_buttony = BUTTON_HEIGHT + button["hover"] / 2
            
            button_box.size = [faux_buttonx, faux_buttony]
            button_box.center = [button_x, button_y]

            text_rect = button_label.get_rect()
            text_rect.center = button_box.center

            text_rect2 = button_label2.get_rect()
            text_rect2.center = button_box.center


            pygame.draw.rect(screen, button_color, button_box)
            screen.blit(button_label, text_rect)
            screen.blit(button_label2, text_rect2)

            button_i += 1
     

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(FPS) # Use the clock to control the frame rate

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()