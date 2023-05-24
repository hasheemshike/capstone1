import pygame
from support import import_folder
from button import Button


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.10
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
       
       #player movements
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.7
        self.jump_speed = -16

        self.max_jumps = 2
        self.jump_count = 0
        self.jump_cooldown = 800
        self.last_jump_time = 0

        #player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.is_dead = False
def mini_menu():
    OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

    SCREEN = pygame.display.set_mode((1180,640))
    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)
    BG1 = pygame.image.load("graphics/BG.png")

    mathew3 = Button(image=None, pos=(590,100),
                     text_input="Presented by:", font=get_font(75), base_color="grey", hovering_color="orange")
                
    SCREEN.blit(BG1,(0,0))

    mathew3.changeColor(OPTIONS_MOUSE_POS)
    mathew3.update(SCREEN)

    pygame.display.update

    def import_character_assets(self):
         character_path = 'graphics/character/'
         self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

         for animation in self.animations.keys():
              full_path = character_path + animation
              self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]

        #loop frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
             self.frame_index = 0
        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

        # set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        



    def get_input(self):
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_d]:
                self.direction.x = 1
                self.facing_right = True
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.facing_right = False
            else:
                self.direction.x = 0

            if keys[pygame.K_ESCAPE]:
                mini_menu()

            if keys[pygame.K_SPACE] and self.jump_count < self.max_jumps and self.on_ground:
                current_time = pygame.time.get_ticks()
                time_since_last_jump = current_time - self.last_jump_time
                if time_since_last_jump >= self.jump_cooldown:
                    self.jump()
                    self.last_jump_time = current_time
                    self.jump_count += 1
                    if self.jump_count == 1:
                        self.jump_count -= 1

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
                 
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
            self.get_input()
            self.get_status()
            self.animate()
