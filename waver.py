import pygame
import math

# Define the Board/habitat
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Waver")

BACKGROUND_COLOR = (127,127,127)
CELL = 9
FPS = 60
GRID_WIDTH = WIDTH//CELL
GRID_HEIGHT = HEIGHT//CELL

# Wave definitions
WAVE_PERIOD = 50
WAVE_LENGHT= CELL*10
WAVE_SPEED = WAVE_LENGHT/WAVE_PERIOD
WAVE_NUMBER = 2*math.pi/WAVE_LENGHT
ALPHA = 0.01 # amortiguation

# Color
WHITE = (255,255,255)

# Creat the grid
total_cells = [[(x*CELL, y*CELL), []] for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT)]   # Each cell is a list of one tuple (x and y coordinates) and a list containing a time value for every center created



def draw_window(centers, time):
    """ Draws waves on the display

    Args:
        centers (tuple): clicked cells positions
        time (int): reference time

    Returns:
        pygmae.display: pygame.display object update
    """
    WIN.fill(BACKGROUND_COLOR)
    wave = "Wave"
    
    
    for cell in total_cells:    # loop through every cell to update its color/z coordinate
        ztot = 0    # 0 is the default color, grey in this case. z coordinate is translated into color gradient to give the idea of wave
        for center in centers:  # loop through every wave center
            posgrid = grid_position(center[0])  
            distance = math.dist(cell[0], posgrid)  # get the distance from each center
            
            if distance < WAVE_SPEED * (time-center[1]):    # controls if the wave has reach or not the cell
                try: 
                    waveorder = cell[1][centers.index(center)] # get the center time since it was clicked
                    
                    z = waving_function_indep(waveorder)    # make it wave if already waving for every center
                    ztot += z   # adds the time of the center to itself
                    if ztot > 127: ztot = 127   # prevents overshooting due to limits of the wave function
                    if ztot < -127: ztot = -127
                    cell[1][centers.index(center)] += 1 # adds 1 to time in each center
                except: 
                    cell[1].append(0)   # if the cell is reached by a wave, it adds the center to its list
                    z = waving_function_indep(0) # starts the wave function
                    ztot += z
                    if ztot > 127: ztot = 127
                    if ztot < -127: ztot = -127
        color = (127+ztot, 127+ztot, 127+ztot)  # shows the z coordinate
        particle = pygame.Rect(cell[0][0], cell[0][1],CELL,CELL)    # draws the rectangle
        pygame.draw.rect(WIN, color ,particle)
    
              

    pygame.display.update()
    
    return wave
    
 

def grid_position(position):
    """translates clicks into discrete cell positions. Not using it will create a wave position per pixel and be resource consuming

    Args:
        position (tuple): coordinates

    Returns:
        tuple: cell position
    """
    
    x = (position[0]//CELL)*CELL
    y = (position[1]//CELL)*CELL
    return (x,y)

    


def waving_function_indep(time):
    """ Wave function. Generates values betwenn -127 to 127 to generate the sensation of wave

    Args:
        time (int): time passed since the cell first touch from a wave

    Returns:
        int: z height
    """
    
    z = 127*math.exp(-ALPHA*time)*(math.sin((2*math.pi/WAVE_LENGHT)*(WAVE_SPEED*time)))
    
    return z
    
   

def main():
    """ Main game function
    """
    
    run = True
    centers = []    # points of origin of the waves
    time = 0    # time counter // should have used the tick counter method of pygame for the same effect
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():  # quit app
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: # click on board event
                
                pos = pygame.mouse.get_pos()    # get the position to get the center
                center = [pos, time]    # tiem is necessary to diferentiate the different waves
                centers.append(center)  # add the new center to the wave origins
                
            
            
        time += 1   
        
        draw_window(centers, time)
        
    
    pygame.quit()


if __name__=="__main__":
    main()