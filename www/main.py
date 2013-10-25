#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import settings
from urls import URLS
from importlib import import_module

web.config.debug = settings.DEBUG

app = web.application(URLS, globals(), autoreload=settings.DEBUG)

if __name__ == '__main__':
  ElevatorEngine = import_module('app.utils.' + settings.ENGINE).ElevatorEngine
  web.elevator = ElevatorEngine()
  app.run()