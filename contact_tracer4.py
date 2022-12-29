from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Define constant values used in the main program that sets up
# the drawing canvas.  
cell_size = 100 # pixels (default is 100)
grid_width = 9 # squares (default is 9)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = True): # NO! DON'T TOUCH THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('a')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 10, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(cell_size // 6)

    if label_spaces:
        # Left side
        goto(-((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align = 'left', font = big_font)    

    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)

def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#--------------------------------------------------------------------#



#-----Draw Images---------------------------------------------#
# Create a list to save the starting position of each image
start_pos = [xcor(), ycor()] 

# Function to start drawing and filling
def begin(): 
    pendown()
    begin_fill()

# Function to stop drawing and filling
def end(): 
    end_fill()
    penup()

# Draw a box and fill it with a background colour
def square(size, background_col = 'white'): 
    fillcolor(background_col)
    begin()

    for side in range(4):
        forward(size)
        left(90)
        
    end()

# Draw base bird image    
def bird(size):
    # Go to box start 
    setheading(0)
    goto(start_pos[0], start_pos[1])
    bird_size = size / 6

    # Go to bird start position
    forward(size / 3)
    left(90)
    forward(size / 3)

    # Set bird colours
    body_col = '#1E90FF'
    beak_col = '#FF6347'
    wing_col = '#00BFFF'

    # Set correct angle for body
    setheading(290)

    bird_start1 = [xcor(), ycor()] # Save starting position to connect lines 
    circle(bird_size, 15)
    bird_start2 = [xcor(), ycor()] # Save position for correct tail feather position
    
    begin()
    fillcolor(body_col)
    
    # Draw bird body
    circle(bird_size, 175)
    circle(bird_size / 2, 45)
    right(135)

    # Draw head feathers using loop
    for head_tuft in range(3):
        forward(bird_size / 10)
        circle(bird_size / 25, 180)
        forward(bird_size / 10)
        right(150)
    left(70)
    circle(bird_size, 45)
    
    goto(bird_start1[0], bird_start1[1])

    
    # Draw tail feathers
    right(60)
    forward(bird_size / 2)
    for tail_feather in range(2):
        circle(bird_size / 10, 180)
        forward(bird_size / 4)
        right(160)
        forward(bird_size / 6)
    circle(bird_size / 10, 180)
    goto(bird_start2[0], bird_start2[1])

    end()

    # Draw beak
    goto(bird_start1[0], bird_start1[1])
    setheading(290)
    circle(bird_size, 160)
    setheading(45)

    begin()
    fillcolor(beak_col)
       
    for triangle_side in range(3):
        forward(bird_size / 3)
        left(120)

    end()
    
    # Go to outer eye position
    left(90)
    forward(bird_size / 2)

    # Draw outer eye circle
    begin()
    fillcolor('white')
    circle(bird_size / 6)
    end()

    # Go to middle eye circle position
    left(90)
    forward((bird_size / 6) + (bird_size / 12))
    right(270)

    # Draw middle eye circle
    begin()
    fillcolor('black')
    circle(bird_size / 12)
    end()

    # Go to inner eye circle position
    circle(bird_size / 12, 270)

    # Draw middle eye circle
    begin()
    fillcolor('white')
    circle(bird_size / 16)
    end()

    # Go to wing position
    forward(bird_size / 3)
    right(230)
    wing1_start = [xcor(), ycor()]
    
    # Draw wing 
    begin()
    fillcolor(wing_col)
    
    circle(bird_size * 1.5, -45)
    right(180)
    circle(bird_size / 2, 45)
    left(90)
    circle(bird_size, 45)
    circle(bird_size * 2, 30)
    circle(bird_size / 3, 170)
    goto(wing1_start[0], wing1_start[1])
    
    end()

    # Set feet sizes
    leg_size = bird_size / 4
    foot_size = leg_size / 2

    # Go to feet position
    goto(bird_start1[0], bird_start1[1])
    setheading(290)
    circle(bird_size, 45)
    right(90)

    # Draw in feet
    for feet in range(2):
        fillcolor(beak_col)
        begin()
        
        forward(leg_size)
        right(90)
        forward(foot_size)
        left(90)
        forward(foot_size / 2)
        left(90)
        forward(foot_size)
        right(45)
        forward(foot_size)
        left(90)
        forward(foot_size / 2)
        left(90)
        forward(foot_size)
        right(135)
        forward(foot_size)
        left(90)
        forward(foot_size / 2)
        left(90)
        forward(foot_size)
        right(90)
        forward(leg_size)
        
        end()

        # Move forward to second foot position
        forward(-foot_size)
        goto(bird_start1[0], bird_start1[1])
        setheading(290)
        circle(bird_size, 60)
        right(90)

def leaving_home(size = 100):
    # Save start position of image and set correct start direction
    start_pos[0] = xcor()
    start_pos[1] = ycor()
    setheading(0)
    
    square(size, '#0000CD') # Draw in square and background colour

    branch_size = size / 2

    # Go to moon position
    forward(size * 0.8)
    left(90)
    forward(size * 0.75)

    # Set moon and star sizes
    moon_size = size / 8
    star_size = moon_size / 4

    # Draw in first part of moon
    fillcolor('yellow')
    begin_fill()
    right(90)
    circle(moon_size)
    end_fill()

    # Move backwards and draw second circle to give moon shape
    backward(moon_size / 3)
    fillcolor('#0000CD')
    begin_fill()
    circle(moon_size)
    end_fill()

    # Go to star position 
    backward(size / 3)

    # Draw in 3 stars
    for stars in range(3):
        for star in range(5):
            fillcolor('yellow')
            begin_fill()
            forward(star_size)
            right(144)
            forward(star_size)
            end_fill()
        right(135)
        backward(moon_size * 2)

    # Draw tree trunk
    setheading(0)
    goto(start_pos[0], start_pos[1])
    
    fillcolor('#A0522D')
    begin()
    forward(size / 6)
    left(90)
    forward(size)
    left(90)
    forward(size / 6)
    end()

    # Draw tree leaf circle
    left(90)
    forward(size / 3)
    left(90)

    fillcolor('#008000')
    begin()
    
    circle(size / 3, 90)
    for filling_greenery in range(2):
        left(90)
        forward(size / 3)

    end()
    
    # Go to tree hole position
    forward(size / 6)
    left(90)
    forward(size / 10)

    # Draw tree hole
    fillcolor('#8B4513')
    begin()
    for oval_shape in range(2):
        circle(branch_size / 12, 180)
        forward(branch_size / 12)
    end()

    # Go to branch position
    right(90)
    forward(size / 3)
    left(90)
    forward(branch_size / 12)

    # Draw branch
    begin()
    left(10)
    forward(branch_size)
    right(90)
    forward(branch_size / 8)
    right(90)
    forward(branch_size)
    end()

    # Go to end of branch
    right(180)
    forward(branch_size)
    right(45)

    # Draw nest  
    begin()
    circle(branch_size / 6)
    end()

    left(90)
    forward(branch_size / 12)
    right(90)
    begin()
    circle(branch_size / 12)
    end()

    # Draw eggs
    for eggs in range(2):
        for egg_shape in range(2):
            begin()
            fillcolor('#F0E68C')
            circle(branch_size / 24, 180)
            forward(branch_size / 12)
            end()
        right(90) 

    # Draw bird in
    bird(size)

    # Go to hat position
    goto(start_pos[0], start_pos[1])
    setheading(0)
    forward(size * (2 / 5))
    left(90)
    forward(size / 3)

    setheading(290)
    circle(size / 7, 210)

    hat_size = size / 10

    # Draw hat
    fillcolor('#C71585')
    begin()
    left(25)
    for sleep_hat_bottom in range(2):
        forward(hat_size)
        circle(hat_size / 4, 180)
    for sleep_hat_top in range(2):
        forward(hat_size)
        right(120)
    end()

    right(180)

    fillcolor('#EE82EE')
    begin()
    circle(hat_size / 5)
    end()

    # Reset position for next drawing
    setheading(0)
    goto(start_pos[0], start_pos[1])

def mountain_tree(size):
    # Draw tree trunk
    tree_size = size / 6
    left(90)

    fillcolor('brown')
    begin()
    for tree_trunk in range(2):
        forward(tree_size)
        right(90)
        forward(tree_size / 4)
        right(90)
    end()

    # Go to tree top position
    tree_top_size = tree_size * (2 / 3)
    forward(tree_top_size)
    left(90)
    forward(tree_top_size / 3)
    left(180)

    # Draw tree top
    fillcolor('dark green')
    begin()
    for tree_top in range(3):
        forward(tree_top_size)
        left(120)
    end()
      
def mountain_trip(size = 100):
    # Save start position of image and set correct start direction
    start_pos[0] = xcor()
    start_pos[1] = ycor()
    setheading(0)
    
    # Draw in square and background colour
    square(size, '#00BFFF')

    # Draw in ground
    fillcolor('#32CD32')
    begin()
    for ground in range(2):
        forward(size)
        left(90)
        forward(size / 3)
        left(90)
    end()

    # Draw in mountains
    mountain_size = size / 3
    
    left(90)
    forward(size / 3)
    right(90)

    # Draw side mountains
    fillcolor('#DCDCDC')
    for small_mountains in range(2):
        begin()
        for small_mountain_side in range(3):
            forward(mountain_size)
            left(120)
        end()
        forward(mountain_size * 2)

    # Draw middle mountain
    backward(mountain_size * 3.5)

    begin()
    for middle_mountain_sides in range(3):
        forward(mountain_size * 2)
        left(120)
    end()

    # Go to snow start position
    left(60)
    forward(mountain_size * 2)
    mountain_top = [xcor(), ycor()]
    backward(mountain_size * 0.5)
    right(35)

    # Draw in snow cap
    fillcolor('white')
    begin()
    forward(mountain_size * 0.2)
    right(90)
    forward(mountain_size * 0.1)
    left(100)
    forward(mountain_size * 0.15)
    right(85)
    forward(mountain_size * 0.2)
    left(130)
    forward(mountain_size * 0.1)
    goto(mountain_top[0], mountain_top[1])
    setheading(240)
    forward(mountain_size * 0.5)
    end()
        
    # Go to lake position
    left(30)
    forward(mountain_size * 1.3)

    # Save lake starting position
    lake_start = [xcor(), ycor()]

    # Draw lake
    fillcolor('#00BFFF')
    begin()
    
    lake_size = mountain_size * 0.75
    circle(lake_size, 90)
    forward(lake_size * 1.3)
    left(90)
    forward(lake_size / 3)
    left(90)
    forward(lake_size)
    left(180)
    circle(lake_size - (lake_size / 3), -90)
    right(90)
    goto(lake_start[0], lake_start[1]) # Finishes off lines neat

    end()

    # Go to tree position
    goto(start_pos[0], start_pos[1])
    setheading(0)
    forward(size / 15)

    # Draw trees
    for draw_trees in range(2):
        for draw_tree_row in range(3):
            mountain_tree(size)
            forward(size / 10)
        goto(start_pos[0], start_pos[1])
        forward(size / 5)
        
    # Draw bird in
    bird(size)

    # Go to bird scarf position
    setheading(0)
    goto(start_pos[0], start_pos[1])
    forward(size / 3)
    left(90)
    forward(size / 3)
    right(45)
    forward(size / 8)
    right(80)

    # Draw scarf
    scarf_size = size /4
    begin()
    for scarf in range(2):
        forward(scarf_size)
        circle(scarf_size / 10, 180)
    end()

    # Draw stripes
    left(90)
    for stripes in range(4):
        fillcolor('green')
        begin()
        for stipe in range(4):
            forward(scarf_size / 5)
            right(90)
            forward(scarf_size / 8)
            right(90)
        end()
        right(90)
        forward(scarf_size / 4)
        left(90)

    # Reset position for next drawing
    setheading(0)
    goto(start_pos[0], start_pos[1])
    
def beach_trip(size = 100):
    # Save start position of image and set correct start direction
    start_pos[0] = xcor()
    start_pos[1] = ycor()
    setheading(0)

    # Draw in square and background colour
    square(size, '#E0FFFF')

    # Draw water in
    left(90)
    
    fillcolor('#00BFFF')
    begin()
    
    for water_sides in range(2):
        forward(size / 3)
        right(90)
        forward(size)
        right(90)
    end()

    # Draw sand in
    fillcolor('#FFDEAD')
    begin()

    forward(size / 3)
    right(90)
    forward(size / 2)
    right(135)
    circle(size / 12, 90)
    right(180)
    circle(size / 12, -90)
    right(180)
    circle(size / 12, 70)
    goto(start_pos[0] + (size / 2), start_pos[1])
    end()

    # Go to sun start location
    setheading(0)
    forward(size / 4)
    left(90)
    forward(size * (2 / 3))
    right(90)

    sun_size = size / 8
    sun_size2 = size / 12

    # Draw outter sun circle
    begin()
    fillcolor('#FFA500')
    circle(sun_size)
    end()

    # Draw sun ray triangles around sun
    for sunrays in range(6):
        fillcolor('#FFD700')
        begin()          
        for sunray in range(3):
            forward(sun_size / 2)
            right(120)
        end()
        circle(sun_size, 60)
        
    # Go to inner sun position
    left(90)
    forward(sun_size2 / 2)
    right(90)

    # Draw inner circle for sun
    fillcolor('#FF8C00')
    begin()
    circle(sun_size2)
    end()

    # Go to coconut tree starting position
    goto(start_pos[0], start_pos[1])
    setheading(0)
    forward(size / 8)
    
    coconut_tree_size = size 
    coconut_end_size = coconut_tree_size / 24

    # Draw and fill coconut tree trunk
    fillcolor('#CD853F')
    begin()
    left(270)
    circle(coconut_tree_size, -30)
    left(180)
    circle(coconut_end_size, 90)
    
    # Save top of tree position to draw leaves
    leaves_start_pos = [xcor(), ycor()] 

    # Continue drawing rest of tree trunk
    circle(coconut_end_size, 90)
    circle(coconut_tree_size, 30)
    goto(xcor(), start_pos[1])
    end()

    # Draw leaves
    leaf_size = coconut_end_size * 2.5

    # Go to leaves start position
    goto(leaves_start_pos[0], leaves_start_pos[1])
    right(180)
    backward(coconut_end_size / 2)

    # Draw 3 sets of pairs of leaves
    for leaves in range(3):
        for leaf_pair in range(2):
            leaf_start = [xcor(), ycor()]
            fillcolor('#228B22')
            begin()
            circle(leaf_size, 180)
            right(45)
            circle(leaf_size * 1.5, -60)
            goto(leaf_start[0], leaf_start[1])
            end()
            right(135)
        backward(coconut_end_size / 3)
    
    # Draw bird in
    bird(size)

    # Draw fish
    fish_size = size / 20
    right(90)

    # Draw fish body
    begin()
    for fish in range(2):
        circle(fish_size, 180)
        forward(fish_size / 2)
    end()

    # Go to back of fish
    circle(fish_size, 90)
    right(120)

    # Draw fish tail
    begin()
    for fish_tail_side in range(3):
        forward(fish_size)
        left(120)
    end()

    # Go to fish eye
    right(150)
    forward(fish_size * 2)

    # Draw fish eye
    eye_size = fish_size / 4
    
    fillcolor('white')
    begin()
    circle(eye_size)
    end()

    left(90)
    forward(eye_size / 2)

    fillcolor('black')
    begin()
    circle(eye_size / 2)
    end()

    # Go to boat position
    goto(start_pos[0] + (size * 0.9), start_pos[1] + (size / 3))
    setheading(45)

    # Draw boat
    boat_size = size / 6
    boat_size_bottom = size / 20

    # Draw base of boat
    fillcolor('#808080')
    begin()
    forward(boat_size / 2)
    left(135)
    forward(boat_size)
    left(135)
    forward(boat_size / 2)
    left(45)
    forward(boat_size_bottom)
    end()

    # Go to flag pole position
    backward(boat_size_bottom / 2)
    left(90)
    forward(size / 17)

    # Draw pole
    pole_size = boat_size / 4
    fillcolor('brown')
    begin()
    for pole in range(2):
        forward(pole_size)
        left(90)
        forward(pole_size / 2)
        left(90)
    end()

    # Go to flag position
    forward(pole_size)
    flag_pos = [xcor(), ycor()]

    # Drag flag
    fillcolor('red')
    begin()
    forward(pole_size)
    left(135)
    forward(pole_size * 1.4)
    left(135)
    forward(pole_size)
    end()
    
    # Reset position for next drawing
    setheading(0)
    goto(start_pos[0], start_pos[1])
    
def thunder_clouds(cloud_size, lightning = 0):
    cloud_col = randint(1, 5) # Choose a random cloud colour from list
    
    if cloud_col == 1:
        fillcolor('white')
    elif cloud_col == 2:
        fillcolor('#F5F5F5')
    elif cloud_col == 3:
        fillcolor('#DCDCDC')
    else: 
        fillcolor('#696969')

    cloud_curves = cloud_size / 3

    forward(cloud_size) # Go to cloud start

    # Draw cloud
    begin()

    cloud_start = [xcor(), ycor()]
    circle(cloud_curves, 170)
    right(90)
    circle(cloud_curves * 2, 190)
    right(90)
    circle(cloud_curves, 170)
    right(90)
    circle(cloud_curves, 180)
    right(180)
    circle(cloud_curves, 180)
    goto(cloud_start[0], cloud_start[1])
      
    end()

    if lightning == 1:
        # Go to lightning start position
        circle(cloud_curves, 180)
        forward(cloud_curves * 0.66)
        right(30)

        # Save start position to make it pretty
        lightning_start = [xcor(), ycor()]
        
        # Draw in lightning
        fillcolor('yellow')
        begin()
        forward(cloud_size)
        left(135)
        forward(cloud_size / 4)
        right(135)
        forward(cloud_size / 2)
        left(160)
        forward(cloud_size * 0.75)
        left(135)
        forward(cloud_size / 3)
        right(115)
        forward(cloud_size * 0.7)
        goto(lightning_start[0], lightning_start[1])
        end()
    setheading(0)

# Create rain drop function to reuse in ocean_trip image
def rain_drop(size):
    rain_drop_size = size / 50
    setheading(315)
    fillcolor('#87CEEB')
    begin()
    
    circle(rain_drop_size, 180)
    left(30)
    forward(rain_drop_size * 2)
    left(120)
    forward(rain_drop_size * 2)
    
    end()
    
def ocean_trip(size = 100):
    # Save start position of image and set correct start direction
    start_pos[0] = xcor()
    start_pos[1] = ycor()
    setheading(0)
    
    # Draw in square and background colour
    square(size, '#708090')

    # Go to rain drop position
    left(90)
    forward(size / 5)
    right(90)
    forward(size / 20)
    rain_drop_start = [xcor(), ycor()]
    
    # Draw in rain drops
    for rain_drop_column in range(10):
        for rain_drop_row in range(10):
            rain_drop_chance = randint(1,3)
            if  rain_drop_chance == 1:
                rain_drop(size)
            setheading(0)
            forward(size / 10)
        rain_drop_start[1] = rain_drop_start[1] + (size / 20)
        goto(rain_drop_start[0], rain_drop_start[1])
            
    # Go to water position
    goto(start_pos[0], start_pos[1])
    left(90)
    forward(size / 6)
    right(90)

    # Draw and fill water
    wave_curve = size / 8

    fillcolor('#00008B')
    begin()

    # Draw top darker waves
    for top_waves in range(4): # Draw 4 wave curves
        circle(wave_curve, 90)
        left(90)
        circle(wave_curve, -90)
        right(90)
    right(90)
    forward(size / 12)
    right(90)
    forward(size)
    end()

    left(180)

    # Draw bottom waves
    fillcolor('#0000FF')
    begin()
    for bottom_waves in range(4): # Draw 4 wave curves
        circle(wave_curve, 90)
        left(90)
        circle(wave_curve, -90)
        right(90)

    right(90)
    forward(size / 12)
    right(90)
    forward(size)
    end()
    
    # Go to cloud position
    setheading(0)
    goto(start_pos[0] + (size / 9), start_pos[1] + (size * 0.75))
    cloud_pos = [xcor(), ycor()]
    
    # Decide if clouds should have lightning and draw clouds
    for clouds in range(4):
        clouds_lightning = randint(1, 3)
        thunder_clouds(size / 6, clouds_lightning)
        cloud_pos[0] = cloud_pos[0] + (size / 4.5)
        goto(cloud_pos[0], cloud_pos[1])

    # Draw bird in
    bird(size)

    # Go to jacket position
    goto(start_pos[0] + (size / 3), start_pos[1] + (size / 3))
    setheading(290)
    circle(size / 6, 160)
    left(90)

    # Save jacket position for later
    jacket_start = [xcor(), ycor()]

    # Draw jacket
    fillcolor('yellow')
    begin()

    jacket_size = size / 8
    
    forward(jacket_size)
    right(30)
    forward(jacket_size)
    circle(jacket_size / 2, -170)
    right(90)
    forward(jacket_size / 3)
    left(45)
    circle(jacket_size * 1.25, 165)

    end()

    # Go to pocket position
    left(135)
    forward(jacket_size)
    right(135)

    pocket_start = [xcor(), ycor()] # Save pocket start location

    # Draw pocket
    fillcolor('#FFD700')
    begin()
    for pocket in range(2):
        circle(jacket_size / 4, -90)
        backward(jacket_size / 4)
    goto(pocket_start[0], pocket_start[1])
    end()

    # Go to rain hat position
    goto(jacket_start[0], jacket_start[1])
    setheading(90)
    forward(size / 12)
    left(90)
    forward(jacket_size / 5)
    # Draw rain hat
    hat_size = jacket_size * 1.5

    # Draw hat triangle
    fillcolor('yellow')
    begin()
    for hat_side in range(3):
        forward(hat_size)
        right(120)
    end()
    backward(hat_size * 0.1)

    # Draw hat base
    begin()
    for hat_base in range(2):
        forward(hat_size * 1.2)
        right(90)
        forward(hat_size / 4)
        right(90)
    end()

    # Go to umbrella position
    forward(hat_size * 1.7)
    right(45)
    backward(hat_size / 2)

    # Draw tiny umbrella
    umbrella_size = hat_size * 0.75

    fillcolor('red')
    begin()
    forward(umbrella_size)
    right(90)
    forward(umbrella_size * 0.9)
    left(90)
    circle(umbrella_size, 180)
    left(90)
    forward(umbrella_size * 0.9)
    right(90)
    forward(umbrella_size)
    left(90)
    forward(umbrella_size / 5)
    end()

    # Draw umbrella stripe
    left(90)
    forward(umbrella_size)
    fillcolor('green')
    begin()
    for umbrella_stripe in range(2):
        forward(umbrella_size)
        left(90)
        forward(umbrella_size / 5)
        left(90)
    end()

    # Reset position for next drawing
    setheading(0)
    goto(start_pos[0], start_pos[1])

# Set style for text
font_style = ('Arial', 12, 'normal')
title_style = ('Arial', 18, 'normal')


# Draw images as key on right hand side with labels
def image_key():
    penup()
    goto(500, 300)

    # Draw in title
    color('black')
    write('A Birds Adventure', align = 'left', font = title_style)
    setheading(270)
    forward(125)    
    
    # Draw in images with text
    leaving_home()
    setheading(270)
    forward(25)
    color('black')
    write('A. Leaving Home', align = 'left', font = font_style)
    forward(125)

    mountain_trip()
    setheading(270)
    forward(25)
    color('black')
    write('B. Mountain Trip', align = 'left', font = font_style)
    forward(125)

    beach_trip()
    setheading(270)
    forward(25)
    color('black')
    write('C. Beach Trip', align = 'left', font = font_style)
    forward(125)
    
    ocean_trip()
    setheading(270)
    forward(25)
    color('black')
    write('D. Ocean Trip', align = 'left', font = font_style)



def visualise(data):
    image_key() # Draw key on right hand side of screen
    image_letter = ''  # Create letter variable to be used in functions below

    # Determine starting position from instructions and go to that position
    def start_pos(letter, number):
        # Go to bottom left corner of grid
        goto(-450, -350)                            
        # Create list with letters from grid
        column_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',] 
        cycle_pos = 0
        # Compare letter from instruction with letters in list
        # If it finds a match go forward to that letters position on the grid
        for match in column_letters:                
            if letter == match: 
                setheading(0)                       
                forward(column_letters.index(match) * 100)
            cycle_pos = cycle_pos + 1
        setheading(90)
        forward((number - 1) * 100)  # Go up to the starting number position

    # Choosing which image to draw based on instruction letter
    def choose_image(letter):
        global image_letter # Setting image_letter to global to edit in function
        if letter == 'A':
            leaving_home()
            image_letter = 'A'
        elif letter == 'B':
            mountain_trip()
            image_letter = 'B'
        elif letter == 'C':
            beach_trip()
            image_letter = 'C'
        elif letter == 'D':
            ocean_trip()
            image_letter = 'D'
            
    # Drawing image based on currently selected letter 
    def draw_image():
        global image_letter # Setting image_letter to global to edit in function
        if image_letter == 'A':
            leaving_home()
        elif image_letter == 'B':
            mountain_trip()
        elif image_letter == 'C':
            beach_trip()
        elif image_letter == 'D':
            ocean_trip()
        
    # Loop that cycles through each     
    for instruction in data:
        number_of_steps = instruction[1] # Saves the number of steps to loop through
        # Checks if the current position of variable data_location is in the
        # first position of the list
        if instruction[0] == 'Start':
            # Chooses starting position based on instructions
            start_pos(instruction[1], instruction[2])
            # Chooses image based on the first instruction
            choose_image(instruction[3])
            update()

        # Checks if the instruction contains a change instruction
        elif instruction[0] == 'Change':
            # Draws the image it is changed to and sets variable to be for that image
            choose_image(instruction[1])
            update()

        # Check direction in instruction to determine where to move and
        # how far to move.        
        elif number_of_steps == 0:
            draw_image()
            update()
            
        elif instruction[0] == 'North':
            for steps in range(number_of_steps):
                draw_image()
                setheading(90)
                forward(100)
                update()
            
        elif instruction[0] == 'East':
            for steps in range(number_of_steps):
                draw_image()
                setheading(0)
                forward(100)
                update()
                
        elif instruction[0] == 'South':
            for steps in range(number_of_steps):
                draw_image()
                setheading(270)
                forward(100)
                update()
                
        elif instruction[0] == 'West':
            for steps in range(number_of_steps):
                draw_image()
                setheading(180)
                forward(100)
                update()
                      
    # Draw final variant on left hand side of screen
    goto(-600, -50)
    draw_image()
    setheading(90)
    forward(125)
    color('black')
    write('Final variant:', align = 'left', font = font_style)
            
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#

### Define the function for generating data sets, using the
### "raw data" function if available, but otherwise
### creating a dummy function that returns an empty list
if isfile('data_generator.py'):
    print('\nNote: Data module found\n')
    from data_generator import raw_data
    def data_set(new_seed = None):
        seed(new_seed)
        return raw_data(grid_width, grid_height)
else:
    print('\nNote: No data module available\n')
    def data_set(dummy_parameter = None):
        return []

#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#

create_drawing_canvas(label_spaces = False)

# Control the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
tracer(False)

# Give the drawing canvas a title
title("A birds adventure")

# Call the function to process the data set
visualise(data_set()) 

# Exit drawing
release_drawing_canvas()

#--------------------------------------------------------------------#
