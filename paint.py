import pygame
from datetime import datetime
import tools

pygame.init()

width = 1200
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGNETA = (225, 0, 255)
GRAY = (220, 220, 220)

# Canvas
TOOLBAR_HEIGHT = 100
canvas = pygame.Surface((width, height - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

# BUTTON
CLEAR_BUTTON = pygame.Rect(20, 20, 100, 35)
PENCIL_BUTTON = pygame.Rect(130, 20, 100, 35)
ERASER_BUTTON = pygame.Rect(240, 20, 100, 35)
LINE_BUTTON = pygame.Rect(350, 20, 100, 35)
RECT_BUTTON = pygame.Rect(460, 20, 100, 35)
CIRCLE_BUTTON = pygame.Rect(570, 20, 100, 35)
FILL_BUTTON = pygame.Rect(680, 20, 100, 35)
TEXT_BUTTON = pygame.Rect(790, 20, 100, 35)

SQUARE_BUTTON = pygame.Rect(20, 60, 100, 35)
RIGHT_TRIANGLE_BUTTON = pygame.Rect(130, 60, 100, 35)
EQUILATERAL_BUTTON = pygame.Rect(240, 60, 100, 35)
RHOMBUS_BUTTON = pygame.Rect(350, 60, 100, 35)

SMALL_BUTTON = pygame.Rect(470, 60, 60, 35)
MEDIUM_BUTTON = pygame.Rect(540, 60, 60, 35)
LARGE_BUTTON = pygame.Rect(610, 60, 60, 35)

RED_BUTTON = pygame.Rect(700, 60, 35, 35)
GREEN_BUTTON = pygame.Rect(745, 60, 35, 35)
BLUE_BUTTON = pygame.Rect(790, 60, 35, 35)
BLACK_BUTTON = pygame.Rect(835, 60, 35, 35)
YELLOW_BUTTON = pygame.Rect(880, 60, 35, 35)

font = pygame.font.SysFont("arial", 20)
text_font = pygame.font.SysFont("arial", 30)

tool = "pencil"
color = BLACK
brush_size = 5

drawing = False
last_pos = None
start_pos = None

text_active = False
text_value = ""
text_pos = None


def draw_button(rect, text):
    pygame.draw.rect(screen, GRAY, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    img = font.render(text, True, BLACK)
    img_rect = img.get_rect(center=rect.center)
    screen.blit(img, img_rect)


def draw_buttons():
    pygame.draw.rect(screen, WHITE, (0, 0, width, TOOLBAR_HEIGHT))

    draw_button(CLEAR_BUTTON, "Clear")
    draw_button(PENCIL_BUTTON, "Pencil")
    draw_button(ERASER_BUTTON, "Eraser")
    draw_button(LINE_BUTTON, "Line")
    draw_button(RECT_BUTTON, "Rect")
    draw_button(CIRCLE_BUTTON, "Circle")
    draw_button(FILL_BUTTON, "Fill")
    draw_button(TEXT_BUTTON, "Text")

    draw_button(SQUARE_BUTTON, "Square")
    draw_button(RIGHT_TRIANGLE_BUTTON, "Right")
    draw_button(EQUILATERAL_BUTTON, "Triangle")
    draw_button(RHOMBUS_BUTTON, "Rhomb")

    draw_button(SMALL_BUTTON, "1")
    draw_button(MEDIUM_BUTTON, "2")
    draw_button(LARGE_BUTTON, "3")

    pygame.draw.rect(screen, RED, RED_BUTTON)
    pygame.draw.rect(screen, GREEN, GREEN_BUTTON)
    pygame.draw.rect(screen, BLUE, BLUE_BUTTON)
    pygame.draw.rect(screen, BLACK, BLACK_BUTTON)
    pygame.draw.rect(screen, YELLOW, YELLOW_BUTTON)

    pygame.draw.rect(screen, BLACK, RED_BUTTON, 2)
    pygame.draw.rect(screen, BLACK, GREEN_BUTTON, 2)
    pygame.draw.rect(screen, BLACK, BLUE_BUTTON, 2)
    pygame.draw.rect(screen, BLACK, BLACK_BUTTON, 2)
    pygame.draw.rect(screen, BLACK, YELLOW_BUTTON, 2)

    info = font.render("Tool: " + tool + " | Size: " + str(brush_size), True, BLACK)
    screen.blit(info, (930, 65))


def get_canvas_pos(pos):
    x, y = pos
    return x, y - TOOLBAR_HEIGHT


def draw_shape(surface, selected_tool, start, end):
    if selected_tool == "line":
        tools.line(surface, color, start, end, brush_size)

    elif selected_tool == "rect":
        tools.rectangle(surface, color, start, end, brush_size)

    elif selected_tool == "circle":
        tools.circle(surface, color, start, end, brush_size)

    elif selected_tool == "square":
        tools.square(surface, color, start, end, brush_size)

    elif selected_tool == "right_triangle":
        tools.right_triangle(surface, color, start, end, brush_size)

    elif selected_tool == "equilateral_triangle":
        tools.equilateral_triangle(surface, color, start, end, brush_size)

    elif selected_tool == "rhombus":
        tools.rhombus(surface, color, start, end, brush_size)


running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))
    draw_buttons()

    mouse_pos = pygame.mouse.get_pos()

    if drawing and start_pos is not None:
        if tool in ["line", "rect", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"]:
            preview = canvas.copy()
            current_canvas_pos = get_canvas_pos(mouse_pos)
            draw_shape(preview, tool, start_pos, current_canvas_pos)
            screen.blit(preview, (0, TOOLBAR_HEIGHT))

    if text_active:
        img = text_font.render(text_value, True, color)
        screen.blit(img, (text_pos[0], text_pos[1] + TOOLBAR_HEIGHT))

        cursor_x = text_pos[0] + img.get_width() + 2
        cursor_y = text_pos[1] + TOOLBAR_HEIGHT
        pygame.draw.line(screen, color, (cursor_x, cursor_y), (cursor_x, cursor_y + 30), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                brush_size = 2

            elif event.key == pygame.K_2:
                brush_size = 5

            elif event.key == pygame.K_3:
                brush_size = 10

            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = "assets/" + datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            elif text_active:
                if event.key == pygame.K_RETURN:
                    img = text_font.render(text_value, True, color)
                    canvas.blit(img, text_pos)
                    text_active = False
                    text_value = ""

                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                    text_value = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_value = text_value[:-1]

                else:
                    text_value += event.unicode

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[1] < TOOLBAR_HEIGHT:
                    if CLEAR_BUTTON.collidepoint(event.pos):
                        canvas.fill(WHITE)

                    elif PENCIL_BUTTON.collidepoint(event.pos):
                        tool = "pencil"

                    elif ERASER_BUTTON.collidepoint(event.pos):
                        tool = "eraser"

                    elif LINE_BUTTON.collidepoint(event.pos):
                        tool = "line"

                    elif RECT_BUTTON.collidepoint(event.pos):
                        tool = "rect"

                    elif CIRCLE_BUTTON.collidepoint(event.pos):
                        tool = "circle"

                    elif FILL_BUTTON.collidepoint(event.pos):
                        tool = "fill"

                    elif TEXT_BUTTON.collidepoint(event.pos):
                        tool = "text"

                    elif SQUARE_BUTTON.collidepoint(event.pos):
                        tool = "square"

                    elif RIGHT_TRIANGLE_BUTTON.collidepoint(event.pos):
                        tool = "right_triangle"

                    elif EQUILATERAL_BUTTON.collidepoint(event.pos):
                        tool = "equilateral_triangle"

                    elif RHOMBUS_BUTTON.collidepoint(event.pos):
                        tool = "rhombus"

                    elif SMALL_BUTTON.collidepoint(event.pos):
                        brush_size = 2

                    elif MEDIUM_BUTTON.collidepoint(event.pos):
                        brush_size = 5

                    elif LARGE_BUTTON.collidepoint(event.pos):
                        brush_size = 10

                    elif RED_BUTTON.collidepoint(event.pos):
                        color = RED

                    elif GREEN_BUTTON.collidepoint(event.pos):
                        color = GREEN

                    elif BLUE_BUTTON.collidepoint(event.pos):
                        color = BLUE

                    elif BLACK_BUTTON.collidepoint(event.pos):
                        color = BLACK

                    elif YELLOW_BUTTON.collidepoint(event.pos):
                        color = YELLOW

                else:
                    canvas_pos = get_canvas_pos(event.pos)

                    if tool == "fill":
                        tools.flood_fill(canvas, canvas_pos[0], canvas_pos[1], color)

                    elif tool == "text":
                        text_active = True
                        text_pos = canvas_pos
                        text_value = ""

                    else:
                        drawing = True
                        last_pos = canvas_pos
                        start_pos = canvas_pos

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                canvas_pos = get_canvas_pos(event.pos)

                if tool == "pencil":
                    tools.pencil(canvas, color, last_pos, canvas_pos, brush_size)
                    last_pos = canvas_pos

                elif tool == "eraser":
                    tools.eraser(canvas, last_pos, canvas_pos, 25)
                    last_pos = canvas_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if drawing:
                    canvas_pos = get_canvas_pos(event.pos)

                    if tool in ["line", "rect", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus"]:
                        draw_shape(canvas, tool, start_pos, canvas_pos)

                drawing = False
                last_pos = None
                start_pos = None

    pygame.display.update()

pygame.quit()

#2