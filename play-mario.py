import retro
import os
from stable_baselines.common.vec_env import SubprocVecEnv, DummyVecEnv, VecFrameStack, VecNormalize
from stable_baselines import A2C
from stable_baselines.common.policies import CnnPolicy
import numpy as np
import gym
from stable_baselines.common.callbacks import CheckpointCallback
from utils import *


def Play():

    # Must use the same number of envs as trained on but we create a single dummy env for testing.
    #num_envs = 16
    num_envs = 10
    env = SubprocVecEnv([make_env])

    model = A2C.load(f"a2c-SuperMarioWorld-Snes.zip")
    model.set_env(env)
    obs = env.reset()
    print(obs.shape)

    while True:
        action, _states = model.predict(obs)
        obs, rew, done, info = env.step(action)
        env.render()
        if done.all() == True:
            break


if __name__ == "__main__":
    Play()
