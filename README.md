# Super-Mario-World-Stablebaselines-Model-Prototype

Hi, this is Volke0, this is my project's code for playing/training a RL agent on Super Mario World on the SNES. The agent was trained using A2C on a CNN (convolutional neural network) for 120,000,000 time steps on Donut Plains 1. 

This project is incomplete as I am currently testing other methods besides using A2C to train the agent to play the game.  The model provided can play Donut Plain 1 almost perfectly, however it does not generalize to play other levels that well.  Feel free to train the model yourself and edit the code to help improve this project!

How to play:

1. Make sure you have all the required modules pip installed: retro, gym, stable_baselines (going to need to do more to run this on windows, I recommended reading the documentation here for how to install https://stable-baselines.readthedocs.io/en/master/guide/install.html, and numpy

2. Afterwards, take the SuperMarioWorld-Snes folder and drop it in \retro\data\stable and replace the existing folder. 

3. In order to play this model you need a LEGAL ROM file of Super Mario World.  After you obtain your LEGAL ROM file, rename it to rom and drop it in your SuperMarioWorld-Snes folder.

4. Optional: If you are running the model that I used for testing go to this link and download it (for it's too big to upload on GitHub): 
https://drive.google.com/file/d/1fHe7nZaiQpIhAOEk3vkTHOyehnaQTjaZ/view?usp=sharing
  
5. Finally, run play-mario.py with the model named a2c-SuperMarioWorld-Snes.zip provided in the source code.


How to train?

Simply fiddle with the training parameters in train-mario.py or just simply run the script.


Credits to OpenAI and the Stablebaselines Team for the awesome modules!

And Lucas Thompson and Will Kwan for their great youtube tutorials and for basing my code of off theirs'. 
Lucas Thompson's video (https://youtu.be/QqYSfclTO1c)
Will Kwan's video (https://youtu.be/-oUVr_B_cQo)
