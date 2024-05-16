# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:08:11 2024

@author: clfel
"""

import random

class Agent:
    def __init__(self, world):
        self.world = world
        self.location = None

    def move(self):
        empty_patch = self.world.find_empty_patch()
        if empty_patch:
            if self.location:
                self.world.grid[self.location] = None  # Leave current location
            self.location = empty_patch
            self.world.grid[self.location] = self

class World:
    def __init__(self, size, num_agents):
        assert(size[0] * size[1] > num_agents), 'Grid too small for number of agents.'
        self.size = size
        self.grid = {(x, y): None for x in range(size[0]) for y in range(size[1])}
        self.agents = [Agent(self) for _ in range(num_agents)]
        self.init_world()

    def init_world(self):
        for agent in self.agents:
            empty_patch = self.find_empty_patch()
            if empty_patch:
                agent.location = empty_patch
                self.grid[empty_patch] = agent

    def find_empty_patch(self):
        empty_patches = [loc for loc, occupant in self.grid.items() if occupant is None]
        return random.choice(empty_patches) if empty_patches else None

    def run(self, max_iter):
        for _ in range(max_iter):
            for agent in self.agents:
                agent.move()
            self.print_grid()

    def print_grid(self):
        for y in range(self.size[1]):
            row = ''
            for x in range(self.size[0]):
                row += 'A ' if self.grid[(x, y)] else '. '
            print(row)
        print()

# Parameters
world_size = (5, 5)
num_agents = 5
max_iterations = 10

# Create and run the world
world = World(world_size, num_agents)
world.run(max_iterations)

#https://github.com/ClaudiaFA/Lab9b/blob/main/Lab9b.py
