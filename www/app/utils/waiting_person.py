# -*- coding: utf-8 -*-

class WaitingPerson:
  
  def __init__(self, waitingAtFloor, direction):
    self._waitingAtFloor = waitingAtFloor
    self._direction = direction
  
  
  @property
  def waitingAtFloor(self):
    return self._waitingAtFloor
    
  @property
  def direction(self):
    return self._direction