import pygame


class Shop:
    def __init__(self):
        self.return_button = pygame.image.load(r'../img/cross.png')
        self.return_button_pos = (0, 0)
        self.click_damage = pygame.image.load(r'../img/damage.png')
        self.click_damage_pos = (50, 100)
        self.DPS = pygame.image.load(r'../img/DPS.png')
        self.DPS_pos = (50, 350)
        self.click_cost = 11
        self.DPS_cost = 1000

    def try_to_buy(self, type, balance):
        if type == 'click':
            if balance >= self.click_cost:
                self.click_cost *= 2
                return balance - self.click_cost / 2
        return balance

    def draw(self, screen, balance):
        screen.blit(self.return_button, self.return_button_pos)
        screen.blit(self.click_damage, self.click_damage_pos)
        screen.blit(self.DPS, self.DPS_pos)
        self.write(screen, balance)

    def write(self, screen, balance):
        f1 = pygame.font.Font(None, 80)
        text = f1.render(f"У вас на счету: {balance}", True, [255, 255, 255])
        screen.blit(text, (60, 0))
