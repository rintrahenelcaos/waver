import pygame
import math

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Waver")

BACKGROUND_COLOR = (127,127,127)
CELL = 9
FPS = 60
GRID_WIDTH = WIDTH//CELL
GRID_HEIGHT = HEIGHT//CELL

WAVE_PERIOD = 50
WAVE_LENGHT= CELL*10
WAVE_SPEED = WAVE_LENGHT/WAVE_PERIOD
WAVE_NUMBER = 2*math.pi/WAVE_LENGHT
ALPHA = 0.01 # amortiguation

WHITE = (255,255,255)

total_cells = [((x*5, y*5), 0, False) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]
total_cells = [(x*CELL, y*CELL) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]
total_cells = [[(x*CELL, y*CELL), 0] for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]
total_cells = [[(x*CELL, y*CELL), []] for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]

active_cells = []





def draw_window(centers, time):
    WIN.fill(BACKGROUND_COLOR)
    wave = "Wave"
    
    
    for cell in total_cells:
        ztot = 0
        for center in centers:
            posgrid = grid_position(center[0])
            distance = math.dist(cell[0], posgrid) 
            
            if distance < WAVE_SPEED * (time-center[1]):
                try: 
                    waveorder = cell[1][centers.index(center)]
                    
                    z = waving_function_indep(waveorder)
                    ztot += z
                    if ztot > 127: ztot = 127
                    if ztot < -127: ztot = -127
                    cell[1][centers.index(center)] += 1
                except: 
                    cell[1].append(0)
                    z = waving_function_indep(0)
                    ztot += z
                    if ztot > 127: ztot = 127
                    if ztot < -127: ztot = -127
        color = (127+ztot, 127+ztot, 127+ztot)
        particle = pygame.Rect(cell[0][0], cell[0][1],CELL,CELL)
        pygame.draw.rect(WIN, color ,particle)
                
                    
                        

    pygame.display.update()
    
    return wave
    
 

def grid_position(position):
    x = (position[0]//CELL)*CELL
    y = (position[1]//CELL)*CELL
    return (x,y)

    


def waving_function_indep(time):
    
    z = 127*math.exp(-ALPHA*time)*(math.sin((2*math.pi/WAVE_LENGHT)*(WAVE_SPEED*time)))
    
    return z
    
   

def main():
    
    run = True
    centers = []
    time = 0
    while run:
        
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pos = pygame.mouse.get_pos()
                center = [pos, time]
                centers.append(center)
                
            
            
        time += 1
        
        draw_window(centers, time)
        
    
    pygame.quit()


if __name__=="__main__":
    main()