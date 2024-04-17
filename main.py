import pygame
import math
from game import draw_game_field
from character import Character
from shooting import shoot
from random_trees import RandomTrees

pygame.init()

#для настройки кадров в секунду
clock = pygame.time.Clock()

# Установка размеров окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя игра на Pygame")

# Создание объекта класса RandomTrees
random_trees = RandomTrees(screen_width, screen_height, 20, 10)

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
player = Character(0, 0)
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

    # Вызов функции для стрельбы
    bullets, bullet_delay_counter = shoot(screen, bullets, player, bullet_speed, bullet_delay_counter, bullet_delay)

        # Удаление пуль, вышедших за пределы экрана
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Отрисовка рандомных деревьев
    random_trees.draw(screen)

    # Проверка коллизий с деревьями
    for tree in random_trees.trees:
        tree_rect = pygame.Rect(tree[0], tree[1], random_trees.tree_size, random_trees.tree_size)
        player_rect = pygame.Rect(player.x, player.y, 10, 10)
        if tree_rect.colliderect(player_rect):
            # Обработка столкновения
            player.x, player.y = player.prev_x, player.prev_y

    # Обновление экрана
    pygame.display.flip()
    # фреймрейт 100
    clock.tick(100)


pygame.quit()
