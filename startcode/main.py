import pygame
import time
from snake import Snake, veld_grootte
from food import Food

# kleuren
breedte = 800
hoogte = 600
kleur_achtergrond = (0,0,0)
pygame.init()
venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption("snake")

def game_lus():
    snake = Snake(breedte / 2, hoogte / 2)
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.key == pygame.K_LEFT and snake.x_verandering == 0:
                snake.x_verandering = -veld_grootte
                snake.y_verandering = 0
            elif event.key == pygame.K_RIGHT and snake.x_verandering == 0:
                snake.x_verandering = veld_grootte
                snake.y_verandering = 0
            elif event.key == pygame.K_UP and snake.y_verandering == 0:
                snake.y_verandering = -veld_grootte
                snake.x_verandering = 0
            elif event.key == pygame.K_DOWN and snake.y_verandering == 0:
                snake.y_verandering = veld_grootte
                snake.x_verandering = 0
    snake.beweeg()
    venster.fill(kleur_achtergrond)
    snake.teken(venster)
    pygame.display.update()
    time.sleep(1/5)
    pygame.time.wait(5000)
    game_lus()






# Functie om de score op het scherm te tonen

# Hoofdloop van het spel

# Start de hoofdloop van het spel