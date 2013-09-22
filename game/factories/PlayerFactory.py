class PlayerFactory(object):
  def __init__(self, message_bus):
    self.message_bus = message_bus

  def build(self, playerXML)