# Generally this will be a non enforced singleton.

class MessageBus(object):

  #multiple functions can map to one endpoint (no return value)
  #only one function can map to a command (has return value)
  def __init__(self):
    self.endpoints = {}
    self.commands = {}


  def request(self, string, *args):
    for endpoint in self.endpoints[string]
      endpoint(args)
  #objects can register handlers for string messages
  #multiple objects can handle the same request
  def register_endpoint(self, string, function):
    if string in self.endpoints
      self.endpoints[string].append(function)
    else
      self.endpoints[string] = [function]

  def unregister_endpoint_item(self, string, function):
    self.endpoints[string].remove(function)

  def unregister_endpoint(self, string, function):
    del self.endpoints[string]


  def command(self, string, *args):
    return self.commands[string](args)

  def register_command(self, string, function):
    self.commands[string] = function

  def unregister_command(self, string):
    del self.commands[string]