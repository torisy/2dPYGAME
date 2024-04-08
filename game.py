import pygame

# Установка размеров окна игрового поля для Full HD
field_width = 1920
field_height = 1080

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Статичные зеленые квадраты
static_rects = [
    pygame.Rect(100, 100, 50, 50),
    pygame.Rect(200, 200, 50, 50),
    pygame.Rect(300, 300, 50, 50)
]

# Функция для отрисовки игрового поля и статичных квадратов с коллизиями
def draw_game_field(screen):
    screen.fill(WHITE)  # Заливка экрана белым цветом

    # Рисуем игровое поле
    pygame.draw.rect(screen, (150, 150, 150), (0, 0, field_width, field_height))

    # Обновление экрана
    pygame.display.flip()
