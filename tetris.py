import pygame

pygame.init()
S_WIDTH, S_HEIGHT = 250, 850
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
clock = pygame.time.Clock()
running = True


COLORS = [(0,0,0),(250,250,250),(250,0,0)]

Li_shape = [[[1],[1],[1],[1],[1]],#|
            [[1,1,1,1,1]]]#--




G_LINES = 17
G_COLUMNS = 5
game_area = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]


x_pos = G_COLUMNS//2
y_pos = 0


def draw_game_area():
    for i in range(len(game_area)):
        for j in range (len(game_area[i])):
            if game_area[i][j] == 0:
                pygame.draw.rect(screen, COLORS[game_area[i][j]], ((j*50) , (i*50) , (j*50)+50 , (i*50)+50 ))
            else:
                pygame.draw.rect(screen, COLORS[game_area[i][j]], ((j*50) , (i*50) , (j*50)+50 , (i*50)+50 ))


def shape_position(shape,game):
    global x_pos
    global y_pos

    game[y_pos][x_pos] = 1
    for i in range(len(game_area)):
        for j in range (len(game_area[i])):

    if collision():
        y_pos+=1

def collision():
    print(y_pos)
    if y_pos >= G_LINES-1 or x_pos >= G_COLUMNS-1:
        return False
    else:
        return True


# draw_shapes(Li_shape,game_area,x_pos,y_pos)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    shape_position(Li_shape,game_area)
    draw_game_area()
    pygame.display.flip()

    clock.tick(60)  # Limite à 60 FPS


pygame.quit()