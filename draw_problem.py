import string
import numpy as np
import csv

hold_difficulty = {}
with open('hold_difficulty.csv', mode='r') as infile:
    reader = csv.reader(infile)
    hold_difficulty = {rows[0]:rows[1] for rows in reader}


#XY columns/rows  holds names
X_GRID_NAMES = string.ascii_uppercase[0:11]
Y_GRID_NAMES = list(range(1, 19))

# holds row/columns coordinates (in pixels)
X = {xk:int(n+3) for n,xk in enumerate(X_GRID_NAMES)}  
# the 3 ensures the Moonboard, that is rectangular 18x11, is at middle of the 18x18 square 
# this script produces in the draw_problem_matrix function
Y = {yk:int(18-yk) for yk in Y_GRID_NAMES}

def emph_hold_centered(img, h1, holds, filter_shape):
    """draw out the surroundings with hold position at center"""
    xc1 = X[h1[0]]
    yc1 = 18-int(h1[1:])
    for h2 in holds:
        xc2 = X[h2[0]]
        yc2 = 18-int(h2[1:])
        if xc2-xc1 <= filter_shape[0]//2 and xc1-xc2 <= filter_shape[0]//2 and yc1 - yc2 <= filter_shape[0]//2 and yc2 - yc1 <= filter_shape[0]//2 :
            img[filter_shape[0]//2 + yc2-yc1,filter_shape[1]//2 + xc2-xc1] = 0.66  
            # all neighbors get assigned 0.66, as if they're medium hard / neutral
    img[filter_shape[0]//2,filter_shape[1]//2] = hold_difficulty[h1]  
    # the center hold gets assigned 0.33 for easy, 0.66 for medium, 1 for hard
    return img

def emph_hold(img, xc, yc, color):
    """draw rectagle around hold position"""
    x,y = X[xc],Y[yc]
    img[y,x] = color
    return img


def draw_problem_matrix(holds):
    """draw out full problem """
    bg = np.zeros((18,18))
    for h in holds:
        emph_hold(bg,h[0],int(h[1:]), 0.66)
    return bg

def draw_problem_submatrices(holds, filter_shape=(13,13), max_holds=12):
    output = []
    for i in range(len(holds)):
        bg = np.zeros(filter_shape)
        h = holds[i]
        submatrix = emph_hold_centered(bg, h, holds, filter_shape)
        output.append(submatrix)
    # Now I will duplicate hold neighborhoods so as to reach 12 total submatrix inputs to the ML network
    L = len(output)
    output_original = output
    for i in range(max_holds-L):
        r = np.random.randint(len(output_original))
        output.append(output_original[r])
        # output.append(np.zeros(filter_shape))  #  I tried to not duplicate, but only add zero submatrices. Results were not as good
    return output
        
        
        

