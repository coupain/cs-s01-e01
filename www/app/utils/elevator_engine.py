# -*- coding: utf-8 -*-

import Queue
from app.utils.waiting_person import WaitingPerson

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
    self._currentCommand = ACTION_NOTHING
    self._isBusy = False
    self._waitingList = Queue.Queue()
  
  def call(self, atFloor, to):
    if self.isBusy:
      wp = WaitingPerson(atFloor,to)
      self._waitingList.put(wp)
      print(self.waitingList.qsize())
    else:
      self._isBusy = True
    return
	
  def go(self, floorToGo):
    return
	
  def userHasEntered(self):
    self._numberOfPassenger += 1
	
  def userHasExited(self):
    self._numberOfPassenger -= 1
	
  def reset(self, message):
    print("Reset, cause = " + message)
    self.__init__()
    
  def getNextCommand(self):
   
      
    
  @property
  def currentFloor(self):
    return self._currentFloor
    
  @property
  def numberOfPassenger(self):
    return self._numberOfPassenger
  
  @property
  def doorOpen(self):
    return self._doorOpen
    
  @property
  def isBusy(self):
    return self._isBusy
    
  @property
  def waitingList(self):
    return self._waitingList
    
  @property
  def currentCommand(self):
    return self._currentCommand