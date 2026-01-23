#!/usr/bin/env python3
import gym_duckietown
from gym_duckietown.simulator import Simulator
import numpy as np

env = Simulator(
    seed=123,
    map_name="small_loop",
    max_steps=500001,
    domain_rand=0,
    camera_width=640,
    camera_height=480,
    accept_start_angle_deg=4,
    full_transparency=True,
    distortion=True,
)

obs = env.reset()

while True:
    action = np.array([0.1, 0.1], dtype=np.float64)
    observation, reward, done, misc = env.step(action)
    env.render()
    if done:
        obs = env.reset()