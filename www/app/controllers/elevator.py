# -*- coding: utf-8 -*-

import web

class Elevator(object):
  def GET(self, action):
    params = web.input()
    if action == 'call':
      web.elevator.call(int(params.atFloor),params.to)
    elif action == 'go':
      web.elevator.go(int(params.floorToGo))
    elif action == 'userHasEntered':
      web.elevator.userHasEntered()
    elif action == 'userHasExited':
      web.elevator.userHasExited()
    elif action == 'reset':
        try :
            web.elevator.reset(params.cause)
        except AttributeError:
            web.elevator.reset("")
    elif action == 'nextCommand':
      return web.elevator.getNextCommand()
