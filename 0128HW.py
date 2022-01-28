import pygame
import random

# 顏色常數
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

"""
    Block類別: 繼承自Sprite類別
"""
class Block(pygame.sprite.Sprite):
    
    """ 
        建構式
        當物件產生時會呼叫建構式
        傳入的參數為顏色，還有block的長寬 
    """
    def __init__(self, color, width, height):
        # 在Block建構式裡，我們的目標就是根據傳入參數，創造一個有特定顏色和大小的image   
        
        # 呼叫父類別(此處就是Sprite類別)的建構式
        super().__init__()

        self.image = pygame.Surface([width,height])
        # 創造一個block的image，接著填入顏色到此image
        self.image.fill(color)
        
        #pygame.image.load("playerShip1_orange.png").convert()
        #self.image.set_colorkey(BLACK) #設置去背

        # 抓出image的rect物件，設定給block的屬性rect
        # rect.width & rect.height就是傳入建構式的width&height
        # rect.x and rect.y則是0，之後再根據情況更新
        self.rect = self.image.get_rect()


# 初始化pygame
pygame.init()

# 設定設窗大小
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

mygroup = pygame.sprite.Group()
player = Block(RED,20,15)
mygroup.add(player)

for i in range(50):
    block = Block(BLACK,20,15)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height) 

    mygroup.add(block)   
# 判斷迴圈是否繼續的旗標
play = True
# 畫面更新頻率
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while play:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            play = False 

    # 清除畫面
    screen.fill(WHITE)

    # 畫出所有角色
    #all_sprites_list.draw(screen)      
    mygroup.draw(screen)

    # 更新 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
