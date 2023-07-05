import pygame
import random
import os

pygame.mixer.init()

x = pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#Creating Window
screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_score(text, color, x, y):
	screen_text = font.render(text, True, color)
	gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
	for x,y in snk_list:
		pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
	exit_game = False
	while not exit_game:
		gameWindow.fill((233, 220, 229))
		text_score("Welcome to Snakes", black, 260, 250)
		text_score("Press Space Bar to Play", black, 230, 300)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_SPACE or event.key==pygame.K_RETURN:
					gameloop()

		pygame.display.update()
		clock.tick(60)

def gameloop():
	exit_game = False
	game_over = False
	snake_x = 45
	snake_y = 55
	velocity_x = 0
	velocity_y = 0
	snake_size = 20
	snk_list = []
	snk_length = 1

	if not os.path.exists("highscore.txt"):
		with open ("highscore.txt", "w") as f:
			f.write("0")

	with open("highscore.txt", "r") as f:
		highscore = f.read()

	score=0
	init_velocity = 5

	food_x = random.randint(20,screen_width/2)
	food_y = random.randint(20,screen_height/2)

	fps = 60

	while not exit_game:
		if game_over:

			with open("highscore.txt", "w") as f:
				f.write(str(highscore))


			gameWindow.fill(white)
			text_score("Game Over! Press Enter to Continue", red, 120, 250)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True;

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						welcome()

		else:	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True;

				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RIGHT:
						velocity_x = init_velocity
						velocity_y = 0

					if event.key==pygame.K_LEFT:
						velocity_x = -init_velocity
						velocity_y = 0
					
					if event.key==pygame.K_DOWN:
						velocity_y = init_velocity
						velocity_x = 0

					if event.key==pygame.K_UP:
						velocity_y = -init_velocity
						velocity_x = 0

					if event.key == pygame.K_q:
						score+=5	

			snake_x += velocity_x
			snake_y += velocity_y						

			if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
				score+=10
				food_x = random.randint(20,screen_width/2)
				food_y = random.randint(20,screen_height/2)
				snk_length += 5
				if score>int(highscore):
					highscore=score

			gameWindow.fill(white)	
			text_score("Score: "+str(score)+" highscore: "+str(highscore), red, 5, 5)
			pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


			head = []
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)

			if len(snk_list)>snk_length:
				del snk_list[0]

			first = snk_list[0]
			if first in snk_list[1:]:
				game_over=True

			if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
				game_over = True	

			plot_snake(gameWindow, black, snk_list, snake_size)

		pygame.display.update()
		clock.tick(fps)


	pygame.quit()
	quit()	

welcome()





