import random

class Agent:
	def chooseAction(self, observations, possibleActions):
		return ('straight', 'coast')	
class RuleAgent:
    def __init__(self):
        self.max_velocity = 0.8

    def chooseAction(self, obs):
        lidar = obs['lidar']
        velocity = obs['velocity']

        front = lidar[2]  # center
        left = lidar[0]   # far left
        right = lidar[4]  # far right

        if front > 0.8:
            direction = 'straight'
        elif left > right:
            direction = 'left'
        else:
            direction = 'right'

        if front < 0.3:
            speed = 'brake'
        elif velocity < self.max_velocity and front > 0.5:
            speed = 'accelerate'
        else:
            speed = 'coast'

        return (direction, speed)
