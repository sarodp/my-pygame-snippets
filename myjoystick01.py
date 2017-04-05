#!usr/bin/python3
#myjoystick01.py

"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Show everything we can pull off the joystick
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class TextPrint(object):
    """
    This is a simple class that will help us print to the screen
    It has nothing to do with the joysticks, just outputting the
    information.
    """
    def __init__(self):
        """ Constructor """
        self.reset()
        self.x_pos = 10
        self.y_pos = 10
        self.font = pygame.font.Font(None, 24)

    def print(self, my_screen, text_string):
        """ Draw text onto the screen. """
        text_bitmap = self.font.render(text_string, True, BLACK)
        my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
        self.y_pos += self.line_height

    def reset(self):
        """ Reset text to the top of the screen. """
        self.x_pos = 10
        self.y_pos = 10
        self.line_height = 15

    def indent(self):
        """ Indent the next line of text """
        self.x_pos += 10

    def unindent(self):
        """ Unindent the next line of text """
        self.x_pos -= 10


pygame.init()

# Set the width and height of the screen [width,height]
size = [500, 780]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Joystick Status")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()
tickcount = 0
# -------- Main Program Loop -----------
while not done:
	#========================================================================
    #0..EVENT PROCESSING STEP
	#========================================================================
    xevent = pygame.event.get()
    xeventcnt = (len(xevent)) 
    #for event in pygame.event.get():
    for event in xevent: 
        if event.type == pygame.QUIT:
            done = True

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
        # JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

	#========================================================================
    #1-- screen.reset
    #  textPrint(...)
    # First, clear the screen to white. 
    # Don't put other drawing commands above this
    # or they will be erased with this command.
	#========================================================================
    screen.fill(WHITE)
    textPrint.reset()
    tickcount +=1
    if (tickcount >= 60):
        tickcount = 0
    textPrint.print(screen, "tickcount: {}".format(tickcount))	
    textPrint.print(screen, "eventcount: {}".format(xeventcnt))	

    #1a-- Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.print(screen, "-----------------------------------------------")
    textPrint.indent()

    #1b-- For each joystick:
    for ji in range(joystick_count):
        joystick = pygame.joystick.Joystick(ji)
        joystick.init()

        textPrint.print(screen, "Joystick {}".format(ji))
        textPrint.indent()

        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for xi in range(axes):
            axis = joystick.get_axis(xi)
            #textPrint.print(screen, "Axis {} value: {:&gt;6.3f}".format(i, axis))
            textPrint.print(screen, "Axis {} value: {}".format(xi, axis))
        textPrint.unindent()

        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for bi in range(buttons):
            button = joystick.get_button(bi)
            #textPrint.print(screen, "Button {:&gt;2} value: {}".format(i, button))
            textPrint.print(screen, "Button {} value: {}".format(bi, button))
        textPrint.unindent()

        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        textPrint.print(screen, "Number of hats: {}".format(hats))
        textPrint.indent()

        for hi in range(hats):
            hat = joystick.get_hat(hi)
            textPrint.print(screen, "Hat {} value: {}".format(hi, str(hat)))
        textPrint.unindent()

        textPrint.unindent()

        textPrint.print(screen, "------------------------------------------")

	#=========================================================================
    # D99.. .flip
    #  Go ahead and update the screen with what we've drawn.
    #  Limit to 60 frames per second
	#========================================================================
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
