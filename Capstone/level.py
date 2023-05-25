import pygame
from tile import Tile, LoseTile, NPC, NPC2,NPC3, Spike, Dirt
from settings import tile_size, screen_width
from player import Player
from pyvidplayer import Video


correctanswer = 0

SCREEN = pygame.display.set_mode((1180, 640))

#Sir nins NPC
def sir():
    Vid = Video("graphics/sir_nins/play 2.mp4")
    Vid.set_size((1180, 640))
    Vid.active
    while True:
        Vid.draw(SCREEN, (0,0))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Vid.close()
                Vid.active == False
                return
            if keys[pygame.K_a]:
                correct()
            if keys[pygame.K_b]:
                wrong()
            if keys[pygame.K_c]:
                wrong()
            if keys[pygame.K_d]:
                wrong()

        pygame.display.update()
                

   #Sir correct answer 
def correct():
    global correctanswer
    Vid = Video("graphics/sir_nins/right 3.mp4")
    Vid.set_size((1180, 640))
    Vid.active
    while True:
        Vid.draw(SCREEN, (0,0))
        Vid.set_size((1180, 640))
        Vid.active == True
        while True:
            Vid.draw(SCREEN, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Vid.close()
                    Vid.active = False 
                    continue
            correctanswer += 1 
            pygame.display.update()   
            return
     #sir nins-answer incorrect       
def wrong():
    Vid = Video("graphics/sir_nins/wrong 2.mp4")
    Vid.set_size((1180, 640))
    Vid.active == True
    while True:
        Vid.draw(SCREEN, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Vid.close()
                Vid.active = False 
                continue
        
        pygame.display.update()
        return

#Ma'am jecka NPC
def npc():
    Vid = Video("graphics/maam/NPC-jecka.mp4")
    Vid.set_size((1180, 640))
    Vid.active
    while True:
        Vid.draw(SCREEN, (0,0))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Vid.close()
                Vid.active = False
                continue
            if keys[pygame.K_a]:
                wrong1()
            if keys[pygame.K_b]:
                correct1()
            if keys[pygame.K_c]:
                wrong1()
            if keys[pygame.K_d]:
                wrong1()

        pygame.display.update()

def npc3():
    Vid = Video("graphics/intro vid.mp4")
    Vid.set_size((1180, 640))
    Vid.active
    while True:
        Vid.draw(SCREEN, (0,0))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Vid.close()
                Vid.active = False
            if keys[pygame.K_a]:
                wrong1()
            if keys[pygame.K_b]:
                correct1()
            if keys[pygame.K_c]:
                wrong1()
            if keys[pygame.K_d]:
                wrong1()
            
        pygame.display.update()
       
#Ma'am jecka Correct answer CS#1    
def correct1():
    global correctanswer
    Vid = Video("graphics/maam/right 1.mp4")
    Vid.set_size((1180, 640))
    Vid.active
    while True:
        Vid.draw(SCREEN, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Vid.close()
                Vid.active
            if keys[pygame.K_a]:
                wrong1()
            if keys[pygame.K_b]:
                wrong1()
            if keys[pygame.K_c]:
                correct2()
            if keys[pygame.K_d]:
                wrong1()
        correctanswer += 1
        pygame.display.update()

#Ma'am jecka CS#2
def correct2():
    global correctanswer
    Vid = Video("graphics/maam/right 2.mp4")
    Vid.set_size((1180, 640))
    Vid.active
    while True:
        Vid.draw(SCREEN, (0,0))
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Vid.close()
                Vid.active = False 
                continue
            pygame.display.update()
            if keys[pygame.K_a]:
                correctanswer += 1
                return
        pygame.display.update()
        
           
#Ma'am jecka Incorrect answer        
def wrong1():
    Vid = Video("graphics/maam/wrong.mp4")
    Vid.set_size((1180, 640))
    Vid.active == True
    while True:
        Vid.draw(SCREEN, (0,0))
        pygame.display.update()
    
        Vid.active = False 
        
        pygame.display.update()

def winner():
    if correctanswer == 3:
        Vid = Video("graphics/loading.mp4")
        Vid.set_size((1180, 640))
        Vid.active == True
        while True:
            Vid.draw(SCREEN, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Vid.close()
                    Vid.active = False 
            pygame.display.update()

    
        
            
    
#Level Class
class Level:
    def __init__(self,level_data,surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.lose_tiles = pygame.sprite.Group()
        self.npc = pygame.sprite.Group()
        self.npc2 = pygame.sprite.Group()
        self.spike = pygame.sprite.Group()
        self.dirt = pygame.sprite.Group()
        self.npc3 = pygame.sprite.Group()
       
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'Z':
                    tile = Dirt((x,y),tile_size)
                    self.dirt.add(tile)
                if cell == 'Y':
                    tile = LoseTile((x,y),tile_size)
                    self.lose_tiles.add(tile)
                if cell == 'N':
                    tile = NPC((x,y),tile_size)
                    self.npc.add(tile)
                if cell == 'S':
                    tile = NPC2((x,y),tile_size)
                    self.npc2.add(tile)
                if cell == 'B':
                    tile = NPC3((x,y),tile_size)
                    self.npc3.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == 'D':
                    tile = Spike((x,y), tile_size)
                    self.spike.add(tile)
                
#Scrolling Background
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
                    
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
            
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
#Rect and Collisions            
        for sprite in self.lose_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                player.is_dead = True
        keys = pygame.key.get_pressed()
        for sprite in self.npc.sprites():
            if sprite.rect.colliderect(player.rect) and keys[pygame.K_e]:  
                npc()
        
        for sprite in self.npc2.sprites():
            if sprite.rect.colliderect(player.rect) and keys[pygame.K_e]:  
                sir()

        for sprite in self.npc3.sprites():
            if sprite.rect.colliderect(player.rect) and keys[pygame.K_e]:  
                npc3()

        for sprite in self.spike.sprites():
            if sprite.rect.colliderect(player.rect):  
                player.is_dead = True
            
    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.lose_tiles.update(self.world_shift)
        self.lose_tiles.draw(self.display_surface)
        self.npc.update(self.world_shift)
        self.npc.draw(self.display_surface)
        self.npc2.update(self.world_shift)
        self.npc2.draw(self.display_surface)
        self.spike.update(self.world_shift)
        self.spike.draw(self.display_surface)
        self.dirt.update(self.world_shift)
        self.dirt.draw(self.display_surface)
        self.npc3.update(self.world_shift)
        self.npc3.draw(self.display_surface)
        

        self.scroll_x()
        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        winner()
        return self.player.sprite
