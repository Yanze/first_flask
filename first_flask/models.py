from datetime import datetime

class Message():
  def __init__(self, text):
    self.text = text
    self.date = datetime.utcnow()
