import pygame
def write(screen,text,DIM):
	# screen.fill((0,0,0),(0, 0, screen.get_width(), screen.get_height()))
	font = pygame.font.Font('freesansbold.ttf', 35)
	text = font.render(text, True, (255,255,255))
	textRect = text.get_rect()
	textRect.center = DIM 
	screen.blit(text, textRect)