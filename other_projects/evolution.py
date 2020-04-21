import random, pygame, sys, malcUtil, copy
maxMoves=250
dotNum=3000
vectorMaxLength=15

pygame.init()
dimensions = (500, 650)
canvas = pygame.display.set_mode(dimensions)
evolutions=999999
mutationChance=0.06
distributionVal=2.35
fps=20
clock=pygame.time.Clock()
goalDiameter=25
obsNum=3
onlyBest=False
paused=False


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, index):
        if index==0:
            return self.x
        elif index==1:
            return self.y
        else:
            raise IndexError('unsupported index for two dimensional vector')
    def __repr__(self):
        return f"Vector2D ({self.x}, {self.y})"

start=Vector2D(round(dimensions[0]/2), dimensions[1]-15)
goalPos=Vector2D(round(dimensions[0]/2), 45)
        
class Brain:
    def __init__(self, moveList=None):
        if moveList:
            self.moveList=moveList
        else:
            self.moveList=[]
            for move in range(maxMoves):
                self.moveList.append(self.getRandVector())

    def __getitem__(self, index):
        return self.moveList[index]
            
    @staticmethod
    def getRandVector():
        return Vector2D(random.uniform(-1*vectorMaxLength, vectorMaxLength), random.uniform(-1*vectorMaxLength, vectorMaxLength))
    def mutate(self):
        for i in range(len(self.moveList)):
            if random.random() <= mutationChance:
                @malcUtil.validateValue(f"answer<={vectorMaxLength}", f"answer>={vectorMaxLength*-1}")
                def getCoord(orig):
                    return random.normalvariate(orig, distributionVal)
                nx=getCoord(self.moveList[i][0])
                ny=getCoord(self.moveList[i][1])
                self.moveList[i]=Vector2D(nx, ny)

class Goal:
    def __init__(self):
        self.x, self.y = goalPos
    def draw(self):
        self.rect=pygame.draw.circle(canvas, (0, 230, 100), (self.x, self.y), goalDiameter)
        pygame.draw.circle(canvas, (0,100, 230), (self.x, self.y), round(goalDiameter-goalDiameter/5))
    def collideCheck(self, point):
        x, y=point
        h, k=self.rect.center
        rx=self.rect.width/2
        ry=self.rect.height/2
        return (((x-h)/rx)**2) + (((y-k)/ry)**2)<=1

class Dot:
    def __init__(self, brain=None):
        if brain:
            self.brain=brain
        else:
            self.brain=Brain()
        self.x, self.y=start
        self.success=False
        self.moveCount=0
        self.dead=False
        self.scoreOverride=None
        self.best=False
        self.color=(0,0,0)
        self.radius=2
    def draw(self):
        self.checkCollide()
        if self.dead:
            self.color=(255,0,0)
            self.scoreOverride=0
        elif self.best:
            self.color=(0,255,0)
            self.radius=4
        else:
            self.color=(0,0,0)
        def drawConditionals():
            if ((goal.x-self.x)**2+(goal.y-self.y)**2)**0.5<goalDiameter/2:
                self.success=True
            elif self.x<=0 or self.x>=dimensions[0] or self.y>=dimensions[1] or self.y<=0:
                self.dead=True
                self.score=0
                if self.x<0:
                    self.x=0
                elif self.x>dimensions[0]:
                    self.x=dimensions[0]
                if self.y>dimensions[1]:
                    selfy=dimensions[1]
                elif self.y<0:
                    self.y=0
                pygame.draw.circle(canvas, self.color, (int(self.x), int(self.y)), self.radius)
            else:
                pygame.draw.circle(canvas, self.color, (int(self.x), int(self.y)), self.radius)
                self.moveCount+=1
        if not onlyBest and not self.best:
            drawConditionals()
        elif self.best:
            drawConditionals()
    def move(self, index):
        if not self.success and not self.dead:
            self.x+=self.brain[index][0]
            self.y+=self.brain[index][1]
            self.mv=index
    def distToGoal(self):
        return ((goal.x-self.x)**2+(goal.y-self.y)**2)**0.5
    def getScore(self):
        if self.scoreOverride != None:
            return self.scoreOverride
        else:
            try:
                return (self.distToGoal() ** -1) * (maxMoves/self.mv)
            except ZeroDivisionError:
                return 0
    def checkCollide(self):
        for ob in obsList:
            if ob.collideCheck((self.x, self.y)):
                self.dead=True
        if goal.collideCheck((self.x, self.y)):
            self.success=True

goal=Goal()

class Obstacle:
    def __init__(self, shape, rect):
        self.shape=shape
        self.rect=rect
        self.color=(0,0,0)
    def draw(self):
        if self.shape=="rectangle":
            pygame.draw.rect(canvas, self.color, self.rect)
        elif self.shape=="ellipse":
            pygame.draw.ellipse(canvas, self.color, self.rect)
        else:
            raise ValueError("shape must be 'rectangle' or 'ellipse'")
    def collideCheck(self, point):
        if self.shape=="rectangle":
            return self.rect.collidepoint(int(point[0]), int(point[1]))
        elif self.shape=="ellipse":
            x, y=point
            h, k=self.rect.center
            rx=self.rect.width/2
            ry=self.rect.height/2
            return (((x-h)/rx)**2) + (((y-k)/ry)**2)<=1

def createDots(brainList=None):
    if brainList:
        dotList=[Dot(brainList[i]) for i in range(dotNum-1)]
    else:
        dotList=[Dot() for i in range(dotNum)]
    return dotList

def createObs():
    obsList=[]
    shapeList=["rectangle", "ellipse"]
    for i in range(obsNum):
        shape=random.choice(shapeList)
        rect=pygame.Rect(random.randint(0, dimensions[0]-100), random.randint(0, dimensions[1]-100), random.randint(100, dimensions[0]-300), random.randint(50, dimensions[1]-400))
        obsList.append(Obstacle(shape, rect))
    return obsList
            
obsList=createObs()
dotList = createDots()


def draw():
    canvas.fill((255,255,255))
    goal.draw()
    for obstacle in obsList:
        obstacle.draw()
    for dot in dotList:
        dot.move(mv)
        dot.draw()
    pygame.display.update()

def handleEvents():
    global onlyBest
    global paused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_RETURN:
                if onlyBest:
                    onlyBest=False
                else:
                    onlyBest=True
            elif event.key==pygame.K_SPACE:
                if paused:
                    paused=False
                else:
                    paused=True
                    while paused:
                        handleEvents()
def pickNew():
    global dotList
    weightList=[dot.getScore() for dot in dotList]
    brains = [dot.brain for dot in dotList]
    bestScore=0
    for dot in dotList:
        if dot.getScore()>bestScore:
            bestScore=dot.getScore()
            bestDot=dot
    brainList = [copy.deepcopy(random.choices(brains, weightList)[0]) for i in range(dotNum-1)]
    dotList=createDots(brainList)
    for dot in dotList:
        dot.brain.mutate()
    dotList.append(Dot(brain=bestDot.brain))
    dotList[-1].best=True

    
for ev in range(evolutions):
    mv=0
    while mv<maxMoves:
        draw()
        mv+=1
        handleEvents()
        clock.tick(fps)
    pickNew()
#pygame.quit()
#sys.exit()
