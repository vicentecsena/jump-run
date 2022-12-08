import pygame
from sys import exit
from random import choice
from player import Player
from obstacle import Obstacle
from settings import *


def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time

	'''
	Formatação de string para representação de texto com valor com base numa variavel de tipo numérico (Critério de Correção 2)
	'''
	score_surf = test_font.render(f'Pontuação: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True

def player_animation():
	global player_surf, player_index

	if player_rect.bottom < 300:
		player_surf = player_jump
	else:
		player_index += 0.1
		if player_index >= len(player_walk): player_index = 0
		player_surf = player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((WITH,HEIGHT))
pygame.display.set_caption('Jump\'N\'Run')
clock = pygame.time.Clock()
#Não foi possível utilizar a fonte original, não suporta caracteres portugues (com acentos)
#test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0

try:
	# Fonte do ficheiro: https://pixabay.com/music/electronic-let-the-games-begin-21858/
	bg_music = pygame.mixer.Sound('audio/let-the-games-begin-21858.mp3')
	bg_music.play(loops = -1)
except:
	print("Error loading music file")

#Grupos
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Caracol
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

# Mosca
fly_frame1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk_1 = pygame.transform.scale2x(pygame.image.load('graphics/player/walk1.png').convert_alpha())
player_walk_2 = pygame.transform.scale2x(pygame.image.load('graphics/player/walk2.png').convert_alpha())
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = INITIAL_PLAYER_POS)
player_gravity = 0


# Ecrã inicial
player_stand = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand , (64, 92))
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Jump\'N\'Run',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Carregue na tecla de Espaço para iniciar',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

'''
Execução permanente, com verificação de input do utilizador ou do estado da aplicação (Critério de Correção 7)
'''
while True:
	for event in pygame.event.get():

		'''
		Estrutura de decisão para determinar evento a realizar (Critério de Correção 5)

		Verificação de input do utilizador (Critério de Correção 10)
		'''
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		
		if game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
					player_gravity = -20
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
					player_gravity = -20
				if event.key == pygame.K_LEFT and player_rect.left >= 0:
					player_rect.move(player_rect.x-5, player_rect.y)
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				

				'''
				Passagem para número inteiro de resultado com valor float (Critério de Correção 2)
				'''
				start_time = int(pygame.time.get_ticks() / 1000)

		if game_active:
			if event.type == obstacle_timer:

				'''
				Chamada de função de inicialização da instância da classe (objeto). Passa como parâmetro o tipo de obstáculo (type) - (Critério de Correção 8)
				Criação de Array (Critério de Correção 9)
				'''
				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))

			if event.type == snail_animation_timer:
				if snail_frame_index == 0: snail_frame_index = 1
				else: snail_frame_index = 0

				'''
				Leitura de Array (Critério de Correção 9)
				'''
				snail_surf = snail_frames[snail_frame_index] 

			if event.type == fly_animation_timer:
				if fly_frame_index == 0: fly_frame_index = 1
				else: fly_frame_index = 0
				fly_surf = fly_frames[fly_frame_index] 


	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))

		score = display_score()

		# Player 
		player.draw(screen)
		player.update()

		# obstáculo
		obstacle_group.draw(screen)
		obstacle_group.update()

		# colisão
		game_active = collision_sprite()
		
	else:
		screen.fill((94,129,162))
		screen.blit(player_stand,player_stand_rect)
		obstacle_rect_list.clear()
		player_rect.midbottom = INITIAL_PLAYER_POS
		player_gravity = 0

		score_message = test_font.render(f'A sua pontuação: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		screen.blit(game_name,game_name_rect)

		if score == 0: screen.blit(game_message,game_message_rect)
		else: screen.blit(score_message,score_message_rect)

	pygame.display.update()
	clock.tick(60)
