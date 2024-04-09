import pygame
import math
from game import draw_game_field
from character import Character

pygame.init()

#для настройки кадров в секунду
clock = pygame.time.Clock()

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
# Создание персонажа
player = Character(500, 500)
# Создание пули как отдельного объекта
bullets = []
bullet_speed = 7
bullet_delay = 24
bullet_delay_counter = 0
# Основной игровой цикл

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    # Рисуем кнопки
    new_game_button = pygame.Rect(300, 200, 200, 50)
    exit_button = pygame.Rect(300, 300, 200, 50)

    pygame.draw.rect(screen, BLACK, new_game_button)
    draw_text("Новая игра", font, WHITE, screen, 400, 225)

    pygame.draw.rect(screen, BLACK, exit_button)
    draw_text("Выход", font, WHITE, screen, 400, 325)

    # Обработка нажатий кнопок мыши
    mouse_pos = pygame.mouse.get_pos()
    if new_game_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
            show_game_field = True

    if exit_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
            running = False

    # Отображение игрового поля при нажатии на кнопку "Новая игра"
    if show_game_field:
        draw_game_field(screen)
        player.draw(screen)

    # Стрельба с задержкой
    if bullet_delay_counter > 0:
        bullet_delay_counter -= 1

    # Стрельба по указанию мыши
    if pygame.mouse.get_pressed()[0] and bullet_delay_counter <= 0:  # Левая кнопка мыши
        mouse_pos = pygame.mouse.get_pos()
        angle = math.atan2(mouse_pos[1] - player.x, mouse_pos[0] - player.y)
        bullets.append([player.x + 5, player.y, angle])
        bullet_delay_counter = bullet_delay

    for bullet in bullets:
        pygame.draw.rect(screen, BLACK, (bullet[0], bullet[1], 3, 3))
        if len(bullet) == 3:  # Если есть угол, двигаем пулю в этом направлении
            bullet[0] += bullet_speed * math.cos(bullet[2])
            bullet[1] += bullet_speed * math.sin(bullet[2])
        else:
            bullet[1] -= bullet_speed  # Иначе двигаем пулю вверх

        # Удаление пуль, вышедших за пределы экрана
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Обновление экрана
    pygame.display.flip()
    # фреймрейт 60
    clock.tick(60)


pygame.quit()
