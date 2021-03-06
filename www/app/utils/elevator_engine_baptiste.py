# -*- coding: utf-8 -*-

import Queue
import web
from app.utils.waiting_person import WaitingPerson

class ElevatorEngine:
  ACTION_NOTHING = "NOTHING"
  ACTION_OPEN = "OPEN"
  ACTION_CLOSE = "CLOSE"
  ACTION_UP = "UP"
  ACTION_DOWN = "DOWN"
  
  DIRECTION_NONE = None 
  DIRECTION_UP = "UP"
  DIRECTION_DOWN = "DOWN"
  
  FLOOR_MAX = 5

  def __init__(self):
    self._currentDirection = ElevatorEngine.DIRECTION_UP
    self._commands = Queue.Queue() #FIFO
    self._stopsUp = set() #Store all stop that the elevator must do while going UP
    self._stopsDown = set() #Store all stop that the elevator must do while going DOWN
    self._stops = set() #Store stops that must be done no matter the direction
    self._currentFloor = 0
    self._doorsClosed = True
    self._actions = Queue.Queue() # Store all actions to do
    self._numberOfPassenger = 0
  
  def call(self, atFloor, to):
    web.debug("call at %d to %s" % (atFloor, to))
    self._handleCall(atFloor, to)
    return
	
  def go(self, floorToGo):
    web.debug("user want to go to %d" % (floorToGo))
    #FIXME: handle when floorToGo == currentFloor
    self._handleCall(floorToGo, ElevatorEngine.DIRECTION_NONE)
    return

  """Counting the number of stop in the given direction"""
  def _numberOfStopsInDirection(self, direction):
    if direction == ElevatorEngine.DIRECTION_UP:
      intersect = self._stopsUp.union(self._stops).intersection(range(self._currentFloor, ElevatorEngine.FLOOR_MAX+1, 1))
    elif direction == ElevatorEngine.DIRECTION_DOWN: 
      intersect = self._stopsDown.union(self._stops).intersection(range(self._currentFloor, 0-1, -1))
    else:
      ##FIXME: maybe another choice ?
      return False
      
    return len(intersect)
      
  def _openDoors(self):
    if self._doorsClosed == True:
      self._actions.put(ElevatorEngine.ACTION_OPEN)
    self._handleStop(self._currentFloor) #Removing this floor from the lists
    self._doorsClosed = False
    
  def _closeDoors(self):
    if self._doorsClosed == False:
      self._actions.put(ElevatorEngine.ACTION_CLOSE)
      self._doorsClosed = True
      
  """Adding the floors where to stop in the lists"""
  def _addStop(self, floor, direction):
    web.debug("Adding stop to %d in direction %s" % (floor, direction))
    
    #If floor is top or bottom, no matter the direction
    if floor == ElevatorEngine.FLOOR_MAX or floor == 0:
      direction = ElevatorEngine.DIRECTION_NONE
    
    if direction == ElevatorEngine.DIRECTION_UP:
      self._stopsUp.add(floor)
    elif direction == ElevatorEngine.DIRECTION_DOWN:
      self._stopsDown.add(floor)
    else:
      self._stops.add(floor)
    
  """Remove the given floor from all stops lists"""
  def _handleStop(self, floor):
    if self._currentFloor in self._stopsUp:
      self._stopsUp.remove(floor)
    if self._currentFloor in self._stopsDown:
      self._stopsDown.remove(floor)
    if self._currentFloor in self._stops:
      self._stops.remove(floor)
    
  def _handleCall(self, floor, direction):
    if floor == self._currentFloor:
      if self._doorsClosed == True:
        self._openDoors()
    else:
      self._addStop(floor, direction)
    
  def _goUp(self):
    self._closeDoors()
    self._currentDirection = ElevatorEngine.DIRECTION_UP 
    self._actions.put(ElevatorEngine.ACTION_UP)
    self._currentFloor += 1
    
  def _goDown(self):
    self._closeDoors()
    self._currentDirection = ElevatorEngine.DIRECTION_DOWN
    self._actions.put(ElevatorEngine.ACTION_DOWN)
    self._currentFloor -= 1
	
  def userHasEntered(self):
    web.debug('user has entered')
    self._numberOfPassenger += 1
	
  def userHasExited(self):
    web.debug('user has exited')
    self._numberOfPassenger -= 1
	
  def reset(self, message):
    print("Reset, cause = " + message)
    self.__init__()
    
  def _reverseCurrentDirection(self):
    return self._reverseDirection(self._currentDirection)
    
  def _reverseDirection(self, direction):
    return ElevatorEngine.DIRECTION_UP if direction == ElevatorEngine.DIRECTION_DOWN else ElevatorEngine.DIRECTION_DOWN  
    
  def _goToReverseDirection(self, direction):
    self._goToDirection(self._reverseDirection(self._currentDirection))
    
  def _goToCurrentReverseDirection(self):
    self._goToReverseDirection(self._currentDirection)
      
  def _goToCurrentDirection(self):
    self._goToDirection(self._currentDirection)
      
  def _goToDirection(self, direction):
    if direction == ElevatorEngine.DIRECTION_UP:
      self._goUp()
    elif direction == ElevatorEngine.DIRECTION_DOWN:
      self._goDown()
    else:
      self._goUp()
    
  def getNextCommand(self):
    web.debug("current floor %d" % self._currentFloor)
    web.debug("stops up:" + " - ".join(str(s) for s in self._stopsUp))
    web.debug("stops down:" + " - ".join(str(s) for s in self._stopsDown))
    web.debug("stops:" + " - ".join(str(s) for s in self._stopsDown))
    #if the current floor is in the stops no matter the firection
    if self._currentFloor in self._stops:
      self._openDoors()
    #checking the stops when going up
    elif self._currentDirection == ElevatorEngine.DIRECTION_UP and self._currentFloor in self._stopsUp:
      self._openDoors()
    #checking the stops when going down
    elif self._currentDirection == ElevatorEngine.DIRECTION_DOWN and self._currentFloor in self._stopsDown:
      self._openDoors()
    #checking in the current direction (to avoid going up/down everytime)
    elif self._numberOfStopsInDirection(self._currentDirection) != 0:
      self._goToCurrentDirection()
    #checking the other direction
    elif self._numberOfStopsInDirection(self._reverseCurrentDirection()) != 0:
      self._goToCurrentReverseDirection()
      
    ##Doing the action
    if self._actions.empty():
      action = ElevatorEngine.ACTION_NOTHING
    else:
      action = self._actions.get()
    web.debug("action: %s" % (action))
    return action