# -*- coding: utf-8 -*-

from app.controllers.index import Index
from app.controllers.elevator import Elevator

URLS = (
  r'^/', Index,
  r'^/(call|go|userHasEntered|userHasExited|reset|nextCommand)', Elevator,
)
