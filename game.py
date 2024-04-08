import pygame

# Установка размеров окна игрового поля
field_width = 600
field_height = 400

# Функция для отрисовки игрового поля
def draw_game_field(screen):
    screen.fill((150, 150, 150))  # Заливка экрана серым цветом

    # Рисуем игровое поле
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, field_width, field_height), 2)

    # Обновление экрана
    pygame.display.flip()
