#Joseph Harrison 2019
from snakeClass import Snake
import random
import sys
import os
import termios
import tty
import platform

#determine user's clear command
if platform.system() == 'Windows':
    clrcmd = 'clr'
else:
    clrcmd = 'clear'

FOOD = '.'
SPACE = ' '

#code from:
#https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user/510364
key_Enter = 13
key_Esc = 27
key_Up = '\033[A'
key_Dn = '\033[B'
key_Rt = '\033[C'
key_Lt = '\033[D'
fdInput = sys.stdin.fileno()
termAttr = termios.tcgetattr(0)

def getch():
    tty.setraw(fdInput)
    ch = sys.stdin.buffer.raw.read(4).decode(sys.stdin.encoding)
    if len(ch) == 1:
        if ord(ch) < 32 or ord(ch) > 126:
            ch = ord(ch)
    elif ord(ch[0]) == 27:
        ch = '\033' + ch[1:]
    termios.tcsetattr(fdInput, termios.TCSADRAIN, termAttr)
    return ch
#end

if __name__ == '__main__':
    #get board dimensions
    x, y = int(sys.argv[1]), int(sys.argv[2])
    #initial snake position
    i, j = random.randint(0, y - 1), random.randint(0, x - 1)
    tail = Snake((i, j))
    head = tail.pos     
    #position of food on the board
    food = random.randint(0, y - 1), random.randint(0, x - 1)
    score = 0
    userin = ''
    collision = False
    while userin != 'q' and not collision:
        
        array = [[SPACE for k in range(y)]
                        for l in range(x)] 

        array[food[0]][food[1]] = FOOD
        tail.copy_to_array(array)
    
        #output board
        os.system(clrcmd)
        print(f"{'--' * len(array[0])}- score: {score}")
        for row in array:
            print('|' + ' '.join(row) + '|')
        print('--' * len(array[0]) + '-')

        #if food has been eaten
        if food == head:
            score += 1
            array[food[0]][food[1]] = SPACE         
            #grow snake
            new = Snake((tail.pos[0] - i, tail.pos[1] - j))
            new.ptr = tail
            tail = new
            head = tail.get_head_pos()
            #produce new food
            food = random.randint(0, y - 1), random.randint(0, x - 1)
            array[food[0]][food[1]] = FOOD
        
        #user input
        userin = getch()
        if userin == 'w':
            i, j = -1, 0
        elif userin == 'a':
            i, j = 0, -1
        elif userin == 's':
            i, j = 1, 0
        elif userin == 'd':
            i, j = 0, 1

        #move snake
        head = head[0] + i, head[1] + j
        tail.update_pos((i, j))

        #check for collisions
        if tail.check_collision(head):
            collision = True
        elif head[0] == -1 or head[0] == y:
            collision = True
        elif head[1] == -1 or head[1] == x:
            collision = True

    print('exiting...')


