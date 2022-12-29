
from random import randint, choice

#-----Data Set Function------------------#
# The function creates a random data set defining the overall image to draw. 

def raw_data(width = 1, height = 1):
    
    # Define the variants
    variants = ['A', 'B', 'C', 'D']
    # Define the directions we can move
    directions = ['North', 'South', 'East', 'West']
    # Choose the total number of data items
    # (in addition to the 'start' item)
    num_data = randint(0, 100)
    # Define the likelihood of mutating
    mutation_probability = 20 # percent 

    # Choose the starting point
    x_start = randint(0, width - 1)
    y_start = randint(0, height - 1)
    # Choose the first variant
    variant = choice(variants)
    # Initialise the data set with the first location and variant
    location = [x_start, y_start]
    data_items = [['Start', chr(ord('a') + x_start), y_start + 1, variant]]

    # Add the individual data items
    for datum in range(0, num_data):
        if randint(1, 100) <= mutation_probability:
            # Choose a new variant (remembering that Python lists
            # are mutable and changes are done in-place)
            other_variants = variants.copy()
            other_variants.remove(variant)
            variant = choice(other_variants)
            # Add the mutation to the data set
            data_items.append(['Change', variant])
        else:
            # Choose direction to move
            direction = choice(directions)
            # Choose number of steps (always staying within the grid)
            if direction == 'North':
                num_steps = randint(0, height - location[1] - 1)
                location[1] = location[1] + num_steps
            elif direction == 'South':
                num_steps = randint(0, location[1])
                location[1] = location[1] - num_steps
            elif direction == 'East':
                num_steps = randint(0, width - location[0] - 1)
                location[0] = location[0] + num_steps
            else:
                num_steps = randint(0, location[0])
                location[0] = location[0] - num_steps
            # Add the move to the data set
            data_items.append([direction, num_steps])

    # Print the whole data set to the shell window, nicely laid out
    print('The data set to visualise is as follows:\n')
    print(str(data_items).replace('],', '],\n'))
    if len(data_items) == 1:
        print('\nThere was one step only\n')
    else:
        print('\nThere were', len(data_items), 'steps in total\n')
    # Return the data set to the caller
    return data_items
