## multiples if/else witth similar formulas

#robot movement
#CON:
#  + les of code
#  + simple code
#  + les chages of errors
#  + faster on multi processors
#  + flexible


# control ( if/else) ---> matrices with of coeficience


DIR_UP    = 0
DIR_RIGHT = 1
DIR_DOWN  = 2
DIR_LEFT  = 3


ACT_FRONT = 0
ACT_BACK  = 1
ACT_LEFT  = 2
ACT_RIGHT = 3

action = ACT_BACK
# action = ACT_BACK

rdir = DIR_UP
# rdir = DIR_LEFT
rx = 0
ry = 0

#vvvvvvvvv UNOPTIMIZIMED EXEMPLE vvvvvvvvv#
# if action == ACT_FRONT:
#     if rdir == DIR_UP:
#         ry -= 1
#     if rdir == DIR_RIGHT:
#         rx += 1 
#     if rdir == DIR_DOWN:
#         ry += 1
#     if rdir == DIR_LEFT:
#         rx -= 1 

# if action == ACT_BACK:
#     if rdir == DIR_UP:
#         ry += 1
#     if rdir == DIR_RIGHT:
#         rx -= 1 
#     if rdir == DIR_DOWN:
#         ry -= 1
#     if rdir == DIR_LEFT:
#         rx += 1 
# print(action)
#^^^^^^^UNOPTIMIZIMED EXEMPLE^^^^^^#

##vvvv shape[1,1] (bidimentional) <- EXEMPLE vvvvv#

    # FRONT 
    # dir name |DIR | rx | ry | 
    #    UP    | 0  |  0 | -1 |
    #   RIGHT  | 1  | +1 |  0 |
    #   DOWN   | 2  |  0 | +1 |
    #   LEFT   | 3  | -1 |  0 |

    # BACK
    # dir name |DIR | rx | ry | 
    #    UP    | 0  |  0 | +1 |
    #   RIGHT  | 1  | -1 |  0 |
    #   DOWN   | 2  |  0 | -1 |
    #   LEFT   | 3  | +1 |  0 |
# FRONT_DIR_TO_MOVEMENT =[
#         [  0, -1 ], # 0
#         [  1,  0 ], # 1
#         [  0,  1 ], # 2
#         [ -1,  0 ]  # 3
#         ]
# BACK_DIR_TO_MOVEMENT =[
#         [  0, -1 ], # 0
#         [ -1,  0 ], # 1
#         [  0, -1 ], # 2
#         [  1,  0 ]  # 3
#         ]


# if action == ACT_FRONT:
#     rx += FRONT_DIR_TO_MOVEMENT[rdir][0]
#     ry += BACK_DIR_TO_MOVEMENT [rdir][1]
    
# if action == ACT_BACK:
#     rx += FRONT_DIR_TO_MOVEMENT[rdir][0]
#     ry += BACK_DIR_TO_MOVEMENT [rdir][1]
##^^^^^^ shape[1,1] (bidimentional) <- EXEMPLE ^^^^^#





# #vvvvvvvvvv (threedimentional)<- EXEMPLE vvvvvvvvv#
DIR_TO_MOVEMENT= [
    [# 0    
        [  0, -1 ], # 0
        [  1,  0 ], # 1
        [  0,  1 ], # 2
        [ -1,  0 ]  # 3
    ],   
    [ # 1
        [  0, -1 ], # 0
        [ -1,  0 ], # 1
        [  0, -1 ], # 2
        [  1,  0 ]  # 3  
    ]
]
if action == ACT_FRONT or action == ACT_BACK:
    rx += DIR_TO_MOVEMENT [action][rdir][0]
    ry += DIR_TO_MOVEMENT [action][rdir][1]

print(rx,ry)
# #^^^^^^^^^^(threedimentional)<- EXEMPLE ^^^^^^^^^^^#





