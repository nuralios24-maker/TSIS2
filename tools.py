import pygame
from math import sqrt

WHITE = (255, 255, 255)


def pencil(surface, color, last_pos, current_pos, size):
    pygame.draw.line(surface, color, last_pos, current_pos, size)


def eraser(surface, last_pos, current_pos, size):
    pygame.draw.line(surface, WHITE, last_pos, current_pos, size)


def line(surface, color, start_pos, end_pos, size):
    pygame.draw.line(surface, color, start_pos, end_pos, size)


def rectangle(surface, color, start_pos, end_pos, size):
    x1, y1 = start_pos
    x2, y2 = end_pos

    rect = pygame.Rect(
        min(x1, x2),
        min(y1, y2),
        abs(x2 - x1),
        abs(y2 - y1)
    )

    pygame.draw.rect(surface, color, rect, size)


def circle(surface, color, start_pos, end_pos, size):
    x1, y1 = start_pos
    x2, y2 = end_pos

    radius = int(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    pygame.draw.circle(surface, color, start_pos, radius, size)


def square(surface, color, start_pos, end_pos, size):
    x1, y1 = start_pos
    x2, y2 = end_pos

    side = min(abs(x2 - x1), abs(y2 - y1))

    if x2 < x1:
        x1 -= side
    if y2 < y1:
        y1 -= side

    rect = pygame.Rect(x1, y1, side, side)
    pygame.draw.rect(surface, color, rect, size)


def right_triangle(surface, color, start_pos, end_pos, size):
    x1, y1 = start_pos
    x2, y2 = end_pos

    points = [
        (x1, y1),
        (x1, y2),
        (x2, y2)
    ]

    pygame.draw.polygon(surface, color, points, size)


def equilateral_triangle(surface, color, start_pos, end_pos, size):
    x1, y1 = start_pos
    x2, y2 = end_pos

    points = [
        ((x1 + x2) // 2, y1),
        (x1, y2),
        (x2, y2)
    ]

    pygame.draw.polygon(surface, color, points, size)


def rhombus(surface, color, start_pos, end_pos, size):
    x1, y1 = start_pos
    x2, y2 = end_pos

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    points = [
        (center_x, y1),
        (x2, center_y),
        (center_x, y2),
        (x1, center_y)
    ]

    pygame.draw.polygon(surface, color, points, size)


def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()

    if x < 0 or x >= width or y < 0 or y >= height:
        return

    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), new_color)

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))