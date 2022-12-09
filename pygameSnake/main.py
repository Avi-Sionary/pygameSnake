### Snake Game

import pygame, sys
import random
import time

# Check for initialization errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) {} initializing errors".format(check_errors[1]))
    sys.exit()
else:
    print("PyGame successfully initialized")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game")

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

fpsController = pygame.time.Clock()

# Snake
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]] # the blocks "behind" the snake head

# Food
foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10] # Make it divisible by 10
foodSpawn = True

# Movement
direction = "RIGHT"
changeTo = direction

stopGame = False
score = 0

# Game over
def gameOver():
    myFont = pygame.font.SysFont('Mario64Regular.ttf', 72)
    gameOverSurface = myFont.render("Game Over!", True, red)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (360, 20)
    playSurface.fill(white)
    playSurface.blit(gameOverSurface, gameOverRect)
    showScore(0)
    pygame.display.flip()
    time.sleep(10)
    pygame.quit()
    sys.exit()

# Score display
def showScore(choice = 1):
    scoreFont = pygame.font.SysFont('Mario64Regular.ttf', 56)
    scoreSurface = scoreFont.render('Score: ' + str(score), True, black)
    scoreRect = scoreSurface.get_rect()
    if choice == 1:
        scoreRect.midtop = (80, 20)
    else:
        scoreRect.midtop = (360, 80)
    playSurface.blit(scoreSurface, scoreRect)

while True:

    if not stopGame:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'): # ord gives us ASCII of character
                    changeTo = "RIGHT"
                if event.key == pygame.K_LEFT or event.key == ord('a'): # ord gives us ASCII of character
                    changeTo = "LEFT"
                if event.key == pygame.K_UP or event.key == ord('w'): # ord gives us ASCII of character
                    changeTo = "UP"
                if event.key == pygame.K_DOWN or event.key == ord('s'): # ord gives us ASCII of character
                    changeTo = "DOWN"
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT)) # create an event

        # validation of direction
        if changeTo == "RIGHT" and not direction == "LEFT":
            direction = "RIGHT"
        if changeTo == "LEFT" and not direction == "RIGHT":
            direction = "LEFT"
        if changeTo == "UP" and not direction == "DOWN":
            direction = "UP"
        if changeTo == "DOWN" and not direction == "UP":
            direction = "DOWN"

        if direction == "RIGHT":
            snakePos[0] += 10
        if direction == "LEFT":
            snakePos[0] -= 10
        if direction == "UP":
            snakePos[1] -= 10
        if direction == "DOWN":
            snakePos[1] += 10

        # Snake body mechanism
        snakeBody.insert(0, list(snakePos))
        if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
            score += 1
            foodSpawn = False
        else:
            snakeBody.pop()

        # Position food
        if foodSpawn == False:
            foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
        foodSpawn = True

        playSurface.fill(white)

        # Draw snake
        for pos in snakeBody:
            snakeBlock = pygame.Rect(pos[0], pos[1], 10, 10)
            pygame.draw.rect(playSurface, green, snakeBlock)

        # Draw food
        foodBlock = pygame.Rect(foodPos[0], foodPos[1], 10, 10)
        pygame.draw.rect(playSurface, brown, foodBlock)

        # Window bounds
        if snakePos[0] > 720 or snakePos[0] < 0:
            stopGame = True
        if snakePos[1] > 450 or snakePos[1] < 0:
            stopGame = True

        # Self-hit
        for block in snakeBody[1:]:
            if snakePos[0] == block[0] and snakePos[1] == block[1]:
                stopGame = True

    else:
        gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(25)
