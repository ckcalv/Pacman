import pygame
import math
import copy
import pygame_gui


pygame.init()
# Dimensions of the game screen
width = 900
height = 950
screen = pygame.display.set_mode([width, height])
timer = pygame.time.Clock()
fps = 60
# Height divided by 32 as 50 pixels are left for score and level
num1 = 900 // 32
# Width (900) divided by 30
num2 = 30
num3 = 16
# A 2D array used to map out the design
level = [
   [6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
   [3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
   [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
   [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
   [3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
   [3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
   [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
   [3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
   [3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
   [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
   [3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
   [3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
   [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
   [8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
   [4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
   [4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
   [5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
   [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
   [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
   [3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
   [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
   [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
   [3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
   [3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
   [3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
   [3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
   [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
   [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
   [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
   [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
   [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
   [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
]


baseLevel = copy.deepcopy(level)


lives = 1
levels = 1
scores = 0
gameCount = 0
levelComplete = False
gameRunning = False
gameScreen = 'menu'


# Font used for headers
titleFont = pygame.font.SysFont('arial', 70)
# Text for title header
titleText = titleFont.render("PacMan", True, 'Yellow')
# Text for speed selection header
speedText = titleFont.render("Select Speed", True, 'Yellow')
# Images to be usd for the other screens
screenModel = pygame.transform.scale(pygame.image.load(f'player_model/{1}.png'), (200, 200))
# Font used for descriptions
infoFont = pygame.font.SysFont('arial', 35)
# Text for game over/won header
gameOverText = titleFont.render("Game Over", True, 'Yellow')
gameWonText = titleFont.render("Game Complete", True, 'Yellow')








class Game:
   def __init__(self):
       self.width = 900
       self.height = 950
       # Sets font type for score and level text
       self.font = pygame.font.SysFont('arial', 20)
       # Sets colour for walls of the map
       self.colour = self.levelColour()


   def levelColour(self):
       if 4 < levels < 10:
           self.colour = 'dark red'
       elif 9 < levels < 15:
           self.colour = 'aquamarine3'
       elif 14 < levels < 20:
           self.colour = 'darkgoldenrod2'
       elif levels == 20:
           self.colour = 'purple'
       else:
           self.colour = 'blue'
       return self.colour


   # Subroutine to draw each item
   def drawMap(self):
       global levels
       # Nested for loops to iterate through the array level
       for i in range(len(level)):
           for j in range(len(level[i])):
               if level[i][j] == 1:  # Draws all dots
                   pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 3)
               elif level[i][j] == 2:  # Draws all power pellets
                   pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 9)
               elif level[i][j] == 3:  # Draws all vertical lines
                   pygame.draw.line(screen, self.colour, (j * num2 + (0.5 * num2), i * num1),
                                    (j * num2 + (0.5 * num2), i * num1 + num1), 4)
               elif level[i][j] == 4:  # Draws all horizontal lines
                   pygame.draw.line(screen, self.colour, (j * num2, i * num1 + (0.5 * num1)),
                                    (j * num2 + num2, i * num1 + (0.5 * num1)), 4)
               elif level[i][j] == 5:  # Draws all top right corners
                   pygame.draw.arc(screen, self.colour,
                                   [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1], 0,
                                   math.pi / 2, 3)
               elif level[i][j] == 6:  # Draws all top left corners
                   pygame.draw.arc(screen, self.colour,
                                   [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], math.pi / 2,
                                   math.pi, 3)
               elif level[i][j] == 7:  # Draws all bottom left corners
                   pygame.draw.arc(screen, self.colour,
                                   [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], math.pi,
                                   3 * math.pi / 2, 3)
               elif level[i][j] == 8:  # Draws all bottom right corners
                   pygame.draw.arc(screen, self.colour,
                                   [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1],
                                   3 * math.pi / 2, 2 * math.pi, 3)
               elif level[i][j] == 9:  # Draws ghost barrier
                   pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                    (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
               elif level[i][j] == 10:  # Draws all power pellets
                   pygame.draw.circle(screen, 'blue', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 9)


   def updateUI(self):
       # Draws score onto screen
       scoreText = self.font.render(f'Score: {scores}', True, 'white')
       screen.blit(scoreText, (10, 920))
       # Draws level onto screen
       levelText = self.font.render(f'Level: {levels}', True, 'white')
       screen.blit(levelText, (650, 920))
       # During a power up display a blue circle next to the score
       if player.powerUp:
           pygame.draw.circle(screen, 'blue', (140, 930), 15)
       # Display player icons representing the number of lives on the bottom right of the screen
       for i in range(lives):
           screen.blit(pygame.transform.scale(player.playerModel[0], (25, 25)), (750 + i * 40, 915))




game = Game()




class Player:
   # All variables needed that are related to player
   def __init__(self):
       self.playerX: int = 430
       self.playerY: int = 665
       self.playerWidth = 35
       # Determines player speed which can be altered
       self.playerSpeed = 3
       # Creating a list and appending images onto it representing the pacman model
       self.playerModel = []
       for i in range(1, 4):
           self.playerModel.append(pygame.transform.scale(pygame.image.load(f'player_model/{i}.png'), (35, 35)))
       # Variable to determine direction player is facing
       self.direction = 0
       # Variable for how fast program cycles through images
       self.counter = 0
       self.centreX = self.playerX + 23
       self.centreY = self.playerY + 24
       self.width = 900
       self.height = 950
       self.directionInput = 0
       self.score = 0
       self.powerUp = False
       self.powerCount = 0
       self.ghostsEaten = [False, False, False, False]


   # Subroutine that draws model and each elif statement represents a different direction it can face
   def drawPlayer(self):
       # 0 is right 1 is left 2 is up 3 is down
       if self.direction == 0:
           # Draws base png of pacman which faces right and cycles through the images creating the animation
           screen.blit(self.playerModel[self.counter // 4 % len(self.playerModel)], (self.playerX, self.playerY))
       elif self.direction == 1:
           # FLips the base images making pacman face left
           screen.blit(pygame.transform.flip(self.playerModel[self.counter // 4 % len(self.playerModel)], True, False),
                       (self.playerX, self.playerY))
       elif self.direction == 2:
           # Rotates the base images by 90 degrees making it face up
           screen.blit(pygame.transform.rotate(self.playerModel[self.counter // 4 % len(self.playerModel)], 90),
                       (self.playerX, self.playerY))
       elif self.direction == 3:
           # Rotates the base images by 270 degrees making it face down
           screen.blit(pygame.transform.rotate(self.playerModel[self.counter // 4 % len(self.playerModel)], 270),
                       (self.playerX, self.playerY))


   def checkPos(self):
       self.validTurn = [False, False, False, False]
       # check collisions based on centre x and centre y of player and num3
       # check if player is within boundaries of the screen
       if self.centreX // 30 < 29:
           # if going right it will check piece to the left and if it isn't a wall set the left direction to true
           if self.direction == 0:
               if level[self.centreY // num1][(self.centreX - num3) // num2] < 3:
                   self.validTurn[1] = True
           # if going left it will check piece to the right and if it isn't a wall set the right direction to true
           if self.direction == 1:
               if level[self.centreY // num1][(self.centreX + num3) // num2] < 30:
                   self.validTurn[0] = True
           # if going up it will check piece to the down and if it isn't a wall set the down direction to true
           if self.direction == 2:
               if level[(self.centreY + num3) // num1][self.centreX // num2] < 3:
                   self.validTurn[3] = True
           # if going down it will check piece to the up and if it isn't a wall set the up direction to true
           if self.direction == 3:
               if level[(self.centreY - 18) // num1][self.centreX // num2] < 3:
                   self.validTurn[2] = True


           # Checks whether player is roughly in the centre of a square
           if self.direction == 2 or self.direction == 3:
               if 12 <= self.centreX % num2 <= 18:
                   if level[(self.centreY + num3) // num1][self.centreX // num2] < 3:
                       self.validTurn[3] = True
                   if level[(self.centreY - 18) // num1][self.centreX // num2] < 3:
                       self.validTurn[2] = True
               if 12 <= self.centreY % num1 <= 18:
                   if level[self.centreY // num1][(self.centreX - num2) // num2] < 3:
                       self.validTurn[1] = True
                   if level[self.centreY // num1][(self.centreX + num2) // num2] < 3:
                       self.validTurn[0] = True
           if self.direction == 0 or self.direction == 1:
               if 12 <= self.centreX % num2 <= 18:
                   if level[(self.centreY + num1) // num1][self.centreX // num2] < 3:
                       self.validTurn[3] = True
                   if level[(self.centreY - num1) // num1][self.centreX // num2] < 3:
                       self.validTurn[2] = True
               if 12 <= self.centreY % num1 <= 18:
                   if level[self.centreY // num1][(self.centreX - num3) // num2] < 3:
                       self.validTurn[1] = True
                   if level[self.centreY // num1][(self.centreX + num3) // num2] < 3:
                       self.validTurn[0] = True
       # Left and right are set to true as it would mean they are in the warp tunnel
       else:
           self.validTurn[0] = True
           self.validTurn[1] = True


       return self.validTurn


   def playerMovement(self):
       if self.validTurn[0] and self.direction == 0:  # Move right
           self.playerX += self.playerSpeed
       elif self.validTurn[1] and self.direction == 1:  # Move left
           self.playerX -= self.playerSpeed
       elif self.validTurn[2] and self.direction == 2:  # Move up
           self.playerY -= self.playerSpeed
       elif self.validTurn[3] and self.direction == 3:  # Move down
           self.playerY += self.playerSpeed


       # Updates cooridnates of player's centre
       self.centreX = self.playerX + 23
       self.centreY = self.playerY + 24


       return self.playerX, self.playerY


   def playerInteraction(self):
       # Check if player is in grid
       if 0 < self.playerX < 870:
           # Check if pacman is on a dot
           if level[self.centreY // num1][self.centreX // num2] == 1:
               level[self.centreY // num1][self.centreX // num2] = 0
               self.score = self.score + 10


           # Check if pacman is on a power pellet
           if level[self.centreY // num1][self.centreX // num2] == 2:
               level[self.centreY // num1][self.centreX // num2] = 0
               self.score = self.score + 50
               self.powerUp = True
               self.powerCount = 0
               self.ghostsEaten = [False, False, False, False]


       return self.score, self.powerUp, self.powerCount, self.ghostsEaten




player = Player()


# Getting all images from the ghost_images file and assigning them to variables and also scaling them down
red_img = pygame.transform.scale(pygame.image.load(f'ghost_images/red.png'), (35, 35))
pink_img = pygame.transform.scale(pygame.image.load(f'ghost_images/pink.png'), (35, 35))
blue_img = pygame.transform.scale(pygame.image.load(f'ghost_images/blue.png'), (35, 35))
orange_img = pygame.transform.scale(pygame.image.load(f'ghost_images/orange.png'), (35, 35))
deadGhost = pygame.transform.scale(pygame.image.load(f'ghost_images/dead.png'), (35, 35))
powerup = pygame.transform.scale(pygame.image.load(f'ghost_images/powerup.png'), (35, 35))
# Starting coordinates and direction of all the ghosts
orangeX = 438
orangeY = 335
orangeDirection = 0
pinkX = 440
pinkY = 438
pinkDirection = 2
blueX = 400
blueY = 438
blueDirection = 2
redX = 480
redY = 438
redDirection = 2
# Creating the array for targets for each ghost
targets = [(player.playerX, player.playerY), (player.playerX, player.playerY), (player.playerX, player.playerY),
          (player.playerX, player.playerY)]
# Boolean variables for if ghost is dead
redDead = False
pinkDead = False
blueDead = False
orangeDead = False
# Boolean variables for if ghost is in the ghost box
redBox = False
pinkBox = False
blueBox = False
orangeBox = False
# Sets base ghost speed (same as the player speed)
ghostSpeed = [3, 3, 3, 3]




class Ghosts:
   def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
       # Ghost coordinates
       self.ghostX = x_coord
       self.ghostY = y_coord
       # Centre coordinates of ghosts
       self.ghostCentreX = int(self.ghostX + 22)
       self.ghostCentreY = int(self.ghostY + 22)
       # Stores array of player's coordinates for ghost to chase
       self.target = target
       # Determines speed of ghosts
       self.speed = speed
       # Stores png of ghosts and their states
       self.img = img
       # Direction ghost is facing
       self.direction = direct
       self.Dead = dead
       self.inbox = box
       # Way of identifying the ghosts easier as numerical values
       self.id = id


       # Array of valid turns similar to player
       self.turns, self.inbox = self.checkCollisions()
       # Hit box of ghosts
       self.rect = self.draw()
       self.respawnTimer = 0


   def draw(self):
       if gameRunning:
           # Draw normal ghosts if power pellet is not and dead or not eaten and power pellet not eaten and not dead
           if (not player.powerUp and not self.Dead) or (
                   player.ghostsEaten[self.id] and player.powerUp and not self.Dead):
               screen.blit(self.img, (self.ghostX, self.ghostY))
           # Draw spooked ghosts (bluish ones) when power pellet is eaten and not dead and not eaten
           elif player.powerUp and not self.Dead and not player.ghostsEaten[self.id]:
               screen.blit(powerup, (self.ghostX, self.ghostY))
           # Only other state of ghosts are when they are eaten and turn into eyes going back to the centre
           elif self.Dead and player.ghostsEaten[self.id]:
               screen.blit(deadGhost, (self.ghostX, self.ghostY))
           # Creates hit box
           ghost_rect = pygame.rect.Rect((self.ghostCentreX - 18, self.ghostCentreY - 18), (36, 36))
           return ghost_rect


   def checkCollisions(self):


       # Sets all directions to false every time it is called
       self.turns = [False, False, False, False]
       # Is ghost in screen boundaries
       if 0 < self.ghostCentreX // 30 < 29:
           # Allows ghosts to leave ghost box
           if level[(self.ghostCentreY - num3) // num1][self.ghostCentreX // num2] == 9:
               self.turns[2] = True
           # Check if piece ghost is on is a wall or ghost wall
           if level[self.ghostCentreY // num1][(self.ghostCentreX - num3) // num2] < 3 \
                   or (level[self.ghostCentreY // num1][(self.ghostCentreX - num3) // num2] == 9 and (
                   self.inbox or self.Dead)):
               self.turns[1] = True  # Left is valid
           if level[self.ghostCentreY // num1][(self.ghostCentreX + num3) // num2] < 3 \
                   or (level[self.ghostCentreY // num1][(self.ghostCentreX + num3) // num2] == 9 and (
                   self.inbox or self.Dead)):
               self.turns[0] = True  # Right is valid
           if level[(self.ghostCentreY + num3) // num1][self.ghostCentreX // num2] < 3 \
                   or (level[(self.ghostCentreY + num3) // num1][self.ghostCentreX // num2] == 9 and (
                   self.inbox or self.Dead)):
               self.turns[3] = True  # Up is valid
           if level[(self.ghostCentreY - num3) // num1][self.ghostCentreX // num2] < 3 \
                   or (level[(self.ghostCentreY - num3) // num1][self.ghostCentreX // num2] == 9 and (
                   self.inbox or self.Dead)):
               self.turns[2] = True  # Down is valid


           if self.direction == 2 or self.direction == 3:
               # If ghost is roughly in the middle of a piece
               if 12 <= self.ghostCentreX % num2 <= 18:
                   if level[(self.ghostCentreY + num3) // num1][self.ghostCentreX // num2] < 3 \
                           or (level[(self.ghostCentreY + num3) // num1][self.ghostCentreX // num2] == 9 and (
                           self.inbox or self.Dead)):
                       self.turns[3] = True  # Up is valid
                   if level[(self.ghostCentreY - num3) // num1][self.ghostCentreX // num2] < 3 \
                           or (level[(self.ghostCentreY - num3) // num1][self.ghostCentreX // num2] == 9 and (
                           self.inbox or self.Dead)):
                       self.turns[2] = True  # Down is valid
               if 12 <= self.ghostCentreY % num1 <= 18:
                   if level[self.ghostCentreY // num1][(self.ghostCentreX - num2) // num2] < 3 \
                           or (level[self.ghostCentreY // num1][(self.ghostCentreX - num2) // num2] == 9 and (
                           self.inbox or self.Dead)):
                       self.turns[1] = True  # Left is valid
                   if level[self.ghostCentreY // num1][(self.ghostCentreX + num2) // num2] < 3 \
                           or (level[self.ghostCentreY // num1][(self.ghostCentreX + num2) // num2] == 9 and (
                           self.inbox or self.Dead)):
                       self.turns[0] = True  # Right is valid


           if self.direction == 0 or self.direction == 1:
               # If ghost is roughly in the middle of a piece
               if 12 <= self.ghostCentreX % num2 <= 18:
                   if level[(self.ghostCentreY + num3) // num1][self.ghostCentreX // num2] < 3 \
                           or (level[(self.ghostCentreY + num3) // num1][self.ghostCentreX // num2] == 9 and (
                           self.inbox or self.Dead)):
                       self.turns[3] = True  # Up is valid
                   if level[(self.ghostCentreY - num3) // num1][self.ghostCentreX // num2] < 3 \
                           or (level[(self.ghostCentreY - num3) // num1][self.ghostCentreX // num2] == 9 and (
                           self.inbox or self.Dead)):
                       self.turns[2] = True  # Down is valid
               if 12 <= self.ghostCentreY % num1 <= 18:
                   if level[self.ghostCentreY // num1][(self.ghostCentreX - num3) // num2] < 3 \
                           or (level[self.ghostCentreY // num1][(self.ghostCentreX - num3) // num2] == 9 and (
                           self.inbox or self.Dead)):
                       self.turns[1] = True  # Left is valid
                   if level[self.ghostCentreY // num1][(self.ghostCentreX + num3) // num2] < 3 \
                           or (level[self.ghostCentreY // num1][(self.ghostCentreX + num3) // num2] == 9 and (
                           self.inbox or self.Dead)):
                       self.turns[0] = True  # Right is valid
       else:
           self.turns[0] = True
           self.turns[1] = True
       if 350 < self.ghostX < 550 and 370 < self.ghostY < 480:
           self.inbox = True
       else:
           self.inbox = False
       return self.turns, self.inbox


   def moveOrange(self):
       # Movement checks if direction is right
       if self.direction == 0:
           # If target is to the right and it is a valid turn the continue to move right
           if self.target[0] > self.ghostX and self.turns[0]:
               self.ghostX += self.speed
           # Changes directions based on player position
           elif not self.turns[0]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               # If ghost cannot move then change its direction
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
           # If ghost can move right but is no longer targeting the player
           # Will change direction to where the player is
           elif self.turns[0]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               if self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               else:
                   self.ghostX += self.speed
       # Repeated logic for each other direction
       # If moving left
       elif self.direction == 1:
           if self.target[1] > self.ghostY and self.turns[3]:
               self.direction = 3
           elif self.target[0] < self.ghostX and self.turns[1]:
               self.ghostX -= self.speed
           elif not self.turns[1]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[1]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               if self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               else:
                   self.ghostX -= self.speed
       # If moving up
       elif self.direction == 2:
           if self.target[0] < self.ghostX and self.turns[1]:
               self.direction = 1
               self.ghostX -= self.speed
           elif self.target[1] < self.ghostY and self.turns[2]:
               self.direction = 2
               self.ghostY -= self.speed
           elif not self.turns[2]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[2]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               else:
                   self.ghostY -= self.speed
       # If moving down
       elif self.direction == 3:
           if self.target[1] > self.ghostY and self.turns[3]:
               self.ghostY += self.speed
           elif not self.turns[3]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[3]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               else:
                   self.ghostY += self.speed


       if self.ghostX > 895:
           self.ghostX = -45
       elif self.ghostX < -45:
           self.ghostX = 890


       return self.ghostX, self.ghostY, self.direction


   def moveBlue(self):
       # Blue ghost will move in a direction until there is a wall  collision
       # If moving right
       if self.direction == 0:
           # If player is to the left then move left
           if self.target[0] > self.ghostX and self.turns[0]:
               self.ghostX += self.speed
           # If there is a collision change direction to target player
           elif not self.turns[0]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               # Altered directions being set when stuck to make movement unique
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
           # If not continue to move left
           elif self.turns[0]:
               self.ghostX += self.speed
       # Repeated logic for other directions
       # If moving left
       elif self.direction == 1:
           if self.target[0] < self.ghostX and self.turns[1]:
               self.ghostX -= self.speed
           elif not self.turns[1]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[1]:
               self.ghostX -= self.speed
       # If moving up
       elif self.direction == 2:
           if self.target[1] < self.ghostY and self.turns[2]:
               self.direction = 2
               self.ghostY -= self.speed
           elif not self.turns[2]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
           elif self.turns[2]:
               self.ghostY -= self.speed
       # If moving down
       elif self.direction == 3:
           if self.target[1] > self.ghostY and self.turns[3]:
               self.ghostY += self.speed
           elif not self.turns[3]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
           elif self.turns[3]:
               self.ghostY += self.speed


       if self.ghostX > 890:
           self.ghostX = -45
       elif self.ghostX < -45:
           self.ghostX = 890


       return self.ghostX, self.ghostY, self.direction


   # r l u d


   def moveRed(self):
       # Red will move left/right to chase the player and only move up/down on wall collisions
       if self.direction == 0:
           # If target is to the right and it is a valid turn then continue to move right
           if self.target[0] > self.ghostX and self.turns[0]:
               self.ghostX += self.speed
           # Change direction based on player position
           elif not self.turns[0]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               # If ghost cannot move then change its direction
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
           # If ghost can move right but is no longer targeting the player
           # Will change direction to where the player is
           elif self.turns[0]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               if self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               else:
                   self.ghostX += self.speed
       # Repeated logic for each other direction
       # If moving left
       elif self.direction == 1:
           if self.target[1] > self.ghostY and self.turns[3]:
               self.direction = 3
           elif self.target[0] < self.ghostX and self.turns[1]:
               self.ghostX -= self.speed
           elif not self.turns[1]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[1]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               if self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               else:
                   self.ghostX -= self.speed
       # If moving up
       elif self.direction == 2:
           if self.target[0] < self.ghostX and self.turns[1]:
               self.direction = 1
               self.ghostX -= self.speed
           elif self.target[1] < self.ghostY and self.turns[2]:
               self.direction = 2
               self.ghostY -= self.speed
           elif not self.turns[2]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[2]:
               self.ghostY -= self.speed
       # If moving down
       elif self.direction == 3:
           if self.target[1] > self.ghostY and self.turns[3]:
               self.ghostY += self.speed
           elif not self.turns[3]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[3]:
               self.ghostY += self.speed


       if self.ghostX > 895:
           self.ghostX = -45
       elif self.ghostX < -45:
           self.ghostX = 890


       return self.ghostX, self.ghostY, self.direction


   def movePink(self):
       # Pink ghost will move up/down to chase the player and right/left on collisions
       if self.direction == 0:
           # If target is to the right and it is a valid turn the continue to move right
           if self.target[0] > self.ghostX and self.turns[0]:
               self.ghostX += self.speed
           # Changes directions based on player position
           elif not self.turns[0]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               # If ghost cannot move then change its direction
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
           # Continue to move right
           elif self.turns[0]:
               self.ghostX += self.speed
       # If moving left
       elif self.direction == 1:
           if self.target[1] > self.ghostY and self.turns[3]:
               self.direction = 3
           elif self.target[0] < self.ghostX and self.turns[1]:
               self.ghostX -= self.speed
           elif not self.turns[1]:
               if self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           # Continue to move left
           elif self.turns[1]:
               self.ghostX -= self.speed
       # If moving up
       elif self.direction == 2:
           if self.target[0] < self.ghostX and self.turns[1]:
               self.direction = 1
               self.ghostX -= self.speed
           elif self.target[1] < self.ghostY and self.turns[2]:
               self.direction = 2
               self.ghostY -= self.speed
           elif not self.turns[2]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.target[1] > self.ghostY and self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.turns[3]:
                   self.direction = 3
                   self.ghostY += self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[2]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               else:
                   self.ghostY -= self.speed
       # If moving down
       elif self.direction == 3:
           if self.target[1] > self.ghostY and self.turns[3]:
               self.ghostY += self.speed
           elif not self.turns[3]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.target[1] < self.ghostY and self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[2]:
                   self.direction = 2
                   self.ghostY -= self.speed
               elif self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               elif self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
           elif self.turns[3]:
               if self.target[0] > self.ghostX and self.turns[0]:
                   self.direction = 0
                   self.ghostX += self.speed
               elif self.target[0] < self.ghostX and self.turns[1]:
                   self.direction = 1
                   self.ghostX -= self.speed
               else:
                   self.ghostY += self.speed


       if self.ghostX > 895:
           self.ghostX = -45
       elif self.ghostX < -45:
           self.ghostX = 890


       return self.ghostX, self.ghostY, self.direction


   # Function to get new targets based on the game state
   def Targets(self):
       # Determines coordinates for when ghosts scatter
       if player.playerX < 450:
           scatterX = 900
       else:
           scatterX = 0
       if player.playerY < 450:
           scatterY = 900
       else:
           scatterY = 0
       # Target for ghosts to return to ghost box when eaten
       returnTarget = (380, 415)
       if player.powerUp:
           # If ghost is alive and not eaten then scatter
           if not self.Dead and not player.ghostsEaten[self.id]:
               self.target = (scatterX, scatterY)
           elif not self.Dead and player.ghostsEaten[self.id]:
               # If alive and eaten target door
               if 340 < self.ghostX < 560 and 340 < self.ghostY < 500:
                   self.target = (400, 100)
               # If alive and not eaten target player
               else:
                   self.target = (player.playerX, player.playerY)
           # If dead and eaten return to ghost box
           elif self.Dead and player.ghostsEaten[self.id]:
               self.target = returnTarget
       # Target getting for normal game conditions
       else:
           if not self.Dead:
               if 340 < self.ghostX < 560 and 340 < self.ghostY < 500:
                   self.target = (400, 100)
               else:
                   self.target = (player.playerX, player.playerY)
           elif self.Dead and player.ghostsEaten[self.id]:
               self.target = returnTarget


       return self.target




# Used to display title and pacman drawings on game screens
def startScreen(content, Xpos):
   text = content
   screen.fill('black')
   # Display Pacman onto screen
   screen.blit(text, (Xpos, 90))
   # Display images of pacmans for screens
   screen.blit(pygame.transform.rotate(screenModel, 25), (25, 700))
   screen.blit(pygame.transform.rotate(screenModel, 155), (625, 700))




# Used to hide or remove buttons from the current screen
def hideButtons(*buttons):
   # Checks if the parameter passed in is a list or not
   # If it is it will iterate through the list to hide the buttons
   for item in buttons:
       if isinstance(item, list):
           for button in item:
               button.hide()
       # If it isn't it will hide the singular button
       else:
           item.hide()




# Used to display buttons for the current screen
def showButtons(*buttons):
   for item in buttons:
       # Checks if the parameter passed in is a list or not
       # If it is it will iterate through the list to show the buttons
       if isinstance(item, list):
           for button in item:
               button.show()
       # If it isn't it will show the singular button
       else:
           item.show()


# Used to display text onto the screen
def writeText(content, Xpos, Ypos, increment, font):
   # Will iterate through the text passed in
   for line in content:
       # Creates a variable for the text to be displayed using the correct font
       Text = font.render(line, True, 'Yellow')
       # Displays the text onto the screen
       screen.blit(Text, (Xpos, Ypos))
       # Increments the Y position to allo for spacing between text
       Ypos += increment




# creating a manager used for the gui
manager = pygame_gui.UIManager((900, 950), theme_path="theme.json")


# variables for all menu buttons including their position
playButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 300), (200, 100)), text='Play',
                                         manager=manager)
controlButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 425), (200, 100)), text='Controls',
                                            manager=manager)
gameButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 550), (200, 100)), text='Game Info',
                                         manager=manager)
closeButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 5), (50, 50)), text='X',
                                          manager=manager)
# List storing all the buttons in the main menu
menuButtons = [playButton, controlButton, gameButton]


# variables for all speed selection buttons including their position
slowButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 300), (200, 100)), text='Slow',
                                         manager=manager)
mediumButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 425), (200, 100)), text='Medium',
                                           manager=manager)
fastButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 550), (200, 100)), text='Fast',
                                         manager=manager)
# List storing all the buttons for the speed selection
speedButtons = [slowButton, mediumButton, fastButton]


# variables for buttons to do with the pause screen
resumeButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 300), (200, 100)), text='Resume',
                                           manager=manager)
returnButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 425), (200, 100)), text='Return to menu',
                                           manager=manager)


# List storing all the buttons for the pause screen
pauseButtons = [resumeButton, returnButton]


playAgain = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 550), (200, 100)), text='Play again',
                                        manager=manager)


clock = pygame.time.Clock()
run = True
while run:
   timeDelta = clock.tick(fps) / 1000.0  # Ensures consistent timing for 60 FPS
   # Initial screen
   startScreen(titleText, 310)


   # Check to switch between different screens
   if gameScreen == 'menu':
       screen.fill('black')
       startScreen(titleText, 310)
       # Displays menu buttons and hides the other buttons
       showButtons(menuButtons, closeButton)
       hideButtons(speedButtons, pauseButtons, playAgain)






   elif gameScreen == 'controls':
       startScreen(titleText, 310)
       hideButtons(menuButtons)


       # Text to be displayed for control screen
       controlText = [
           "W - Move Up",
           "A - Move Left",
           "S - Move Down",
           "D - Move Right",
           "Space - Pause Game"
       ]
       # Displays text onto the screen
       writeText(controlText, 260, 200, 100, titleFont)




   elif gameScreen == 'info':
       startScreen(titleText, 310)
       # Hides the buttons
       hideButtons(menuButtons)
       # Text to be displayed for info screen
       gameText = [
           "Game objectives: ",
           "Eat all the dots",
           "Eating power pellets lets you ",
           "eat ghosts",
           "Once all dots are eaten level ",
           "will increase",
           "Complete level 20 to finish the ",
           "game",
       ]
       scoreText = [
           "Scoring:",
           "Dots - 10 Points",
           "Power Pellet - 50 points",
           "Ghosts - 200, 400, 800, 1600 points",
       ]
       writeText(gameText, 40, 180, 65, infoFont)
       writeText(scoreText, 440, 180, 65, infoFont)




   elif gameScreen == 'speedSelection':
       startScreen(speedText, 300)
       # Show necessary buttons
       hideButtons(menuButtons, returnButton, playAgain)
       showButtons(speedButtons)
       # Resets variables to the start of the game excluding
       # Resets map
       for i in range(len(level)):
           for j in range(len(level[i])):
               level[i][j] = baseLevel[i][j]
       levels = 1
       player.score = 0
       game.colour = 'blue'
       lives = 3
       gameCount = 0
       player.powerUp = False
       player.powerCount = 0
       player.playerX = 450
       player.playerY = 663
       player.centreX = player.playerX + 23
       player.centreY = player.playerY + 24
       player.direction = 0
       player.directionInput = 0
       orangeX = 438
       orangeY = 335
       orangeDirection = 0
       pinkX = 440
       pinkY = 438
       pinkDirection = 2
       blueX = 400
       blueY = 438
       blueDirection = 2
       redX = 480
       redY = 438
       redDirection = 2
       player.ghostsEaten = [False, False, False, False]
       redDead = False
       blueDead = False
       pinkDead = False
       orangeDead = False
       moving = False






   elif gameScreen == 'gameOver':
       startScreen(gameOverText, 300)
       # Draws score onto screen
       scoreText = titleFont.render(f'Score: {scores}', True, 'yellow')
       screen.blit(scoreText, (320, 200))
       # Draws level onto screen
       levelText = titleFont.render(f'Level: {levels}', True, 'yellow')
       screen.blit(levelText, (320, 300))
       showButtons(returnButton, playAgain)






   elif gameScreen == 'gameWon':
       startScreen(gameWonText, 300)
       # Draws score onto screen
       scoreText = titleFont.render(f'Score: {scores}', True, 'yellow')
       screen.blit(scoreText, (320, 200))
       # Draws level onto screen
       levelText = titleFont.render(f'Level: {levels}', True, 'yellow')
       screen.blit(levelText, (320, 300))
       showButtons(returnButton, playAgain)
       # Reset levels variable
       levels = 1




   elif gameScreen == 'pause':
       # Stop all movements and pause game
       moving = False
       gameRunning = False
       pauseText = titleFont.render("Game Paused", True, 'Yellow')
       startScreen(pauseText, 300)
       showButtons(pauseButtons)






   elif gameScreen == 'playing':
       gameRunning = True


   if player.counter < 20:
       player.counter += 1
   else:
       player.counter = 0
   # Increments power up timer
   if player.powerUp and player.powerCount < 600:
       player.powerCount += 1
   # Once power up duration is over
   elif player.powerUp and player.powerCount >= 600:
       # Resets count for power up
       player.powerCount = 0
       player.powerUp = False
       player.ghostsEaten = [False, False, False, False]


   # Once play has been seleceted
   if gameRunning:
       screen.fill('black')
       # Hdies buttons
       hideButtons(menuButtons, speedButtons, closeButton, resumeButton, returnButton)


       # Instances of the ghost class for each ghost
       red = Ghosts(redX, redY, targets[0], ghostSpeed[0], red_img, redDirection, redDead, redBox, 0)
       blue = Ghosts(blueX, blueY, targets[1], ghostSpeed[1], blue_img, blueDirection, blueDead, blueBox, 1)
       pink = Ghosts(pinkX, pinkY, targets[2], ghostSpeed[2], pink_img, pinkDirection, pinkDead, pinkBox, 2)
       orange = Ghosts(orangeX, orangeY, targets[3], ghostSpeed[3], orange_img, orangeDirection, orangeDead,
                       orangeBox, 3)


       # When starting or restarting game there will be a delay before it starts
       if gameCount < 120:
           moving = False
           gameCount += 1
       else:
           moving = True


           # Changing ghost speeds in various game states
           if player.powerUp:
               # During a power up set the speed of all ghosts to 1 lower than the player
               ghostSpeed = [2, 2, 2, 2]
           elif levels % 5 == 0:
               ghostSpeed = [2 + 0.1 * min(levels // 5, 4)] * 4
           else:
               # In normal conditions the ghost speed matches the player speed
               ghostSpeed = [3, 3, 3, 3]
           # If a ghost dies make their speed faster, so they get back to box and reset faster
           if redDead:
               ghostSpeed[0] = 4
           if blueDead:
               ghostSpeed[1] = 4
           if pinkDead:
               ghostSpeed[2] = 4
           if orangeDead:
               ghostSpeed[3] = 4


       targets[0] = red.Targets()
       targets[1] = blue.Targets()
       targets[2] = pink.Targets()
       targets[3] = orange.Targets()


       if moving:
           if not redDead and not red.inbox:
               redX, redY, redDirection = red.moveRed()
           else:
               redX, redY, redDirection = red.moveOrange()
           if not blueDead and not blue.inbox:
               blueX, blueY, blueDirection = blue.moveBlue()
           else:
               blueX, blueY, blueDirection = blue.moveOrange()
           if not pinkDead and not pink.inbox:
               pinkX, pinkY, pinkDirection = pink.movePink()
           else:
               pinkX, pinkY, pinkDirection = pink.moveOrange()


           orangeX, orangeY, orangeDirection = orange.moveOrange()


           player.playerX, player.playerY = player.playerMovement()


       game.drawMap()
       player.drawPlayer()
       scores, player.powerUp, player.powerCount, player.ghostsEaten = player.playerInteraction()
       game.updateUI()
       pygame.display.update()


       # Hitbox of player
       playerCircle = pygame.draw.circle(screen, 'black', (player.centreX - 6, player.centreY - 6), 19, 2)


       # In normal conditions
       if not player.powerUp:
           if (playerCircle.colliderect(red.rect) and not red.Dead) or \
                   (playerCircle.colliderect(blue.rect) and not blue.Dead) or \
                   (playerCircle.colliderect(pink.rect) and not pink.Dead) or \
                   (playerCircle.colliderect(orange.rect) and not orange.Dead):
               if lives > 1:
                   # Player loses a life
                   lives -= 1
                   gameCount = 0
                   # Resets variables to the start of the game excluding the dos
                   player.powerUp = False
                   player.powerCount = 0
                   player.playerX = 450
                   player.playerY = 663
                   player.centreX = player.playerX + 23
                   player.centreY = player.playerY + 24
                   player.direction = 0
                   player.directionInput = 0
                   orangeX = 438
                   orangeY = 335
                   orangeDirection = 0
                   pinkX = 440
                   pinkY = 438
                   pinkDirection = 2
                   blueX = 400
                   blueY = 438
                   blueDirection = 2
                   redX = 480
                   redY = 438
                   redDirection = 2
                   player.ghostsEaten = [False, False, False, False]
                   redDead = False
                   blueDead = False
                   pinkDead = False
                   orangeDead = False
                   moving = False
               else:
                   gameScreen = 'gameOver'
                   moving = False
                   gameCount = 0
                   gameRunning = False




       else:
           # If the player collides with a ghost that respawned during a power up
           if (playerCircle.colliderect(red.rect) and not red.Dead and player.ghostsEaten[0]) or \
                   (playerCircle.colliderect(blue.rect) and not blue.Dead and player.ghostsEaten[1]) or \
                   (playerCircle.colliderect(pink.rect) and not pink.Dead and player.ghostsEaten[2]) or \
                   (playerCircle.colliderect(orange.rect) and not orange.Dead and player.ghostsEaten[3]):
               if lives > 1:
                   # Player loses a life
                   lives -= 1
                   gameCount = 0
                   # Resets variables to the start of the game excluding the dos
                   player.powerUp = False
                   player.powerCount = 0
                   player.playerX = 450
                   player.playerY = 663
                   player.centreX = player.playerX + 23
                   player.centreY = player.playerY + 24
                   player.direction = 0
                   player.directionInput = 0
                   orangeX = 438
                   orangeY = 335
                   orangeDirection = 0
                   pinkX = 440
                   pinkY = 438
                   pinkDirection = 2
                   blueX = 400
                   blueY = 438
                   blueDirection = 2
                   redX = 480
                   redY = 438
                   redDirection = 2
                   player.ghostsEaten = [False, False, False, False]
                   redDead = False
                   blueDead = False
                   pinkDead = False
                   orangeDead = False
                   moving = False
               else:
                   gameScreen = 'gameOver'
                   moving = False
                   gameCount = 0
                   gameRunning = False


           # During a power up if the player collides with a ghost that wasn’t eaten and not dead it is eaten and now dead
           if playerCircle.colliderect(red.rect) and not red.Dead and not player.ghostsEaten[0]:
               redDead = True
               player.ghostsEaten[0] = True
               player.score += (2 ** player.ghostsEaten.count(True)) * 100


           # Logic is repeated for each ghost
           if playerCircle.colliderect(blue.rect) and not blue.Dead and not player.ghostsEaten[1]:
               blueDead = True
               player.ghostsEaten[1] = True
               player.score += (2 ** player.ghostsEaten.count(True)) * 100


           if playerCircle.colliderect(pink.rect) and not pink.Dead and not player.ghostsEaten[2]:
               pinkDead = True
               player.ghostsEaten[2] = True
               player.score += (2 ** player.ghostsEaten.count(True)) * 100


           if playerCircle.colliderect(orange.rect) and not orange.Dead and not player.ghostsEaten[3]:
               orangeDead = True
               player.ghostsEaten[3] = True
               player.score += (2 ** player.ghostsEaten.count(True)) * 100


       if red.Dead and red.inbox:
           redDead = False
       if blue.Dead and blue.inbox:
           blueDead = False
       if pink.Dead and pink.inbox:
           pinkDead = False
       if orange.Dead and orange.inbox:
           orangeDead = False




   def checkLevel():
       for i in range(len(level)):
           for j in range(len(level[i])):
               if level[i][j] == 1 or level[i][j] == 2:  # Check for pellet values
                   return False  # If any pellet is found, level is not complete
       return True  # If no pellets are found, level is complete




   # Call the function and update the levelComplete variable
   levelComplete = checkLevel()


   if levelComplete and levels < 20:
       moving = False
       # Increments level
       levels += 1
       # Changes colour depending on level
       game.colour = game.levelColour()
       # Resets map
       for i in range(len(level)):
           for j in range(len(level[i])):
               level[i][j] = baseLevel[i][j]
       gameCount = 0
       # Resets variables to the start of the game excluding the dos
       player.powerUp = False
       player.powerCount = 0
       player.playerX = 450
       player.playerY = 663
       player.centreX = player.playerX + 23
       player.centreY = player.playerY + 24
       player.direction = 0
       player.directionInput = 0
       orangeX = 438
       orangeY = 335
       orangeDirection = 0
       pinkX = 440
       pinkY = 438
       pinkDirection = 2
       blueX = 400
       blueY = 438
       blueDirection = 2
       redX = 480
       redY = 438
       redDirection = 2
       player.ghostsEaten = [False, False, False, False]
       redDead = False
       blueDead = False
       pinkDead = False
       orangeDead = False




   elif levelComplete and levels == 20:
       gameScreen = 'gameWon'
       moving = False
       gameCount = 0
       gameRunning = False


   for event in pygame.event.get():
       # Condition to exit infinite loop
       if event.type == pygame.QUIT:
           run = False
       # Registers each key (WASD) and assigns it a direction as a numerical value
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_d:
               player.directionInput = 0
           if event.key == pygame.K_a:
               player.directionInput = 1
           if event.key == pygame.K_w:
               player.directionInput = 2
           if event.key == pygame.K_s:
               player.directionInput = 3
           if event.key == pygame.K_SPACE and gameScreen == 'playing':
               gameScreen = 'pause'


       manager.process_events(event)


       if event.type == pygame.KEYUP:
           if event.key == pygame.K_d and player.directionInput == 0:
               player.directionInput = player.directionInput
           if event.key == pygame.K_a and player.directionInput == 1:
               player.directionInput = player.directionInput
           if event.key == pygame.K_w and player.directionInput == 2:
               player.directionInput = player.directionInput
           if event.key == pygame.K_s and player.directionInput == 3:
               player.directionInput = player.directionInput


       # Event handling for buttons
       if event.type == pygame_gui.UI_BUTTON_PRESSED:
           # When an option is clicked it will display the corresponding screen
           if event.ui_element == playButton:
               gameScreen = 'speedSelection'
           if event.ui_element == controlButton:
               gameScreen = 'controls'
           if event.ui_element == gameButton:
               gameScreen = 'info'
           if event.ui_element == closeButton:
               gameScreen = 'menu'


           # When an option is clicked the speed is set and the game will start
           if event.ui_element == slowButton:
               player.playerSpeed = 3
               gameScreen = 'playing'
           if event.ui_element == mediumButton:
               player.playerSpeed = 4
               gameScreen = 'playing'
           if event.ui_element == fastButton:
               player.playerSpeed = 5
               gameScreen = 'playing'


           # Option to return to menu
           if event.ui_element == returnButton:
               gameScreen = 'menu'


           # Option to play again / resume game
           if event.ui_element == resumeButton:
               gameScreen = 'playing'
           if event.ui_element == playAgain:
               gameScreen = 'speedSelection'


   player.validTurn = player.checkPos()
   if player.directionInput == 0 and player.validTurn[0]:
       player.direction = 0
   if player.directionInput == 1 and player.validTurn[1]:
       player.direction = 1
   if player.directionInput == 2 and player.validTurn[2]:
       player.direction = 2
   if player.directionInput == 3 and player.validTurn[3]:
       player.direction = 3


       # Code for warp tunnel
   if player.playerX > 900:
       player.playerX = -45
   elif player.playerX < -50:
       player.playerX = 890


   manager.update(timeDelta)
   screen.blit(screen, (0, 0))
   manager.draw_ui(screen)


   pygame.display.flip()
pygame.quit



