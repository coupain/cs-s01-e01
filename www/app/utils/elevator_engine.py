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
    self._currentCommand = ElevatorEngine.ACTION_NOTHING
    self._isBusy = False
    self._waitingList = Queue.Queue()
    self._floorSelected = -1
  
  def call(self, atFloor, to):
    web.debug('call at ' + atFloor + ' to floor ' + to)
    wp = WaitingPerson(atFloor,to)
    self._waitingList.put(wp)
    return
	
  def go(self, floorToGo):
    web.debug('go to floor' + floorToGo')
    self._floorSelected = floorToGo
    return
	
  def userHasEntered(self):
    web.debug('user has entered')
    self._numberOfPassenger += 1
	
  def userHasExited(self):
    web.debug('user has exited')
    self._numberOfPassenger -= 1
	
  def reset(self, message):
    print("Reset, cause = " + message)
    self.__init__()
    
  def getNextCommand(self):
    action = ElevatorEngine.ACTION_NOTHING
    if not self.isBusy and self.waitingList.empty(): #No one in the elevator or waiting for it
      action = ElevatorEngine.ACTION_NOTHING
      
    ###
    elif not self.isBusy and not self.waitingList.empty(): #Elevator empty but someone is waiting
      if self.currentCommand == ElevatorEngine.ACTION_NOTHING or self.currentCommand == ElevatorEngine.ACTION_CLOSE: #Was not doing anything
        personToDeliver = self.waitingList.get()
        #Go to the right floor
        if self.currentFloor < personToDeliver.waitingAtFloor:
          self._currentFloor = personToDeliver.waitingAtFloor
          self._currentCommand = ElevatorEngine.ACTION_UP
          action = ElevatorEngine.ACTION_UP
        elif self.currentFloor > personToDeliver.waitingAtFloor:
          self._currentFloor = personToDeliver.waitingAtFloor
          self._currentCommand = ElevatorEngine.ACTION_DOWN
          action = ElevatorEngine.ACTION_DOWN
        else:
          self._currentCommand = ElevatorEngine.ACTION_OPEN
          action = ElevatorEngine.ACTION_OPEN
    
      elif self.currentCommand == ElevatorEngine.ACTION_UP or self.currentCommand == ElevatorEngine.ACTION_DOWN: #Was going to the right floor
        self._currentCommand = ElevatorEngine.ACTION_OPEN
        action = ElevatorEngine.ACTION_OPEN
      
      elif self.currentCommand == ElevatorEngine.ACTION_OPEN: #Doors where open
        self._isBusy = True #Now the person is in the elevator
        self._currentCommand = ElevatorEngine.ACTION_CLOSE
        action = ElevatorEngine.ACTION_CLOSE
        
    ###   
    elif self.isBusy: #Elevator full
      if (self.currentCommand == ElevatorEngine.ACTION_CLOSE or self.currentCommand == ElevatorEngine.ACTION_NOTHING) and self.floorSelected == -1: #Doors are close, we are waiting the floor selection
        self._currentCommand = ElevatorEngine.ACTION_NOTHING
        action = ElevatorEngine.ACTION_NOTHING
      elif (self.currentCommand == ElevatorEngine.ACTION_CLOSE or self.currentCommand == ElevatorEngine.ACTION_NOTHING) and self.floorSelected != -1: # Floor selected
      
        #Go to the right floor
        if self.currentFloor < self.floorSelected:
          self._currentFloor = self.floorSelected
          self._currentCommand = ElevatorEngine.ACTION_UP
          action = ElevatorEngine.ACTION_UP
        elif self.currentFloor > self.floorSelected:
          self._currentFloor = self.floorSelected
          self._currentCommand = ElevatorEngine.ACTION_DOWN
          action = ElevatorEngine.ACTION_DOWN
        else:
          self._currentCommand = ElevatorEngine.ACTION_OPEN
          action = ElevatorEngine.ACTION_OPEN
          
      elif self.currentCommand == ElevatorEngine.ACTION_UP or self.currentCommand == ElevatorEngine.ACTION_DOWN: #Was going to the right floor
        self._currentCommand = ElevatorEngine.ACTION_OPEN
        action = ElevatorEngine.ACTION_OPEN
      
      elif self.currentCommand == ElevatorEngine.ACTION_NOTHING: #Doors are open, the person is gone
        self._currentCommand = ElevatorEngine.ACTION_NOTHING
        self._isBusy = False
        action = ElevatorEngine.ACTION_NOTHING
        
    web.debug('action: ' + action)
    return action
    
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
    
  @property
  def floorSelected(self):
    return self._floorSelected
    