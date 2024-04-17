import pygame
import math

def shoot(screen, bullets, player, bullet_speed, bullet_delay_counter, bullet_delay):
    if bullet_delay_counter > 0:
        bullet_delay_counter -= 1

    if pygame.mouse.get_pressed()[0] and bullet_delay_counter <= 0:  # Левая кнопка мыши
        mouse_pos = pygame.mouse.get_pos()
        angle = math.atan2(mouse_pos[1] - player.x, mouse_pos[0] - player.y)
        bullets.append([player.x + 5, player.y, angle])
        bullet_delay_counter = bullet_delay

    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 0), (bullet[0], bullet[1], 3, 3))
        if len(bullet) == 3:  # Если есть угол, двигаем пулю в этом направлении
            bullet[0] += bullet_speed * math.cos(bullet[2])
            bullet[1] += bullet_speed * math.sin(bullet[2])
        else:
            bullet[1] -= bullet_speed  # Иначе двигаем пулю вверх

    # Удаление пуль, вышедших за пределы экрана
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    return bullets, bullet_delay_counter
