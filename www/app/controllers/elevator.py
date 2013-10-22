# -*- coding: utf-8 -*-

import web
from importlib import import_module
from settings import ENGINE
#from app.utils.elevator_engine import ElevatorEngine

ElevatorEngine = import_module('app.utils.' + ENGINE).ElevatorEngine

#Using a global for Elevator engine... meh :(
elevator = ElevatorEngine()

class Elevator(object):
  def GET(self, action):
    params = web.input()
    if action == 'call':
      elevator.call(int(params.atFloor),int(params.to))
    elif action == 'go':
      elevator.go(int(params.floorToGo))
    elif action == 'userHasEntered':
      elevator.userHasEntered()
    elif action == 'userHasExited':
      elevator.userHasExited()
    elif action == 'reset':
        try :
            elevator.reset(params.cause)
        except AttributeError:
            elevator.reset("")
    elif action == 'nextCommand':
      return elevator.getNextCommand()
