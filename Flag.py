import pygame


# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)

def draw():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (152, 118, 84), (345, 260, 5, 100), 0)
    pygame.draw.rect(screen, (255, 255, 255), (350, 260, 100, 20), 0)

draw()
# смена (отрисовка) кадра:
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()