import pygame
from sys import exit
from random import choice
from player import Player
from obstacle import Obstacle
from settings import *
import time


def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time

	'''
	Formatação de string para representação de texto com valor com base numa variavel de tipo numérico (Critério de Correção 2)
	'''
	score_surf = test_font.render(f'Pontuação: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time

def display_best_scores(number):
	unique_scores = list(set(scores_list))
	unique_scores.sort(reverse=True)
	
	print(unique_scores)

	if len(unique_scores) > 1:
		best_scores = test_font.render("Os seus melhores resultados:",False,(111,196,169))
		best_scores_rect = score_message.get_rect(center = (320,230))
		pos_y = 270
		delta_y = 45
		
		if len(unique_scores) >= 3:
			for s in range(3):
				score1 = test_font.render(f'{s + 1}º - {unique_scores[s]}', False,(111,196,169))
				score1_rect = score1.get_rect(center = (390,pos_y))
				screen.blit(best_scores,best_scores_rect)
				screen.blit(score1,score1_rect)
				pos_y += delta_y
		else:
			for s in range(len(unique_scores)):
				score1 = test_font.render(f'{s + 1}º - {unique_scores[s]}', False,(111,196,169))
				score1_rect = score1.get_rect(center = (390,pos_y))
				screen.blit(best_scores,best_scores_rect)
				screen.blit(score1,score1_rect)
				pos_y += delta_y

		'''
		O código em cima poderia ser otimizado através da utilização de um ternary operator, evitando a duplicação do código para desenho no ecrã
		'''
		'''
		range_scores = range(3) if len(unique_scores) >= 3 else range(len(unique_scores))
		for s in range_scores:
			score1 = test_font.render(f'{s + 1}º - {unique_scores[s]}', False,(111,196,169))
			score1_rect = score1.get_rect(center = (390,pos_y))
			screen.blit(best_scores,best_scores_rect)
			screen.blit(score1,score1_rect)
			pos_y += delta_y
		'''
	else:
		pass	


def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True

pygame.init()
screen = pygame.display.set_mode((WITH,HEIGHT))
pygame.display.set_caption('Jump\'N\'Run')
GAME_ICON = pygame.image.load("graphics/Player/jump.png")
pygame.display.set_icon(GAME_ICON)
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

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

obstacle_rect_list = []

scores_list = []

# Ecrã inicial
player_stand = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand , (128, 184))
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
			if event.type == obstacle_timer:

				'''
				Chamada de função de inicialização da instância da classe (objeto). Passa como parâmetro o tipo de obstáculo (type) - (Critério de Correção 8)
				Criação de Array (Critério de Correção 9)
				'''
				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				
				'''
				Passagem para número inteiro de resultado com valor float (Critério de Correção 2)
				'''
				start_time = int(pygame.time.get_ticks() / 1000)

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
		if not game_active:
			scores_list.append(score)		
	else:
		screen.fill((94,129,162))
		
		obstacle_rect_list.clear()
		#player_rect.midbottom = INITIAL_PLAYER_POS
		player_gravity = 0
		score_message = test_font.render(f'A sua pontuação: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,150))
		screen.blit(game_name,game_name_rect)
		
		
		if score == 0: 
			screen.blit(game_message,game_message_rect)
			screen.blit(player_stand, player_stand_rect)
		else: 
			screen.blit(score_message,score_message_rect)
			display_best_scores(3)

	pygame.display.update()
	clock.tick(60)
