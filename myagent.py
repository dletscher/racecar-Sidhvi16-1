class Agent:
    def __init__(self):
        self.last_steer = 0.0  # steering value between -1 and 1

    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        left, fleft, front, fright, right = lidar

        left_sum = left + fleft
        right_sum = right + fright
        diff = right_sum - left_sum

        # Reduced proportional gain for gentler steering
        Kp = 1.0
        steer = max(min(Kp * diff, 1.0), -1.0)

        # More smoothing
        alpha = 0.85
        steer = alpha * self.last_steer + (1 - alpha) * steer
        self.last_steer = steer

        # Direction based on smoothed steer
        if steer > 0.4:
            direction = 'right'
        elif steer < -0.4:
            direction = 'left'
        else:
            direction = 'straight'

        # Slow down before tight turns or obstacles
        min_clearance = min(front, fleft, fright)

        if min_clearance < 0.5 or abs(steer) > 0.6:
            speed = 'brake'
        elif velocity < 3.8 and front > 0.7:
            speed = 'accelerate'
        else:
            speed = 'coast'

        print(f"DEBUG: LIDAR={lidar}, Vel={velocity:.2f}, Steer={steer:.2f}, Dir={direction}, Speed={speed}")
        return (direction, speed)
