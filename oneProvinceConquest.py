import pygame, random

def draw():
    for i in range(countryNum):
        for j in range(len(country[i])):
            pygame.draw.rect(screen, colors[i], (country[i][j][0], country[i][j][1], terSize, terSize))

def conquest():
    rand = random.randrange(0, countryNum)
    for rand in range(countryNum):
        possibleConq = []
        for i in range(len(country[rand])):
            if (country[rand][i][0]-terSize, country[rand][i][1]) not in country[rand] and country[rand][i][0] != 0:
                possibleConq.append((country[rand][i][0]-terSize, country[rand][i][1]))
            if (country[rand][i][0]+terSize, country[rand][i][1]) not in country[rand] and country[rand][i][0] != width:
                possibleConq.append((country[rand][i][0]+terSize, country[rand][i][1]))
            if (country[rand][i][0], country[rand][i][1]-terSize) not in country[rand] and country[rand][i][1] != 0:
                possibleConq.append((country[rand][i][0], country[rand][i][1]-terSize))
            if (country[rand][i][0], country[rand][i][1]+terSize) not in country[rand] and country[rand][i][1] != height:
                possibleConq.append((country[rand][i][0], country[rand][i][1]+terSize))
        conq = random.choice(possibleConq)
        for i in range(countryNum):
            if conq in country[i]:
                country[i].remove(conq)
        country[rand].append(conq)


white     = (255, 255, 255)
black     = (0, 0, 0)
red       = (255, 0, 0)
green     = (0, 255, 0)
blue      = (0, 0, 255)
colors    = (red, green, blue)

width = 820
height = 600
terSize = 10
fps = 60
countryNum = 3

country = [[] for i in range(countryNum)]
for i in range(countryNum):
    rX = random.randrange(0, 820, terSize)
    rY = random.randrange(0, 600, terSize)
    while [(rX, rY)] in country:
        rX = random.randrange(0, 820, terSize)
        rY = random.randrange(0, 600, terSize)
    country[i].append((rX, rY))

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('World Conquest')
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(fps)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.fill(black)
    conquest()
    draw()
    pygame.display.update()
pygame.quit()
