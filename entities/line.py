from lib.entity import Entity
from lib.point import *
import math

class Line(Entity):
  def __init__(self):
    super(Line, self).__init__()
    for i in xrange(-100,100,5):
      self.points.append(Point(i,0))
