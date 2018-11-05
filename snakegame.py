# snake game
# our game imports
import sys,random,pygame,time
# for adding sounds
#pygame.mixer.pre_init(44100,16,2,4096)
check_errors=pygame.init()
if check_errors[1]>0:
    print("had {} errors"
          ".........exiting".format(check_errors))
    sys.exit(-1)
else:
    print("pygame sucessfully installed")

# Play surface
playSurface=pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake game!")
#colors
red=pygame.Color(250,0,0) # gameover
green=pygame.Color(0,250,0) # snake
black=pygame.Color(0,0,0) # score
white=pygame.Color(250,250,250)  # background
brown=pygame.Color(165,42,42)  # food

#pygame.mixer.music.load('but.mp3')
#pygame.mixer.music.set_volumne(0.5)
#pygame.mixer.music.play(-1)
# FPS  controller
fpsController =pygame.time.Clock()# to set the speed

# important variables

snakePos =[100,50]
snakeBody =[[100,50],[90,50],[80,50]]

foodPos =[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn =True

direction = 'RIGHT'
changeto = direction

score =0
# game over function
def gameOver():
    myFont=pygame.font.SysFont('monaco',60)
    GOsurf = myFont.render('GameOver !',True,red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,15)
    playSurface.blit(GOsurf,GOrect)
    pygame.display.update()
    showScore(0)
    pygame.display.flip()

    time.sleep(4)
    pygame.quit() # pygame exit
    sys.exit()  # console exit

def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco',24)
    Ssurf = sFont.render('Score : {}'.format(score),True,black)
    Srect=Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80,10)
    else:
        Srect.midtop = (360,120)

    playSurface.blit(Ssurf,Srect)
# Main Logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame. K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
            direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -=10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] +=10

     # Snake body mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0]==foodPos[0] and snakePos[1] == foodPos[1]:
        score += 10
        foodSpawn =False
    else:
        snakeBody.pop()

    if  foodSpawn == False:
        foodPos =[random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True

    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface,green,
        pygame.Rect(pos[0],pos[1],10,10))
        pygame.draw.rect(playSurface,brown,
        pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0]>710 or snakePos[0]<0 :
        snakePos[0]=0
    if snakePos[1] >450 or snakePos[1] <0 :
        snakePos[1]=450
    for segments in snakeBody[1:]:
        if snakePos[0] == segments[0] and snakePos[1] == segments[1]:
            gameOver()
#common stuff
    pygame.display.update()
    showScore()
    pygame.display.flip()
    fpsController.tick(25)
gameOver()











































