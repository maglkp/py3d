import pygame, sys, math

pygame.init()
w, h = 400, 400
cx, cy = w//2, h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()


verts = (-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1), (-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1)
#verts = (0,1,5), (1,0,5)
edges = (0, 1), (1,2), (2,3), (3,0), (4, 5), (5,6), (6,7), (7,4), (0, 4), (1,5), (2,6), (3,7)

while True:
	dt = clock.tick()/1000

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.fill((225, 225, 225))

	for x, y, z in verts:
		z += 5
		f = 200/z
		x, y = x*f, y*f
		pygame.draw.circle(screen, (0, 0, 0), (cx + int(x), cy + int(y)), 6)

	#pygame.draw.circle(screen, (0, 0, 0), (200, 200), 6)

	# for edge in edges:
	# 	points = []
	# 	for x,y,z in (verts[edge[0]], verts[edge[1]]):
	# 			z += 5
	# 			f = 200/z
	# 			x, y = x*f, y*f
	# 			points += [[cx + int(x), cy + int(y)]]
	# 	pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)


	pygame.display.flip()