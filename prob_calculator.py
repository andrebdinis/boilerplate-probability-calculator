import copy
import random
# Consider using the modules imported above.


# OBJECTIVE: Write a program to determine the approximate probability of drawing certain balls randomly from a hat.


class Hat:
  contents = list()

  def __init__(self, **kwargs):
    self.contents = []
    for color,numBalls in kwargs.items():
      for ball in range(numBalls):
        self.contents.append(color)

  # draw a number of balls from the hat
  def draw(self, nBallsToDraw):
    if nBallsToDraw > len(self.contents): return self.contents
    sample = random.sample(self.contents, k=nBallsToDraw)
    for drawnBall in sample:
      self.contents.remove(drawnBall)
    return sample


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for experiment in range(num_experiments):
    hatObj = copy.deepcopy(hat)
    match = False
    draw = hatObj.draw(num_balls_drawn)
    for color,numBalls in expected_balls.items():
      if draw.count(color) >= numBalls: match = True; continue
      match = False; break
    if match: count += 1;
  return (count / num_experiments)