import retro
from stable_baselines.common import make_vec_env
from stable_baselines import A2C
from stable_baselines.common.policies import CnnPolicy
from stable_baselines.common.vec_env import SubprocVecEnv, DummyVecEnv, VecFrameStack, VecNormalize
import numpy as np
import gym
from stable_baselines.common.callbacks import CheckpointCallback
from utils import *

if __name__ == "__main__":
    n_cpu = 10

    env = SubprocVecEnv([make_env]*n_cpu)

    model = A2C(CnnPolicy, env, n_steps=128, nminibatches=1, noptepochs=6,
                 verbose=1, tensorboard_log='log location of your choosing')

    # For loading an already existing model to continue training it
    #model = PPO2.load("training_checkpoints/mario_model.zip", tensorboard_log="./tboard_log")
    # model.set_env(env)

    checkpoint_callback = CheckpointCallback(
        save_freq=1000, save_path='save location of your choice',)

    model.learn(total_timesteps=90_000_000, callback=checkpoint_callback)
    model.save('mario-ppo2')
    env.close()
