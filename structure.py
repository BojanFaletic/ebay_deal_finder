class structure:
  min_ = -1
  max_ = -1
  mean_ = -1

  def __init__(self, mean, max_,min_):
    self.min = min_
    self.max_ = max_
    self.mean_ = mean
  
  def minimal(self):
    return self.min_

  def maximal(self):
    return self.max_

  def medium(self):
    return self.mean_



