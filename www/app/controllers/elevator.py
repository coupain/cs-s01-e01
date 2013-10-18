# -*- coding: utf-8 -*-

import web

class Elevator(object):
  def GET(self, action):
    params = web.input()
    if action == 'call':
	  return
    elif action == 'go':
      return 'go'
    elif action == 'userHasEntered':
	  return
    elif action == 'userHasExited':
	  return
    elif action == 'reset':
	  return
    elif action == 'nextCommand':
	  return
	
