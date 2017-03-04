"""
Lander Game
Alex
1/4/2017
"""

import pygame
import Lander
import Background

from Config import *

""" Main File consists of game loop  """


class GameLoop:

	def __init__(self, width=WIDTH, height=HEIGHT, fps=FPS):

		pygame.init()

		self.width = width
		self.height = height
		self.fps = fps

		self.screen = pygame.display.set_mode((self.width, self.height))
		self.screen.fill(black)

		self.background = pygame.Surface((self.screen.get_width(), self.screen.get_height()))

		pygame.display.set_caption("Lander Game")
		self.clock = pygame.time.Clock()

	def draw(self):
		Background.mountain(self.background)

	def run(self):

		running = True

		all_sprites = pygame.sprite.Group()

		self.draw()

		lander = Lander.lander()
		all_sprites.add(lander)

		while running:

			self.clock.tick(FPS)

			#   process events

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					running = False

				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
			#   Update

			lander.move()
			all_sprites.update()
			all_sprites.clear(self.screen, self.background)

			#   Draw/render
			all_sprites.draw(self.screen)

			pygame.display.flip()
			self.screen.blit(self.background, (0, 0))

		pygame.quit()

if __name__ == "__main__":

	GameLoop().run()
