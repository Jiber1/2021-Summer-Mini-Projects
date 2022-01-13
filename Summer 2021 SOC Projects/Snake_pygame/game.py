import pygame, sys, random

width = 400
height = 400
size = (width, height)

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)



class Snake():
    def __init__(self):
        self.length = 1
        self.position = [((width/4), (height/4))]
        self.direction = up
        self.color = (255, 255, 255)
        self.score = 0

    def head_position(self):
        return self.position[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        head = self.head_position()
        x, y = self.direction
        newpos = (((head[0]+(x*20))%width), (head[1]+(y*20))%height)
        if len(self.position) > 2 and newpos in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0,newpos)
            if len(self.position) > self.length:
                self.position.pop()

    def reset(self):
        self.length = 1
        self.position = [((width/2), (height/2))]
        self.direction = up
        self.score = 0

    def draw(self,surface):
        for position in self.position:
            coords = pygame.Rect((position[0], position[1]), (20,20))
            pygame.draw.rect(surface, self.color, coords)
            pygame.draw.rect(surface, (255, 255, 255), coords, 1)

    def inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.turn(up)
                elif event.key == pygame.K_s:
                    self.turn(down)
                elif event.key == pygame.K_a:
                    self.turn(left)
                elif event.key == pygame.K_d:
                    self.turn(right)

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (34, 139, 34)
        self.random_position()

    def random_position(self):
        self.position = (random.randint(0, 19)*20, random.randint(0, 19)*20)

    def draw(self, surface):
        coords = pygame.Rect((self.position[0], self.position[1]), (20, 20))
        pygame.draw.rect(surface, self.color, coords)
        pygame.draw.rect(surface, (34, 139, 34), coords, 1)

def drawGrid(surface):
    for y in range(0, 20):
        for x in range(0, 20):
            coords = pygame.Rect((x*20, y*20), (20, 20))
            pygame.draw.rect(surface,(0,0,0), coords)
            

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    font = pygame.font.SysFont("monospace",16)

    while 1:
        clock.tick(8)
        snake.inputs()
        drawGrid(surface)
        snake.move()
        if snake.head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.random_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = font.render("Score = {0}".format(snake.score), 1, (255,255,255))
        screen.blit(text, (4,8))
        pygame.display.update()

main()
