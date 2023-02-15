import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents = []
    for k,v in kwargs.items():
      i = 0
      while i < v :
        self.contents.append(k)
        i += 1
  def draw(self, number):
    if number > len(self.contents):
      return self.contents
      exit()
    drawn_balls=[]
    i = 0
    while i < number:
      draw_index = random.randint(0,len(self.contents)-1)
      drawn_balls.append(self.contents.pop(draw_index))
      i += 1
    return drawn_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  match_count=0
  i = 0
  while i < num_experiments:
    ball_counts = dict()
    drawn_balls = hat.draw(num_balls_drawn)
    if num_balls_drawn < len(hat.contents):
      hat.contents.extend(drawn_balls)
    for ball in drawn_balls:
      ball_counts[ball] = ball_counts.get(ball, 0) + 1
    check_match = all((k in ball_counts and ball_counts[k] >= v) for k,v in expected_balls.items())
    i += 1
    if check_match:
      match_count +=1
    else:
      continue
  probability = match_count/num_experiments
  return probability
