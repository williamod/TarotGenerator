import pygame
from card import Card
from settings import *

class FaceCard(Card):
    def __init__(self, group):
        super().__init__(group)
        width = 120
        height = 160