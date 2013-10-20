#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from settings import DEBUG
from urls import URLS

web.config.debug = DEBUG

app = web.application(URLS, globals(), autoreload=DEBUG)

if __name__ == '__main__':
  app.run()
