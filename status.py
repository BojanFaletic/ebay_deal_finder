SUCCESS = True
FAILURE = False

class result:
  t_names = []
  itm = []
  def __init__(self):
    self.itm.clear()

  def append(self, name_of_item, price_of_item, value_of_item):
    tmp = self.t_names.copy()

    tmp.append(name_of_item)
    tmp.append(price_of_item)
    tmp.append(value_of_item)
  
    self.itm.append(tmp)

  def status(self):
    return self.itm