import pygame, sys
from settings import * 
from level import Level
from button import Button
from pyvidplayer import Video
from player import Player
from pygame import mixer


pygame.mixer.init()
pygame.init()


SCREEN = pygame.display.set_mode((1180, 640))
pygame.display.set_caption("Mathew")
icon = pygame.image.load("assets/icon.png").convert_alpha()
pygame.display.set_icon(icon)

BG = pygame.image.load("graphics/BG.png") 
bg = pygame.image.load("graphics/BG.png")  
BG1 = pygame.image.load("graphics/back.png")


def game():
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    level = Level(level_map,screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                
                                

        screen.blit(bg, (0,0))
        player = level.run()
        if player.is_dead == True:
            # pygame.quit() REMOVED
            game_over()

        pygame.display.update()
        clock.tick(60)

        
                

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)
    
vid = Video("graphics/intro vid.mp4")
vid.set_size((1180, 640))

def intro():
    vid.active
    while True:
        vid.draw(SCREEN, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                vid.active = False # ADDED
                # background_music() REMOVED
                # main_menu() REMOVED
        if vid.active == False: # ADDED
            pygame.display.update() # ADDED
            return # ADDED

def credits():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG1,(0,0))

        mathew = Button(image=None, pos=(590,100),
                            text_input="Presented by:", font=get_font(75), base_color="grey", hovering_color="orange")
        mathew1 = Button(image=None, pos=(590,180),
                            text_input="xXProg_GodzXx", font=get_font(50), base_color="grey", hovering_color="orange")
        CREDITS_BACK = Button(image=pygame.image.load("graphics/3.png"), pos=(590,500),
                            text_input="Back", font=get_font(30), base_color="White", hovering_color="orange")
        
        

        CREDITS_BACK.changeColor(OPTIONS_MOUSE_POS)
        CREDITS_BACK.update(SCREEN)
        mathew.update(SCREEN)
        mathew1.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    options()
        
        pygame.display.update()

def game_over():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        gameover = Button(image=pygame.image.load("graphics/2.png"), pos=(590,160),
                            text_input="Retry", font=get_font(30), base_color="grey", hovering_color="orange")
        gameover1 = Button(image=pygame.image.load('graphics/2.png'), pos=(590,500),
                            text_input="Quit", font=get_font(30), base_color="grey", hovering_color="orange")
        gameover2 = Button(image=pygame.image.load("graphics/1.png"), pos=(590,350),
                            text_input="Options", font=get_font(30), base_color="grey", hovering_color="orange")
        
        for button in[gameover, gameover1, gameover2]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if gameover.checkForInput(OPTIONS_MOUSE_POS):
                        game()
                    if gameover1.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()
                    if gameover2.checkForInput(OPTIONS_MOUSE_POS):
                        options2()

            pygame.display.update()

def options2():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))
        
        CREDITS = Button(image=pygame.image.load("graphics/1.png"), pos=(590,400),
                            text_input="Credits", font=get_font(30), base_color="White", hovering_color="Orange")
        MUTE = Button(image=pygame.image.load("graphics/2.png"), pos=(590,100),
                            text_input="Mute", font=get_font(30), base_color="White", hovering_color="orange")
        UNMUTE = Button(image=pygame.image.load("graphics/1.png"), pos=(590,250),
                            text_input="Unmute", font=get_font(30), base_color="White", hovering_color="orange")
        OPTIONS_BACK = Button(image=pygame.image.load("graphics/2.png"), pos=(590, 550), 
                            text_input="BACK", font=get_font(30), base_color="White", hovering_color="orange")


        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        MUTE.changeColor(OPTIONS_MOUSE_POS)
        CREDITS.changeColor(OPTIONS_MOUSE_POS)
        UNMUTE.changeColor(OPTIONS_MOUSE_POS)
        CREDITS.update(SCREEN)
        OPTIONS_BACK.update(SCREEN)
        MUTE.update(SCREEN)
        UNMUTE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MUTE.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer_music.pause()
                if UNMUTE.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer_music.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    game_over() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS.checkForInput(OPTIONS_MOUSE_POS):
                    credits()
        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))
        
        CREDITS = Button(image=pygame.image.load("graphics/1.png"), pos=(590,400),
                            text_input="Credits", font=get_font(30), base_color="White", hovering_color="Orange")
        MUTE = Button(image=pygame.image.load("graphics/2.png"), pos=(590,100),
                            text_input="Mute", font=get_font(30), base_color="White", hovering_color="orange")
        UNMUTE = Button(image=pygame.image.load("graphics/1.png"), pos=(590,250),
                            text_input="Unmute", font=get_font(30), base_color="White", hovering_color="orange")
        OPTIONS_BACK = Button(image=pygame.image.load("graphics/2.png"), pos=(590, 550), 
                            text_input="BACK", font=get_font(30), base_color="White", hovering_color="orange")


        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        MUTE.changeColor(OPTIONS_MOUSE_POS)
        CREDITS.changeColor(OPTIONS_MOUSE_POS)
        UNMUTE.changeColor(OPTIONS_MOUSE_POS)
        CREDITS.update(SCREEN)
        OPTIONS_BACK.update(SCREEN)
        MUTE.update(SCREEN)
        UNMUTE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MUTE.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer_music.pause()
                if UNMUTE.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer_music.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CREDITS.checkForInput(OPTIONS_MOUSE_POS):
                    credits()
        pygame.display.update()

Vid = Video("graphics/loading.mp4") 
Vid.set_size((1180, 640))

def loading():
     Vid.active
     while True:
        Vid.draw(SCREEN, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Vid.close()
                Vid.active = False # ADDED
                # game() REMOVED
                # return REMOVED 
        if Vid.active == False: # ADDED
            pygame.display.update() # ADDED
            return # ADDED
     
def background_music():
     mixer.music.load('graphics/videoplayback.mp3')
     mixer.music.play(-1)

def main_menu():
    # loading() REMOVED
    # game() REMOVED

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
    
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(0).render("MATHEW", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        MATHEW = Button(image=pygame.image.load("graphics/mathew.png"), pos=(590, 100), 
                            text_input="PLAY", font=get_font(0), base_color="#d7fcd4", hovering_color="orange")
        PLAY_BUTTON = Button(image=pygame.image.load("graphics/2.png"), pos=(590, 250), 
                            text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="orange")
        OPTIONS_BUTTON = Button(image=pygame.image.load("graphics/1.png"), pos=(590, 400), 
                            text_input="OPTIONS", font=get_font(30), base_color="#d7fcd4", hovering_color="orange")
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/2.png"), pos=(590, 550), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="orange")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, MATHEW]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mixer.music.stop()
                    loading()
                    game() # ADDED
                    break
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

intro()
main_menu()
