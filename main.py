import pygame
from game import draw_game_field

pygame.init()

# Установка размеров окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя игра на Pygame")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)

# Функция для отрисовки текста на экране
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Флаг для отображения игрового поля
show_game_field = False

# Основной игровой цикл
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if new_game_button.collidepoint(mouse_pos):
                show_game_field = True
            if exit_button.collidepoint(mouse_pos):
                running = False

    # Рисуем кнопки
    new_game_button = pygame.Rect(300, 200, 200, 50)
    exit_button = pygame.Rect(300, 300, 200, 50)

    pygame.draw.rect(screen, BLACK, new_game_button)
    draw_text("Новая игра", font, WHITE, screen, 400, 225)

    pygame.draw.rect(screen, BLACK, exit_button)
    draw_text("Выход", font, WHITE, screen, 400, 325)

    # Отображение игрового поля при нажатии на кнопку "Новая игра"
    if show_game_field:
        draw_game_field(screen)

    # Обновление экрана
    pygame.display.flip()

pygame.quit()