import pygame
import math

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    
    #-----------------------------Program Variable Initialization----------------------------#
    # Set up some data to describe a small circle and its color
    RED = pygame.Color(255,0,0) #RGB is accepted
    GREEN = pygame.Color('#00FF00') #Hex Codes Accepted
    BLUE = pygame.Color("blue") #Predefined colors accepted 
    LIGHT_PURPLE = pygame.Color('mediumpurple1') #There are a LOT! See https://www.pygame.org/docs/ref/color_list.html
    
    circleColor = LIGHT_PURPLE        # A color is a mix of (Red, Green, Blue)

    #-----------------------------Main Program Loop---------------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...


        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))

        # Draw a circle on the surface
        pygame.draw.circle(mainSurface, circleColor, (50,100), 20)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()
