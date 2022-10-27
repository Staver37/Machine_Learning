from time import sleep
from Enviroment import *
from Agent import Agent


env = Enviroment()

env.room_sectors[0][2] = WALL
env.room_sectors[2][2] = WALL
env.room_sectors[2][1] = WALL
env.room_sectors[1][5] = WALL
env.room_sectors[7][9] = WALL

env.room_sectors[8][7] = WALL
env.room_sectors[8][6] = WALL
env.room_sectors[8][5] = WALL
env.room_sectors[9][8] = WALL
env.room_sectors[8][4] = WALL
env.room_sectors[8][3] = WALL
env.room_sectors[8][3] = WALL
env.room_sectors[8][2] = WALL
env.room_sectors[4][4] = WALL
ag = Agent()


for i in range (80):
    env.render()

    action    = ag.selectAction(env)
    print("select action", action)

    state_after = env.step( action, ag = ag )
    ag.rememberState(state_after)
    sleep(0.6)
    print("state:",state_after)
    
    
    