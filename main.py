import pygame, sys, time, random

pygame.init()
fps = 60
xo = 'x'
width = 400
height = 400
game_icon = pygame.image.load("images/game_icon.png")
pygame.display.set_icon(game_icon)
winner = None
draw = False
white = (255, 255, 255)
line_color = (0, 0, 0)
clock = pygame.time.Clock()
ttt = [[None] * 3, [None] * 3, [None] * 3]
mode = None

pygame.display.set_caption('Tic Tac Toe')
screen = pygame.display.set_mode((width, height + 100), 0, 32)

x_img = pygame.image.load('images/x.png')
o_img = pygame.image.load('images/o.png')
home_img = pygame.image.load('images/home.png')
singlePlayer = pygame.image.load('images/singlePlayer.png')
multiPlayer = pygame.image.load('images/multiPlayer.png')

x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(o_img, (80, 80))
home_img = pygame.transform.scale(home_img, (width, height + 100))
singlePlayer = pygame.transform.scale(singlePlayer, (200, 200))
multiPlayer = pygame.transform.scale(multiPlayer, (170, 170))


def home_screen():
    global mode

    screen.blit(home_img, (0, 0))
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)
    pygame.draw.line(screen, line_color, (0, 250), (width, 250), 7)
    screen.blit(singlePlayer, (100, 0))
    screen.blit(multiPlayer, (100, 300))
    pygame.display.update()


def main_screen():
    screen.fill(white)
    pygame.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pygame.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    pygame.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pygame.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    status()


def status():
    global draw
    if winner is None:
        message = xo.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game drawn !"
    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pygame.display.update()


def check_win():
    global ttt, winner, draw

    for row in range(0, 3):
        if ttt[row][0] == ttt[row][1] and ttt[row][1] == ttt[row][2] and ttt[row][0] is not None:
            winner = ttt[row][0]
            pygame.draw.line(screen, (250, 0, 0), (0, (row + 1) * height / 3 - height / 6), \
                             (width, (row + 1) * height / 3 - height / 6), 4)
            break

    for col in range(0, 3):
        if (ttt[0][col] == ttt[1][col] == ttt[2][col]) and (ttt[0][col] is not None):
            # this column won
            winner = ttt[0][col]
            # draw winning line
            pygame.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0), \
                             ((col + 1) * width / 3 - width / 6, height), 4)
            break
    if (ttt[0][0] == ttt[1][1] == ttt[2][2]) and (ttt[0][0] is not None):
        # game won diagonally left to right
        winner = ttt[0][0]
        pygame.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
    if (ttt[0][2] == ttt[1][1] == ttt[2][0]) and (ttt[0][2] is not None):
        # game won diagonally right to left
        winner = ttt[0][2]
        pygame.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
    if all([all(row) for row in ttt]) and winner is None:
        draw = True
    status()


def reset():
    global ttt, winner, draw, xo
    time.sleep(3)
    xo = 'x'
    winner = None
    draw = False
    home_screen()
    ttt = [[None] * 3, [None] * 3, [None] * 3]


def draw_xo(row, col):
    global ttt, xo, posx, posy
    if row == 1:
        posy = 30
    if row == 2:
        posy = width / 3 + 30
    if row == 3:
        posy = width / 3 * 2 + 30
    if col == 1:
        posx = 30
    if col == 2:
        posx = height / 3 + 30
    if col == 3:
        posx = height / 3 * 2 + 30
    ttt[row - 1][col - 1] = xo
    if xo == 'x':
        screen.blit(x_img, (posx, posy))
        xo = '0'
    else:
        screen.blit(o_img, (posx, posy))
        xo = 'x'
    pygame.display.update()


def user_click():
    x, y = pygame.mouse.get_pos()
    if x < width / 3:
        col = 1
        print('h')
    elif x < (width / 3) * 2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None
    if y < height / 3:
        row = 1
    elif y < (height / 3) * 2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None
    if row and col and ttt[row - 1][col - 1] is None:
        global xo
        # draw the x or o on screen
        draw_xo(row, col)
        check_win()


def user_click_single():
    x, y = pygame.mouse.get_pos()
    col = 0
    if x < width / 3:
        col = 1
    elif x < (width / 3) * 2:
        col = 2
    elif x < width:
        col = 3
    else:
        col = None
    if y < height / 3:
        row = 1
    elif y < (height / 3) * 2:
        row = 2
    elif y < height:
        row = 3
    else:
        row = None
    if row and col and ttt[row - 1][col - 1] is None:
        global xo
        # draw the x or o on screen
        draw_xo(row, col)
        check_win()
        a = random.randrange(1, 4)
        b = random.randrange(1, 4)
        while ttt[a - 1][b - 1] is not None:
            a = random.randrange(1, 4)
            b = random.randrange(1, 4)
        draw_xo(a, b)
        check_win()


home_screen()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            main_screen()
            x, y = pygame.mouse.get_pos()
            if y > 250:
                main_screen()
                while True:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif e.type == pygame.MOUSEBUTTONDOWN:
                            user_click()
                            if winner or draw:
                                reset()
                    pygame.display.update()
                    clock.tick(fps)
            if y < 250:
                main_screen()
                while True:
                    for f in pygame.event.get():
                        print(f.type == pygame.MOUSEBUTTONDOWN)
                        if f.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif f.type == pygame.MOUSEBUTTONDOWN:
                            user_click_single()
                            if winner or draw:
                                reset()

                    pygame.display.update()
                    clock.tick(fps)
