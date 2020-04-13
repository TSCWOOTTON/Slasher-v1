import pygame
import math

pygame.init()

# General
display_width = 600
display_height = 800
background = pygame.image.load("background.png")
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SLASHR")
pygame.display.set_icon(pygame.image.load("knifeart.png"))
knife_art = pygame.image.load("knifeart.png")

# Global variables
kill_counter = 0
sharpened = 1
falling_teens = 0


# Functions
def counter():
    font = pygame.font.Font("freesansbold.ttf", 52)
    crimson = (220, 20, 60)
    global kill_counter
    kill_counter += 0.25 * falling_teens
    int(kill_counter)
    screen.blit(font.render("Kill Count: " + str(kill_counter), True, crimson), (0, 10))


def bubble():
    global kill_counter
    global sharpened
    orange = (255, 165, 0)
    dark_orange = (255, 140, 0)
    bubble_color = dark_orange
    bubble_x = 300
    bubble_y = 400
    bubble_pos = (bubble_x, bubble_y)
    bubble_rad = 100
    mouse_x, mouse_y = pygame.mouse.get_pos()
    distance = math.hypot(bubble_x - mouse_x, bubble_y - mouse_y)
    if bubble_rad >= distance:
        bubble_color = orange
    if bubble_rad >= distance and event.type == pygame.MOUSEBUTTONDOWN:
        kill_counter += 1 * sharpened
        pygame.time.wait(50)
    pygame.draw.circle(screen, bubble_color, bubble_pos, bubble_rad)


def knife():
    knife = pygame.image.load("knifeart.png")
    knife = pygame.transform.scale(knife, (100, 100))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    bubble_rad = 100
    bubble_x = 300
    bubble_y = 400
    distance = math.hypot(bubble_x - mouse_x, bubble_y - mouse_y)
    if bubble_rad >= distance and event.type == pygame.MOUSEBUTTONDOWN:
        knife = pygame.transform.scale(knife, (150, 150))
        screen.blit(knife, (230, 310))
    else:
        screen.blit(knife, (260, 325))


def shop_1():
    global sharpened
    global kill_counter
    orange = (255, 165, 0)
    dark_orange = (255, 140, 0)
    box_x = 1
    box_y = 700
    box_width = 300
    box_height = 100
    crimson = (220, 20, 60)
    font = pygame.font.Font("freesansbold.ttf", 22)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if box_x < mouse_x < box_x + box_width and box_y < mouse_y < box_y + box_height and event.type == pygame.MOUSEBUTTONDOWN and kill_counter >= 300:
        sharpened += 1
        kill_counter -= 300
        pygame.time.wait(50)
    if box_x < mouse_x < box_x + box_width and box_y < mouse_y < box_y + box_height:
        pygame.draw.rect(screen, orange, (box_x, box_y, box_width, box_height), 0)
    else:
        pygame.draw.rect(screen, dark_orange, (box_x, box_y, box_width, box_height), 0)
    screen.blit(font.render("SHARPEN YOUR WEAPON", True, crimson), (box_x, box_y))
    screen.blit(font.render("COST = 300 KILLS", True, crimson), (box_x, box_y + 25))
    screen.blit(font.render("SHARPENED X" + str(sharpened), True, crimson), (box_x, box_y + 50))


def shop_2():
    global falling_teens
    global kill_counter
    orange = (255, 165, 0)
    dark_orange = (255, 140, 0)
    box_x = 300
    box_y = 700
    box_width = 300
    box_height = 100
    crimson = (220, 20, 60)
    font = pygame.font.Font("freesansbold.ttf", 22)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if box_x < mouse_x < box_x + box_width and box_y < mouse_y < box_y + box_height and event.type == pygame.MOUSEBUTTONDOWN and kill_counter >= 150:
        falling_teens += 1
        kill_counter -= 150
        pygame.time.wait(50)
    if box_x < mouse_x < box_x + box_width and box_y < mouse_y < box_y + box_height:
        pygame.draw.rect(screen, orange, (box_x, box_y, box_width, box_height), 0)
    else:
        pygame.draw.rect(screen, dark_orange, (box_x, box_y, box_width, box_height), 0)
    screen.blit(font.render("SHARPEN YOUR WEAPON", True, crimson), (box_x, box_y))
    screen.blit(font.render("COST = 150 KILLS", True, crimson), (box_x, box_y + 25))
    screen.blit(font.render("FALLING TEENS X" + str(falling_teens), True, crimson), (box_x, box_y + 50))


# Game Loop
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    counter()
    bubble()
    knife()
    shop_1()
    shop_2()
    pygame.display.update()
