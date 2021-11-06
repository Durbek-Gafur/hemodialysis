def write(text):
	screen.fill((0,0,0),(0, 400, screen.get_width(), screen.get_height()-200))
	font = pygame.font.Font('freesansbold.ttf', 22)
	text = font.render(text, True, (255,255,255))
	textRect = text.get_rect()
	textRect.center = (400,500)
	screen.blit(text, textRect)