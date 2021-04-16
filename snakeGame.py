import pygame
import random
import os

pygame.mixer.init() #for playing audio


pygame.init() #all modules of pygame

# defining colores
nicecolor=(180,200,245)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

#creating window for game
screen_width=900
screen_height=600
gamewindow=pygame.display.set_mode((screen_width,screen_height))

#background image
background=pygame.image.load("background.jpg")
background=pygame.transform.scale(background,(screen_width, screen_height)).convert_alpha()

#The title of game
pygame.display.set_caption("SnakyyyProtik")
pygame.display.update()

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def screen_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit( screen_text,[x,y])
def plot_snake(gamewindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y , snake_size, snake_size])

def welcome():
    exit_game= False
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play()
    while not exit_game:
        gamewindow.fill((200,245,150))
        screen_score("Welcome To Snakky_Protik",black,180,250)
        screen_score("Press space to start the game",black,165,300)
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('attention.mp3')
                    pygame.mixer.music.play()
                    gameloop()
                    
        pygame.display.update()
        clock.tick(60)


#Gameloop
def gameloop():
        #Game specific Variables opr global variables
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=25 #snake properties

    #food properties
    food_x=random.randint(0,screen_width)
    food_y=random.randint(0,screen_height)

    fps=60
        # velocity
    init_velocity=5
    velocity_x=0 
    velocity_y=0
    score=0
    snake_length=1
    snake_list=[]
    
    if (not os.path.exists('hiscore.txt')):
        with open('hiscore.txt','w') as f:
            f.write("0")
    with open('hiscore.txt', 'r') as f:
        hiscore=f.read()

    while not exit_game:
        if game_over:
            with open('hiscore.txt', 'w') as f:
                f.write(str(hiscore))

            gamewindow.fill(nicecolor)
            screen_score("Game Over! press enter to continue",red,100,250)
            screen_score("Your Score: "+str(score),red,100,300)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                    
                    if event.key==pygame.K_c:
                        score=score+10
                    
            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y


            if abs(snake_x-food_x)<12 and abs(snake_y-food_y)<12:
                score=score+1
                food_x=random.randint(20,screen_width /2)
                food_y=random.randint(20,screen_height /2)
                snake_length=snake_length+5
                if score > int(hiscore):
                    hiscore=score

            gamewindow.fill(nicecolor)
            gamewindow.blit(background,(0,0))
            screen_score("Score : "+ str(score)+ "   Hiscore : "+str(hiscore), red, 5, 5)
            #pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gamewindow,black, snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()