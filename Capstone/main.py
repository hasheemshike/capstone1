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

BG = pygame.image.load("assets/Back.jpg") 
Button1 = pygame.image.load("assets/Mute.png")
Button2 = pygame.image.load("assets/Unmute.png")  



def game():
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    level = Level(level_map,screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                
                                

        screen.fill('white')
        player = level.run()
        if player.is_dead == True:
            pygame.quit()
            return

        pygame.display.update()
        clock.tick(60)

        
                

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)
    
vid = Video("assets/starting vid_Trim.mp4")
vid.set_size((1180, 640))

def intro():
    vid.active
    while True:
         vid.draw(SCREEN, (0,0))
         pygame.display.update()
         for event in pygame.event.get():
              if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                background_music()
                main_menu()

    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))
        
        MUTE = Button(image=Button1, pos=(640,100),
                            text_input="Mute", font=get_font(0), base_color="White", hovering_color="Green")
        UNMUTE = Button(image=Button2, pos=(640,300),
                            text_input="Unmute", font=get_font(0), base_color="White", hovering_color="Green")
        OPTIONS_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        MUTE.changeColor(OPTIONS_MOUSE_POS)
        UNMUTE.changeColor(OPTIONS_MOUSE_POS)
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

        pygame.display.update()

Vid = Video("assets/starting vid_Trim.mp4") 
Vid.set_size((1180, 640))

def loading():
     Vid.active
     while True:
         Vid.draw(SCREEN, (0,0))
         pygame.display.update()
         for event in pygame.event.get():
              if event.type == pygame.MOUSEBUTTONDOWN:
                Vid.close()           
                game()
                return
     
def background_music():
     mixer.music.load('graphics/videoplayback.mp3')
     mixer.music.play(-1)

def main_menu():
    loading()
    game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
    
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MATHEW", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/start button.png"), pos=(600, 250), 
                            text_input="PLAY", font=get_font(0), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options.png"), pos=(600, 400), 
                            text_input="OPTIONS", font=get_font(0), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Exit button.png"), pos=(600, 550), 
                            text_input="QUIT", font=get_font(0), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
                    break
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

intro()
main_menu()
