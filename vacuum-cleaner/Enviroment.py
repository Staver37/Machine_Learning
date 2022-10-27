import turtle as tt
from Agent import *

DIR_UP    = 0
DIR_RIGHT = 1
DIR_DOWN  = 2
DIR_LEFT  = 3


WALL  = -1
EMPTY = 0
BASE  = 1

DIR_TO_MOVEMENT= [
    None,
    None,
    [# 2    
        [  0, -1 ], # 0
        [  1,  0 ], # 1
        [  0,  1 ], # 2
        [ -1,  0 ]  # 3
    ],   
    [ # 3
        [  0, -1 ], # 0
        [ -1,  0 ], # 1
        [  0, -1 ], # 2
        [  1,  0 ]  # 3  
    ]
]

DRAW_CIRCLE = [
    [90,40,90,10,90 ],
    [90,25,90,25,90 ],
    [90,10,90,10,90 ],
    [90,25,270,5,270]
]



# penalties
PEN_OUTSIDE = -2
PEN_WALL    = -1
PEN_TURN    = -0.5
PEN_FARTHER = -0.5
PEN_WALK    =  0
PEN_CLOSER  =  0.5



class Enviroment:
#                                    x|y        /          x|y      /     dir 
    def __init__(self, room_size = (10,10), robo_coords = [0,0],robo_dir = DIR_RIGHT):

        self.room_size = room_size
        self.room_sectors = [
            [
                EMPTY for x in range(self.room_size[0])
            ]   for y in range(self.room_size[1])
            
        ]
        #self.room_sectors[7][5] = WALL
        self.room_sectors[9][9] = BASE
        self.base =[9,9]
        self.robo_coords = robo_coords
        self.robo_dir = robo_dir

        self.scale = 50 # pixels/coords

    def coordsToPixels(self,coords):
        sx, sy = self.room_size
        x,y = coords
        scrx = ( x - sx / 2) * self.scale
        scry = -(y -sy / 2 ) * self.scale
        return [scrx,scry]  
    
    def render(self):
        draw = tt.Turtle()
        screen = tt.Screen()
        screen.setup(self.room_size[0] * self.scale, self.room_size[1] * self.scale)

    #  squares
        tt.tracer(0,0)
        
        for y in range (self.room_size[1]):
            for x in range (self.room_size[0]):
                draw.penup()
                draw.goto(self.coordsToPixels((x,y)))
                draw.pendown()
                color = 'White'
                if self.room_sectors[y][x] == WALL:
                    color = 'gray'
                if self.room_sectors[y][x] == BASE:
                    color = 'green'

                draw.fillcolor(color)
                draw.begin_fill()
                draw.forward(self.scale)
                draw.right(90)
                draw.forward(self.scale)
                draw.right(90)
                draw.forward(self.scale)
                draw.right(90)
                draw.forward(self.scale)
                draw.right(90)
                draw.end_fill() 

        # adjust  starting point robot
        robot_screen_coords = self.coordsToPixels(self.robo_coords)
        robot_screen_coords[1] -= self.scale
        robot_screen_coords[0] += self.scale / 2
        draw.penup()
        draw.goto(robot_screen_coords)
        draw.pendown()
        draw.fillcolor('gray')
        draw.begin_fill()
        draw.circle(self.scale/2)
        draw.end_fill()

    #   Direction moving    
    # HW 7 Try to optimize the code bellow using matrix
    
        draw.penup  ()
        draw.left   (DRAW_CIRCLE[self.robo_dir][0])
        draw.forward(DRAW_CIRCLE[self.robo_dir][1])
        draw.right  (DRAW_CIRCLE[self.robo_dir][2])
        draw.forward(DRAW_CIRCLE[self.robo_dir][3])
        draw.left   (DRAW_CIRCLE[self.robo_dir][4])
        draw.pendown() 
    #  small circle
        draw.fillcolor('green')
        draw.begin_fill()
        draw.circle(10)
        draw.end_fill()

        
        draw.hideturtle()
        tt.update()
        #tt.done()
        #input()
   


    def dirToMovement(self, action, odirection):
            return DIR_TO_MOVEMENT [action][odirection]

    def getObjectFromCoords(self, x, y):
        if x < 0 or y < 0 or x >= self.room_size[0] or y >= self.room_size[1]:
            return None

        return self.room_sectors[y][x]

    def turn(self,direction,action):
            
            direction += action
            direction %= 4

            if direction < 0:
                direction = 3
            return direction

    def step(self, action, ag , simulate = False):
        pen = PEN_WALK
        rx, ry = self.robo_coords
        rdir  = self.robo_dir
        dist_x = abs(self.base[0] - rx)
        dist_y = abs(self.base[1] - ry)

        if action == ACT_RIGHT or action == ACT_LEFT:
            rdir = self.turn(rdir,action)
            
            # make another virtual step to FRONT
            dx, dy = self.dirToMovement(ACT_FRONT, rdir)
            if self.getObjectFromCoords(rx + dx,ry + dy) == WALL or None:
                pen = PEN_TURN


        elif action == ACT_FRONT or action == ACT_BACK:
            dx, dy = self.dirToMovement(action, rdir)
            rx += dx
            ry += dy

            dist_x = abs(self.base[0] - rx)
            dist_y = abs(self.base[1] - ry)
        
            
            
            if rx >= self.room_size[0] or\
                ry >= self.room_size[1] or\
                rx < 0 or\
                ry < 0:  
                        pen = PEN_OUTSIDE
                        
            elif self.getObjectFromCoords(rx, ry ) == WALL:
                pen = PEN_WALL


            elif ag.last_state != None:
                last_dist_x, last_dist_y = ag.last_state[3]
                if dist_x > last_dist_x or dist_y > last_dist_y:
                    pen = PEN_FARTHER
                elif dist_x < last_dist_x or dist_y < last_dist_y:
                    pen = PEN_CLOSER 
                    print("pen_dist",dist_x,dist_y)


        if not simulate:
            self.robo_coords = [rx,ry]
            self.robo_dir    = rdir

        state = [
            [rx,ry], # [x,y]
            rdir,    # <^>v   
            pen,
            [dist_x, dist_y]
        ]

        return state

    def getState(self):
        state =[
            self.robo_coords, # [x,y]
            self.robo_dir,    # <^>v  
            0
        ]
        return state





