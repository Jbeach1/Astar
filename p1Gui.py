import pygame

class Gui:


    def run_it(self, path, start, end):
        pygame.init()
    # COLORS
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
    # DIMENSIONS / DISPLAY SCREEN
        width = 1000
        height = 500
        screen_display = pygame.display.set_mode((width, height))  # W , H
        screen_display.fill(white)
    # START AND GOAL GUI
        font = pygame.font.Font('freesansbold.ttf', 32)
        start_text = font.render('S', True, green, white)
        goal_text = font.render('G', True, green, white)
        start_box = start_text.get_rect()
        goal_box = goal_text.get_rect()

        start_box.center = start
        pygame.draw.circle(screen_display, black, start, 4)
        goal_box.center = end
        pygame.draw.circle(screen_display, black, end, 4)


        screen_display.blit(start_text, start_box)
        screen_display.blit(goal_text, goal_box)
    #SHAPES
        rectangle1 = pygame.draw.polygon(screen_display, black, ((230, 360), (550, 360), (550, 480), (230, 480)), 2)
        triangle1 = pygame.draw.polygon(screen_display, black, ((450, 125), (480, 300), (400, 300)), 2)
        pentagon = pygame.draw.polygon(screen_display, black, ((218, 130), (230, 260), (335, 275), (380, 135),
                                                               (320, 50)), 2)
        ugly = pygame.draw.polygon(screen_display, black, ((490, 60), (560, 45), (620, 125), (490, 200)), 2)
        triangle2 = pygame.draw.polygon(screen_display, black, ((560, 250), (660, 340), (590, 425)), 2)
        rectangle2 = pygame.draw.polygon(screen_display, black, ((635, 50), (750, 50), (750, 270), (635, 270)), 2)
        diamond = pygame.draw.polygon(screen_display, black, ((770, 70), (830, 40), (870, 85), (840, 330)), 2)
        stop_sign = pygame.draw.polygon(screen_display, black, ((700, 370), (775, 325), (825, 370), (825, 460),
                                                                (755, 490), (700, 450)), 2)

        pygame.draw.lines(screen_display, blue, False, path, 3)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()