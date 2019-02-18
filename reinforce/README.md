[//]: # (Image References)

# REINFORCE

## Introduction

### Objective

Train an agent with the [REINFORCE algorithm](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf) to solve the [CartPole-v0 environment](https://gym.openai.com/envs/CartPole-v0/).

<p align="center"><a href="https://github.com/plopd/deep-reinforcement-learning/blob/master/reinforce/results/smart_agent.gif">
 <img width="512" height="256" src="https://github.com/plopd/deep-reinforcement-learning/blob/master/reinforce/results/smart_agent.gif"></a>
</p>

### Background

A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and the goal is to prevent it from falling over.

**Reward:**
A reward of +1 is provided for every timestep that the pole remains upright.

**State:**
```
        Type: Box(4)
        Num	Observation                 Min         Max
        0	Cart Position             -4.8            4.8
        1	Cart Velocity             -Inf            Inf
        2	Pole Angle                 -24°           24°
        3	Pole Velocity At Tip      -Inf            Inf
```

**Actions:**
```Type: Discrete(2)
        Num	Action
        0	Push cart to the left
        1	Push cart to the right
```        
*Note: The amount the velocity is reduced or increased is not fixed as it depends on the angle the pole is pointing. This is because the center of gravity of the pole increases the amount of energy needed to move the cart underneath it.*

**Episode Termination:**
- Pole Angle is more than ±12°
- Cart Position is more than ±2.4 (center of the cart reaches the edge of the display)
- Episode length is greater than 200

**Solved Requirements**
- Considered solved when the average reward is greater than or equal to 195.0 over 100 consecutive trials


## Getting Started

Run
```
jupyter-notebook
```

## References

- [Policy Gradient Methods for Reinforcement Learning with Function Approximation](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf)
- [Deep Reinforcement Learning: Pong from Pixels](http://karpathy.github.io/2016/05/31/rl/)
