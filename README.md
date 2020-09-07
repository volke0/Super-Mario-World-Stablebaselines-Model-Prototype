# Super-Mario-World-Stablebaselines-Model-Prototype
Training a RL agent to play Super Mario World for the SNES 
Hi, this is Volke0, this is my project's code for playing/training a RL agent on Super Mario World on the SNES. The agent was trained using A2C for 120,000,000 time steps on Donut Plains 1. This project is incomplete as I am currently testing other methods besides using A2C to train the agent to play the game.  The model provided can play Donut Plain 1 almost perfectly, however it does not generalize to play other levels that well.  Feel free to train the model yourself and edit the code to help improve this project!

How to play:
Make sure you have all the required modules pip installed:
  *retro
  *gym
  *stable_baselines (going to need to do more to run this on windows, I recommended reading the documentation here for how to install https://stable-baselines.readthedocs.io/en/master/guide/install.html
  *numpy*
 
  
Simply run play-mario.py with the model named a2c-SuperMarioWorld-Snes.zip provided in the source code.


How to train?
Simply fiddle with the training parameters in train-mario.py or just simply run the script.


Credits to OpenAI and the Stablebaselines Team for the awesome modules!
And Lucas Thompson and Will Kwan for their great youtube tutorials and for basing my code of off theirs'. 
Lucas Thompson's video (https://youtu.be/QqYSfclTO1c)
Will Kwan's video (https://youtu.be/-oUVr_B_cQo)
