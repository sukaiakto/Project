import pygame
import sys
import time
from pygame.locals import *
from moves import *

pygame.init()
window = pygame.display.set_mode((450, 550))
pygame.display.set_caption("2048")

gray = (120, 120, 120)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
font_text = pygame.font.SysFont(None, 50)
score_num = 0


def build_text(board, i, j):
    if board[j][i] == "0":
        text = font_text.render(" ", True, black)
    else:
        text = font_text.render(board[j][i], True, black)
    text_rect = text.get_rect()
    text_rect.centerx = i * 100 + 75
    text_rect.centery = j * 100 + 180
    return text, text_rect


def show_text(board):
    for i in range(4):
        for j in range(4):
            window.blit(build_text(board, i, j)[0], build_text(board, i, j)[1])


def quit_window(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()


def game_over(score_num):
    window.fill((255, 255, 255))
    label = font_text.render(f"GAME OVER Score: {score_num}", True, red)
    label_rect = label.get_rect()
    label_rect.centerx = window.get_rect().centerx
    label_rect.centery = window.get_rect().centery
    window.blit(label, label_rect)
    event = pygame.event.wait()
    quit_window(event)


def victory(score_num):
    window.fill((255, 255, 255))
    label = font_text.render(f"You WIN! Score: {score_num}", True, red)
    label_rect = label.get_rect()
    label_rect.centerx = window.get_rect().centerx
    label_rect.centery = window.get_rect().centery
    window.blit(label, label_rect)
    event = pygame.event.wait()
    quit_window(event)


def game_loop():
    board = init_board()
    blocks = []
    for i in range(4):
        for j in range(4):
            blocks.append([pygame.Rect((i * 100) + 30, (j * 100) + 135, 90, 90), gray])
    while True:
        for event in pygame.event.get():

            quit_window(event)
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    board = main(board, "u")
                if event.key == K_DOWN:
                    board = main(board, "d")
                if event.key == K_LEFT:
                    board = main(board, "l")
                if event.key == K_RIGHT:
                    board = main(board, "r")
                if event.key == K_r:
                    board = main(board, "rest")
                if event.key == K_z:
                    board = main(board, "win")

        window.fill((255, 255, 255))
        pygame.draw.rect(window, (240, 240, 240), pygame.Rect(20, 20, 410, 100))
        score_num = score(board)
        header = font_text.render(f"Score:  {score_num}", True, black)
        window.blit(header, (30, 50))
        pygame.draw.rect(window, black, pygame.Rect(20, 125, 410, 410))

        for block in blocks:
            pygame.draw.rect(window, block[1], block[0])
        show_text(board)

        if lose(board):
            game_over(score_num)
        elif win(board):
            victory(score_num)

        pygame.display.update()

        time.sleep(0.02)


game_loop()
