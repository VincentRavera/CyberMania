from src.music.Music import Music
import pygame

'''Music Player'''
music = Music('music/Spacecrusher.ogg')

'''FPSClock'''
fpsClock = pygame.time.Clock()

'''Shut Down Signal'''
isRunning = True
