#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#installing pygame
get_ipython().system('pip install pygame')


# In[1]:


import pygame
import random
import os


# In[2]:


x = pygame.init()
print(x)


# In[3]:


#Music
pygame.mixer.init()


# In[4]:


#colors
white = [255,255,255]
red = [255,0,0]
black = [0,0,0]
blue = [0,0,255]
green=[0,255,0]
grey = [111,110,105]
pink = [205,92,92]
orange = [255,69,0]
maroon = [128,0,0]
dgreen = [0,100,0]


# In[5]:


#Creating Window
screen_width = 900
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width,screen_height))
#Background Image
bgimg = pygame.image.load('snake2.PNG')
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()


# In[6]:


#Game Title
pygame.display.set_caption("SnakeswithRashda")
pygame.display.update()
#Clock
clock = pygame.time.Clock()
#Score on screen
font = pygame.font.SysFont(None,55)


# In[7]:


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

    


# In[8]:


####WELCOME SCREEN#####
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((205,92,92))
        text_screen("Welcome to Snakes",black,230,210)
        text_screen("Press Space Bar to Play",black,205,270)
        text_screen("By @R.Irshaad",black,10,10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('shukr.mp3.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)


# In[9]:


#creating Game loop
def gameloop():
    #Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    #snake length
    snk_list = []
    snk_length = 1
    #check if high score file exit
    if(not os.path.exists("Hiscore.txt")):
        with open("Hiscore.txt","w")as f:
            f.write("0")
    with open("Hiscore.txt","r") as f:
        Hiscore = f.read()
    #Food
    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    #Score
    score = 0
    snake_size =10
    fps = 60
    while not exit_game:
        if game_over:
            with open("Hiscore.txt","w") as f:
                f.write(str(Hiscore))
            gameWindow.fill(black)
            text_screen("Game Over! Press Enter to Continue",red,100,230)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                    #snake_x = snake_x + 10
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                    #snake_x = snake_x - 10
                         velocity_x = -init_velocity
                         velocity_y = 0
                    if event.key == pygame.K_UP:
                    #snake_y = snake_y - 10
                         velocity_y = -init_velocity
                         velocity_x = 0
                    if event.key == pygame.K_DOWN:
                    #snake_y = snake_y + 10
                         velocity_y = init_velocity
                         velocity_x = 0
                            ######CheatCode######
                    if event.key == pygame.K_q:
                        score+=10
                        #print("You have pressed right arrow key")
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            #score
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score+=10
                #print("Score: ",score * 10)

                food_x = random.randint(20,screen_width/2)
                food_y = random.randint(20,screen_height/2)
                snk_length += 5
                if score > int(Hiscore):
                    Hiscore = score
            gameWindow.fill(grey)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: "+str(score) + "  Hiscore: "+str(Hiscore),dgreen,5,5)
            pygame.draw.rect(gameWindow,maroon,[food_x,food_y,snake_size,snake_size])
            #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('back.mp3.mp3')
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('back.mp3.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow,black,snk_list,snake_size)


        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()


# In[ ]:




