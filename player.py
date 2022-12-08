import pygame
from sys import exit
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('graphics/player/walk1.png').convert_alpha()
		player_walk_1 = pygame.transform.scale(player_walk_1, (64, 92))
		player_walk_2 = pygame.image.load('graphics/player/walk2.png').convert_alpha()
		player_walk_2 = pygame.transform.scale(player_walk_2, (64, 92))
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
		self.player_jump = pygame.transform.scale(player_walk_2, (64, 92))
		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		try:
			self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
			self.jump_sound.set_volume(0.5)
		except:
			print("Error loading music file")

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
			try:
				self.jump_sound.play()
			except:
				print("No music file")
		if keys[pygame.K_LEFT] and self.rect.x > 0:
			self.rect.left -= 5
		if keys[pygame.K_RIGHT] and self.rect.right < WITH:
			self.rect.right += 5

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
		if self.rect.bottom < 300: 
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()
