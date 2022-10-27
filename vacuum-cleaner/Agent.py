ACT_LEFT  = -1
ACT_RIGHT = 1

ACT_FRONT = 2
ACT_BACK  = 3


ACTIONS = [
ACT_FRONT,
ACT_BACK,
ACT_LEFT, 
ACT_RIGHT,
]

from random import betavariate, randint

class Agent:
    
    def __init__(self):
        self.last_state = None # short memory

    # THIS IS MAIN AGENT LOGIC
    def selectAction(self, env):
        penalties = [0,0,0,0]
        for act in range(4):
            
            state = env.step(ACTIONS[act], self, simulate = True )
            penalties[act] = state[2]
            print(" +",act, penalties[act] )


        best_penalty = max(penalties)
        print("Penalties 1:>>> ", penalties, best_penalty)
        selected_action = penalties.index(best_penalty)
        return ACTIONS[selected_action]

    def rememberState(self,state):
        self.last_state = state





