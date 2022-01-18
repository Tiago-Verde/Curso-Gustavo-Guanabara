# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3
import pygame 

pygame.init()

pygame.mixer.music.load('Bass.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait



