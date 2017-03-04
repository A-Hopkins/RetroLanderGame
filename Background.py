"""
Lander Game
Alex
1/5/2017
"""

import pygame
import random

from collections import namedtuple

from Config import *

""" Background class used to draw platforms and mountain terrain. """


class mountain:

	def __init__(self, background):

		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.background = background

		self.Platform = namedtuple('Platform', ['start', 'end', 'height'])
		self.Point = namedtuple('Point', ['x', 'y'])

		GaussianDistribution = namedtuple('GaussianDistribution', ['mu', 'sigma'])

		self.PLATFORM_HEIGHT_DISTRIBUTION = GaussianDistribution(50, 10)
		self.PLATFORM_WIDTH_DISTRIBUTION = GaussianDistribution(100, 10)
		self.INTER_PLATFORM_DISTRIBUTION = GaussianDistribution(500, 20)

		self.RANDOM = random.Random()

		platforms = list(self.create_platforms(num_platforms=random.randint(1, 10)))
		terrain = self.create_terrain(platforms)

		self.draw_terrain(terrain)

	def create_platforms(self, num_platforms):

		last_platform_end = 0

		for i in range(num_platforms):

			start = int(self.sample_distribution(self.INTER_PLATFORM_DISTRIBUTION) + last_platform_end)
			end = int(self.sample_distribution(self.PLATFORM_WIDTH_DISTRIBUTION) + start)
			height = HEIGHT - int(self.sample_distribution(self.PLATFORM_HEIGHT_DISTRIBUTION))

			last_platform_end = end
			yield self.Platform(start, end, height)

	def create_mountains_between_points(self, p1, p2):

		mountain_start = p1.x
		mountain_end = p2.x

		num_points = int((mountain_end - mountain_start) / 10)

		for i in range(num_points):
			# TODO: use 1D Perlin function to generate point.y
			yield self.Point(mountain_start + i * 10, HEIGHT - self.RANDOM.random() * 100)

	def create_terrain(self, platforms):

		origin = self.Point(0, 0)
		first_platform_start = self.Point(platforms[0].start, platforms[0].height)

		terrain = []
		terrain += list(self.create_mountains_between_points(origin, first_platform_start))

		for i, platform in enumerate(platforms):
			platform_starts_at = self.Point(platform.start, platform.height)
			platform_ends_at = self.Point(platform.end, platform.height)

			terrain.append(platform_starts_at)
			terrain.append(platform_ends_at)

			if i < len(platforms) - 1:
				next_platform = platforms[i + 1]
				next_platform_starts_at = self.Point(next_platform.start, next_platform.height)
				mountains = self.create_mountains_between_points(platform_ends_at, next_platform_starts_at)
				terrain += mountains

		return terrain

	def draw_terrain(self, terrain):

		return pygame.draw.lines(self.background, white, False, terrain, 2)

	def sample_distribution(self, distribution):

		return self.RANDOM.normalvariate(distribution.mu, distribution.sigma)
