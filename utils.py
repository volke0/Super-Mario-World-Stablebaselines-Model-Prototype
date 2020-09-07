import numpy as np
import gym
import retro

class MarioDiscretizer(gym.ActionWrapper):
    '''
    Wrap a gym environment to make it use discrete actions (from William Kwan)
    based on the code https://github.com/wkwan/mkii-subzero-ppo2agent/blob/master/utils.py
    Args:
        buttons: ordered list of buttons, corresponding to each dimension of the MultiBinary action space
        combos: ordered list of lists of valid button combinations
    '''

    def __init__(self, env, buttons, combos):
        super().__init__(env)
        assert isinstance(env.action_space, gym.spaces.MultiBinary)
        self._decode_discrete_action = []
        for combo in combos:
            arr = np.array([False] * env.action_space.n)
            for button in combo:
                arr[buttons.index(button)] = True
            self._decode_discrete_action.append(arr)

        self.action_space = gym.spaces.Discrete(len(self._decode_discrete_action))

    def action(self, a):
        return self._decode_discrete_action[a].copy()

class Mario_Combos(MarioDiscretizer):
    def __init__(self,env):
        super().__init__(env=env, buttons=env.unwrapped.buttons,
            combos=[[], ['B'], ['Y'], ['START'], ['UP'], ['DOWN'], ['LEFT'], ['RIGHT'], ['X'], ['L'], ['R']],)
game = "SuperMarioWorld-Snes"

def make_env():
    env = retro.RetroEnv(game, state="DonutPlains1.state", scenario="ascen",
                            inttype=retro.data.Integrations.ALL, obs_type=retro.Observations.IMAGE)
    #env = Mario_Combos(env)  #turned off for the model I currently have uploaded you can uncomment it when training your model
    return env 

def make_movie():
    env = retro.RetroEnv(game, state="state.state", scenario="ascen",
                            inttype=retro.data.Integrations.ALL, obs_type=retro.Observations.IMAGE, record='.')
    return env