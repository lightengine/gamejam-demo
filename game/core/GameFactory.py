# This object is a "singleton" it is not enforced but logically you only need one factory.
# Responsibilities of this class
"""
  Build the dependency tree for the game.
"""
from game.factories.PlayerFactory import *

class GameFactory(object):
  
  def build(self, file)
    #read from the level.xml file eventually
    #build game objects based on file
    new PlayerFactory.build(file)