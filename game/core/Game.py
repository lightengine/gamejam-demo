class Game(object):
  def __init__(self, factory, entities, message_bus):
    self.factory = factory
    self.entities = entities

    ## setup the game state
    factory.buildPlayer

  def update(delta_t):
    for e in self.entities:
      e.update(delta_t)