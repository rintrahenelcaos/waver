import pygame
import math

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND_COLOR = (127,127,127)
CELL = 5
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


active_cells = []



def surface_function():
    global total_cells
    
    old_total_cells = total_cells.copy()
    
    
    

def draw_window_orig(position, time):
    WIN.fill(BACKGROUND_COLOR)
    wave = "Wave"
    
    for pos in position:
        posgrid = grid_position(pos)
        wave_function(posgrid, WIN, time)

    pygame.display.update()
    
    return wave

def draw_window(centers, time):
    WIN.fill(BACKGROUND_COLOR)
    wave = "Wave"
    
    """for pos in position:
        posgrid = grid_position(pos)
        wave_function(posgrid, WIN, time)
        mov = longitudinal_wave(posgrid, time)
        if mov != None:
            wave_function(mov, WIN, time)"""
    
    for cell in total_cells:
        for center in centers:
            posgrid = grid_position(center[0])
            distance = math.dist(cell[0], posgrid) 
            if distance < WAVE_SPEED * (time-center[1]):
                
                waving_func(cell[0], (cell[1]), posgrid, WIN)
                cell[1] += 1
            
            

    pygame.display.update()
    
    return wave
    
def wave_function(position, window, time):
    particle = pygame.Rect(position[0], position[1],CELL,CELL)
    print(pygame.draw.rect(window, oscilation_func(time),particle))
    print(oscilation_func(time))
    
    

def oscilation_func(time):
    color_change = round(math.sin(((2*math.pi)/WAVE_PERIOD)*time)*127, 0)
    color = (127+color_change, 127+color_change, 127+color_change)
    return color

def grid_position(position):
    x = (position[0]//CELL)*CELL
    y = (position[1]//CELL)*CELL
    return (x,y)

def longitudinal_wave(position, time):
    
    
    
    pass
    
def waving_func(position, time, center, window):
    
    
    distance = math.dist(position,center)
    
    z = 127*math.exp(-ALPHA*time)*(math.sin((2*math.pi/WAVE_LENGHT)*(WAVE_SPEED*time)))
    color = (127+z, 127+z, 127+z)
    
    particle = pygame.Rect(position[0], position[1],CELL,CELL)
    pygame.draw.rect(window, color ,particle)
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
                #print("x: "+str(pos[0])+ "  ;  y: "+str(pos[1]))
                center = [pos, time]
                centers.append(center)
                print(centers)
            if event.type == pygame.MOUSEMOTION: 
                pass
                """if pygame.mouse.get_pressed()[0]: 
                    pos = pygame.mouse.get_pos()
                    print("x: "+str(pos[0])+ "  ;  y: "+str(pos[1])) 
                    position.append(pos)"""
                    
                    
                
                
                
                    
            if event.type == pygame.MOUSEBUTTONUP: 
                print("button up")
        time += 1
        
        draw_window(centers, time)
        
    
    pygame.quit()


if __name__=="__main__":
    main()