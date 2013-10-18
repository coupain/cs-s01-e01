#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The only file which is directly executed. There's no reason to modify this
file.
"""

import web
from settings import DEBUG
from urls import URLS

web.config.debug = DEBUG

app = web.application(URLS, globals(), autoreload=False)


if __name__ == '__main__':
  app.run()
