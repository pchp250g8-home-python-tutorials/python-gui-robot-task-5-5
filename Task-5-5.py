from robot import *

bIsCellPainted = False
bIsCellPaintedLeft = False
bIsCellPaintedRight = False
bIsCellPaintedUp = False
bIsCellPaintedDown = False


while not bIsCellPainted:
    
    while is_free_up() and not bIsCellPainted:
        bIsCellPainted = is_cell_painted()
        if not bIsCellPainted:
            move_up()
    
    while is_free_down() and not bIsCellPainted:
        bIsCellPainted = is_cell_painted()
        if not bIsCellPainted:
            move_down()
    
    while is_free_left() and not bIsCellPainted:
        bIsCellPainted = is_cell_painted()
        if not bIsCellPainted:
            move_left()
        
    
    while is_free_right() and not bIsCellPainted:
        bIsCellPainted = is_cell_painted()
        if not bIsCellPainted:
            move_right()
        
bIsCellPaintedLeft = bIsCellPainted and is_free_right()
bIsCellPaintedRight = bIsCellPainted and is_free_left()
bIsCellPaintedUp = bIsCellPainted and is_free_down()
bIsCellPaintedDown = bIsCellPainted and is_free_up()

if(bIsCellPaintedUp):
    while is_free_down():
        move_down()
    while is_free_left():
        move_left()
        
if(bIsCellPaintedLeft):
    while is_free_right():
        move_right()
    while is_free_up():
        move_up() 

