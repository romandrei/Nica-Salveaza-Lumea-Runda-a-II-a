import pygame
import sys
import random
pygame.init()

frstr = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Nică Salvează Lumea: Runda a II-a")

nicapng = pygame.image.load("Img/nica.png")
spacepng = pygame.image.load("Img/bgspace.png")
glont1png = pygame.image.load("Img/glont1.png")
glont2png = pygame.image.load("Img/glont2.png")
manualmarepng = pygame.image.load("Img/manualmare.png")
covidpng = pygame.image.load("Img/covid.png")
obiectpng = pygame.image.load("Img/obiect.png")

ceas = pygame.time.Clock()

font = pygame.font.SysFont("arial", 32)
text = font.render("Apasa SPACE pentru a incepe!", True, (0, 250, 0))
textRect = text.get_rect()
textRect.center = (400, 400)

meniu = True
while meniu:
    frstr.blit(spacepng, (0, 0))
    frstr.blit(text, textRect)
    space = pygame.key.get_pressed()
    if space[pygame.K_SPACE]:
        meniu = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(nicapng, (75, 103))
        self.rect = self.image.get_rect()
        self.rect.x = 400 - 90
        self.rect.y = 500 - 123
        self.vit = 6
    def update(self):
        self.taste = pygame.key.get_pressed()
        if self.taste[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.vit
        if self.taste[pygame.K_DOWN] and self.rect.y < 800 - 110:
            self.rect.y += self.vit
        if self.taste[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.vit
        if self.taste[pygame.K_RIGHT] and self.rect.x < 800 - 80:
            self.rect.x += self.vit

class glont(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(glont1png, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vit = 12
    def update(self):
        self.rect.y -= self.vit
        if self.rect.y < -32:
            self.kill()

class coronavirus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(covidpng, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - 64)
        self.rect.y = random.randrange(864, 928)
        self.vit = random.randrange(3, 5)
    def update(self):
        self.rect.y -= self.vit
        if self.rect.y < -64:
            self.rect.y = random.randrange(864, 928, 1)
            self.rect.x = random.randrange(0, 800 - 64)
            self.vit = random.randrange(3, 5)
        if manual.hp < 1:
            self.kill()

class manualmare(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(manualmarepng, (196, 256))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 0
        self.hp = 800
    def update(self):
        if self.hp < 1:
            self.kill()

class glont2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(glont2png, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-32, 0)
        self.rect.y = random.randrange(-32, 800 - 32)
        self.vit = random.randrange(4, 6)
    def update(self):
        self.rect.x += self.vit
        if self.rect.x > 832:
            self.rect.x = random.randrange(-32, 0)
            self.rect.y = random.randrange(-32, 800 - 32)
            self.vit = random.randrange(4, 6)
        if manual.hp < 1:
            self.kill()

class glont3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(glont2png, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(832, 800, -1)
        self.rect.y = random.randrange(-32, 800 - 32)
        self.vit = random.randrange(4, 6)
    def update(self):
        self.rect.x -= self.vit
        if self.rect.x < -32:
            self.rect.x = random.randrange(832, 800, -1)
            self.rect.y = random.randrange(-32, 800 - 32)
            self.vit = random.randrange(4, 6)
        if manual.hp < 1:
            self.kill()

class obiect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(obiectpng, (156 ,78))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - 156)
        self.rect.y = random.randrange(-78, -156, -1)
        self.vit = 7
    def update(self):
        self.rect.y += self.vit
        if self.rect.y > 800 + 156:
            self.rect.x = random.randrange(0, 800 - 156)
            self.rect.y = random.randrange(-78, -156, -1)
        if manual.hp < 1:
            self.kill()
            
toate = pygame.sprite.Group()
gloante = pygame.sprite.Group()
virusi = pygame.sprite.Group()
jucatori = pygame.sprite.Group()
manuale = pygame.sprite.Group()
ply = player()
jucatori.add(ply)
toate.add(ply)
manual = manualmare()
toate.add(manual)
manuale.add(manual)
ob = obiect()
toate.add(ob)
virusi.add(ob)

for i in range(4):
    covid = coronavirus()
    toate.add(covid)
    virusi.add(covid)

for i in range(3):
    gl2 = glont2()
    toate.add(gl2)
    virusi.add(gl2)

for i in range(3):
    gl3 = glont3()
    toate.add(gl3)
    virusi.add(gl3)

def hpcarte():
    pygame.draw.rect(frstr, (0, 0, 0), (0, 800 - 54, 800, 54))
    if manual.hp > 0:
        pygame.draw.rect(frstr, (0, 250, 0), (0, 800 - 54, manual.hp, 54))

rulare = True
while rulare:
    ceas.tick(120)
    frstr.blit(spacepng, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gl = glont(ply.rect.x + 25, ply.rect.y - 20)
                gloante.add(gl)
                toate.add(gl)

    lovitmanual = pygame.sprite.groupcollide(manuale, gloante, False, True)
    lovitply = pygame.sprite.groupcollide(jucatori, virusi, False, False)
    lovitply2 = pygame.sprite.groupcollide(manuale, jucatori, True, False)
    
    if lovitmanual:
        manual.hp -= 8
        
    if lovitply2:
        pygame.quit()
        sys.exit()

    if lovitply:
        pygame.quit()
        sys.exit()
                      
    toate.update()
    toate.draw(frstr)
    hpcarte()
    pygame.display.flip()
