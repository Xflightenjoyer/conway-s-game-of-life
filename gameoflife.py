import pygame
import random
import copy
pygame.init()
screenwidth = 1500
screenheight = 750
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("conways game of life")
gamewidth=300
gameheight=150
gamelist=[]
for x in range(gamewidth):
    gamelist.append([])
    for y in range(gameheight):
        gamelist[x].append("0")
def liveneighborscount(x,y,list):
    live=0
    directions=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    for i in range(8):
        ik=directions[i]
        if list[x+(ik[1])][y+(ik[0])]=="1" or list[x+(ik[1])][y+(ik[0])]=="4":
            live+=1
    return live
def outofbounds(list,x,y):
    if len(list)<=x-1:
        return False
    if x<=0:
        return False
    if len(list[x])<=y-1:
        return False
    if y<=0:
        return False
#def cutedges(list):
    #list2=copy.deepcopy(list)
    #list2.pop(-1)
    #list2.pop(0)
    #for k in range(len(list2)):
        #list2[k].pop(-1)
        #list2[k].pop(0)
    #return list2

def updatelist(list):
    list2=copy.deepcopy(list)
    #these are the rules
    stayliverange=[2,3]
    bornrange=[3]

    for i in range(1,len(list)-1):
        for j in range(1,len(list[i])-1):
            if list[i][j]=="1" or list[i][j]=="3":
                if not(liveneighborscount(i,j,list) in stayliverange) and not outofbounds(list,i,j):
                    list2[i][j]=str(int(list[i][j])-1)    
            if list[i][j]=="0" or list[i][j]=="2":
                if liveneighborscount(i,j,list) in bornrange and not outofbounds(list,i,j):
                    list2[i][j]=str(int(list[i][j])+1)
    return list2



def randomize(list2,chance):
    list=copy.deepcopy(list2)
    for i in range(len(list)):
        for j in range(len(list[int(i)])):
            list[i][j]="0"
    for i in range(len(list)):
        for j in range(len(list[int(i)])):
            if random.randint(1,chance)==1:
                list[i][j]="1"
    return list



def makerects(gamelist):
    rects=[]
    unitx=screenwidth/len(gamelist)
    unity=screenheight/len(gamelist[0])
    for x in range(len(gamelist)):
        for y in range(len(gamelist[x])):
            rects.append([pygame.Rect(unitx*x,unity*y,unitx,unity),gamelist[x][y]])
    return rects

def copylist(list):
    list2=[]
    for i in range(len(list)):
        list2.append(list[i])
    return list2
def drawlevel(rectlist):
    for x in range(len(rectlist)):
        if rectlist[x][1]=="2":
            pygame.draw.rect(screen,(0,255,0),rectlist[x][0])
        elif rectlist[x][1]=="1":
            pygame.draw.rect(screen,(255,255,255),rectlist[x][0])
def clearedges(list):
    list2=copylist(list)
    for i in range(len(list[0])):
        list2[0][i]="0"
    for i in  range(len(list[-1])):
        list2[-1][i]="0"
    for i in range(len(list2)):
        list2[i][0]="0"
        list2[i][-1]="0"
    return list2
gamelist=clearedges(randomize(gamelist,6))
clock = pygame.time.Clock()
running = True
cycles=0
while running:
    cycles+=1
    screen.fill((0, 0, 0)) 
    drawlevel(makerects(gamelist))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            gamelist=clearedges(randomize(gamelist,6))
    gamelist=updatelist(gamelist) 
    pygame.display.flip() 
    clock.tick(60)  
pygame.quit()