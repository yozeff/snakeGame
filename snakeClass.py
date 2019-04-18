#Joseph Harrison 2019
#snake implementation

HEAD = 'O'
BODY = 'o'

class Snake:

    def __init__(self, pos):
        self.pos = pos
        self.ptr = None

    def update_pos(self, vector):
        #head of snake
        if self.ptr == None:
            i = self.pos[0] + vector[0]
            j = self.pos[1] + vector[1]
            self.pos = i, j
        else:
            self.pos = self.ptr.pos
            self.ptr.update_pos(vector)

    def copy_to_array(self, array):
        array[self.pos[0]][self.pos[1]] = HEAD
        if self.ptr != None:
            array[self.pos[0]][self.pos[1]] = BODY
            array = self.ptr.copy_to_array(array)
        return array

    def get_head_pos(self):
        if self.ptr == None:
            return self.pos
        else:
            return self.ptr.get_head_pos()

    def check_collision(self, pos):
        if self.ptr == None:
            return False
        elif self.pos == pos:
            return True
        else:
            return self.ptr.check_collision(pos)

