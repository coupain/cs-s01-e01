# -*- coding: utf-8 -*-

class ElevatorEngine:
  ACTION_NOTHING = "NOTHING"
  ACTION_OPEN = "OPEN"
  ACTION_CLOSE = "CLOSE"
  ACTION_UP = "UP"
  ACTION_DOWN = "DOWN"

  def __init__(self):
    self._currentFloor = 0
    self._doorOpen = False
    self._numberOfPassenger = 0
  
  def call(self, atFloor, to):
    return
	
  def go(self, floorToGo):
    return
	
  def userHasEntered(self):
    self._numberOfPassenger += 1
	
  def userHasExited(self):
    self._numberOfPassenger -= 1
	
  def reset(self, message):
    self.__init__()
    
  @property
  def currentFloor(self):
    return self._currentFloor
    
  @property
  def numberOfPassenger(self):
    return self._numberOfPassenger
  
  @property
  def doorOpen(self):
    return self._doorOpen