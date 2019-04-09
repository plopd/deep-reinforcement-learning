[//]: # (Image References)

[image2]: https://user-images.githubusercontent.com/10624937/42386929-76f671f0-8106-11e8-9376-f17da2ae852e.png "Kernel"

# A collection of the most notable classical and deep Reinforcement Learning algorithms and methods in the literature
It is largely based on the [standard textbook by Sutton and Barto (ed. II, 2018)](http://incompleteideas.net/book/the-book.html).

Every hyperlinking leads you to a more detailed outlook of that concept. You are encouraged to explore around everything.

## Projects

* [The Taxi Problem](https://github.com/plopd/deep-reinforcement-learning/blob/master/lab-taxi/README.md): Train a taxi to pick up and drop off passengers.
* [Navigation](https://github.com/plopd/navigation): Train an agent with the DQN algorithm to navigate and collect yellow bananas while avoiding blue bananas in a large, square world.
* [Continuous Control](https://github.com/plopd/continuous-control): Train an robotic arm to reach target locations. _Coming soon!_
* [Collaboration and Competition](https://github.com/plopd/multi-agent-control): Train a pair of agents to play tennis!

## OpenAI Gym Benchmarks

### Classic Control
- `Acrobot-v1` with [Tile Coding](https://github.com/plopd/deep-reinforcement-learning/blob/master/tile-coding/Tile_Coding.ipynb) and Q-Learning
- `Cartpole-v0` with [Hill Climbing] | _Coming soon!_
- `Cartpole-v0` with [REINFORCE](https://github.com/plopd/deep-reinforcement-learning/tree/master/reinforce) | solved in 691 episodes
- `MountainCarContinuous-v0` with [Cross-Entropy Method] | _Coming soon!_
- `MountainCar-v0` with [Uniform-Grid Discretization] | _Coming soon!_
- `Pendulum-v0` with [Deep Deterministic Policy Gradients (DDPG)] | _Coming soon!_

### Box2d
- `BipedalWalker-v2` with [Deep Deterministic Policy Gradients (DDPG)] | _Coming soon!_
- `CarRacing-v0` with Deep Q-Networks (DQN) | _Coming soon!_
- `LunarLander-v2` with [Deep Q-Networks (DQN)](https://github.com/plopd/deep-reinforcement-learning/blob/master/dqn/Deep_Q_Network.ipynb) | solved in 295 episodes

### Toy Text
- `FrozenLake-v0` with [Dynamic Programming] | _Coming soon!_
- `Blackjack-v0` with [Monte Carlo Methods](https://github.com/plopd/deep-reinforcement-learning/tree/master/monte-carlo) | solved in 500000 episodes
- `CliffWalking-v0` with [Temporal-Difference Methods](https://github.com/plopd/deep-reinforcement-learning/blob/master/temporal-difference/Temporal_Difference.ipynb) | solved in 5000 episodes

## Dependencies

To set up your python environment to run the code in this repository, follow the instructions below.
Deep
1. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
	
2. Follow the instructions in [this repository](https://github.com/openai/gym) to perform a minimal install of OpenAI gym.  
	- Next, install the **classic control** environment group by following the instructions [here](https://github.com/openai/gym#classic-control).
	- Then, install the **box2d** environment group by following the instructions [here](https://github.com/openai/gym#box2d).
	
3. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.
```bash
git clone https://github.com/udacity/deep-reinforcement-learning.git
cd deep-reinforcement-learning/python
pip install .
```

4. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `drlnd` environment.  
```bash
python -m ipykernel install --user --name drlnd --display-name "drlnd"
```

5. Before running code in a notebook, change the kernel to match the `drlnd` environment by using the drop-down `Kernel` menu. 

![Kernel][image2]

## Acknowledgments

This repository is a fork of Udacity's amazing [Deep Reinforcement Learning Nanodegree](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893) program. I provide **own and extended solutions** to all of Udacity's material.

<p align="center"><a href="https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893"></p>

<p align="center"><a href="https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893">
 <img width="503" height="133" src="https://user-images.githubusercontent.com/10624937/42135812-1829637e-7d16-11e8-9aa1-88056f23f51e.png"></a>
</p>
