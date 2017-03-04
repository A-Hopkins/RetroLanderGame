"""
Lander Game
Alex
1/4/2017
"""

import pygame

from math import *
from Config import *

""" Class to handle all things related to the Lander, ie: sprite, movement, collision... """


class lander(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("lander.png").convert()
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)

		self.speed_x = 0
		self.speed_y = 0

	def move(self):

		pressed_keys = pygame.key.get_pressed()

		self.speed_x = 0
		self.speed_y = (1.5 / float(self.rect.centery / self.rect.centery ** 2)) / 85

		if pressed_keys[pygame.K_RIGHT]:
			self.speed_x = 5

		if pressed_keys[pygame.K_LEFT]:
			self.speed_x = -5

		if pressed_keys[pygame.K_UP]:
			self.speed_y = -5

		if pressed_keys[pygame.K_DOWN]:
			self.speed_y = 5

		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

		if self.rect.left > WIDTH:
			self.rect.right = 0
		if self.rect.right < 0:
			self.rect.left = WIDTH
		if self.rect.top < 0:
			self.rect.bottom = HEIGHT
		if self.rect.bottom > HEIGHT:
			self.rect.top = 0
