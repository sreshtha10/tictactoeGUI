import pygame,time,sys

pygame.init()
fps = 60
xo = 'x'
width = 400
height = 400
game_icon = pygame.image.load("images/game_icon.png")
pygame.display.set_icon(game_icon)
winner = None
draw = False
white = (255,255,255)
line_color = (0,0,0)
clock = pygame.time.Clock()
ttt = [[None]*3,[None]*3,[None]*3]

pygame.display.set_caption('Tic Tac Toe')
screen = pygame.display.set_mode((width,height+100),0,32)

x_img = pygame.image.load('images/x.png')
o_img = pygame.image.load('images/o.png')
home_img = pygame.image.load('images/home.png')

x_img = pygame.transform.scale(x_img,(80,80))
o_img = pygame.transform.scale(o_img,(80,80))
home_img = pygame.transform.scale(home_img,(width,height+100))

def homeScreen():
    screen.blit(home_img,(0,0))
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)


    pygame.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pygame.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)

    pygame.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
    pygame.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)

    status()

def status():
    global draw
    if winner is None:
        message = xo.upper()+"'s Turn"
    else:
        message = winner.upper() +" won !"
    if draw:
        message = "Game drawn !"
    font = pygame.font.Font(None,30)
    text = font.render(message,1,(255,255,255))
    screen.fill((0,0,0),(0,400,500,100))
    text_rect = text.get_rect(center = (width/2,500-50))
    screen.blit(text,text_rect)
    pygame.display.update()


def checkWin():
    global ttt,winner, draw

    for row in range(0,3):
        if(ttt[row][0] == ttt[row][1] and ttt[row][1] ==  ttt[row][2] and ttt[row][0] is not None):
            winner = ttt[row][0]
            pygame.draw.line(screen, (250, 0, 0), (0, (row + 1) * height / 3 - height / 6), \
                         (width, (row + 1) * height / 3 - height / 6), 4)
            break

    for col in range(0,3):
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
    if (all([all(row) for row in ttt]) and winner is None):
        draw = True
    status()


def reset():
    global ttt,winner,draw,xo
    time.sleep(3)
    xo = 'x'
    winner = None
    draw = False
    homeScreen()
    ttt = [[None]*3,[None]*3,[None]*3]

def drawXO(row,col):
    global ttt,xo
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
    if (xo == 'x'):
        screen.blit(x_img, (posx, posy))
        xo = '0'
    else:
        screen.blit(o_img,(posx,posy))
        xo = 'x'
    pygame.display.update()

def userClick():
    x,y = pygame.mouse.get_pos()
    if(x<width/3):
        col = 1
    elif(x<(width/3)*2):
        col = 2
    elif( x< width):
        col = 3
    else:
        col = None
    if (y < height / 3):
        row = 1
    elif (y < (height / 3) * 2):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None
    if (row and col and ttt[row - 1][col - 1] is None):
        global xo
        # draw the x or o on screen
        drawXO(row, col)
        checkWin()


homeScreen()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is pygame.MOUSEBUTTONDOWN:
            userClick()
            if(winner or draw):
                reset()

    pygame.display.update()
    clock.tick(fps)





