import pygame
def write(screen,text,DIM,color = (255,255,255)):
	# screen.fill((0,0,0),(0, 0, screen.get_width(), screen.get_height()))
	font = pygame.font.Font(None, 35)
	text = font.render(text, True, color)
	textRect = text.get_rect()
	textRect.center = DIM 
	screen.blit(text, textRect)