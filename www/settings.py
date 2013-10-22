# -*- coding: utf-8 -*-

DEBUG = True

ENGINE = 'elevator_engine_baptiste'

SESSION_TIMEOUT = 3600 # 1 Hour

HASH_KEY = ''
VALIDATE_KEY = ''
ENCRYPT_KEY = ''
SECRET_KEY = ''

DB_USERNAME = ''
DB_PASSWORD = ''
DB_PORT = 1234
DB = ''

def absolute(path):
  import os
  PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
  return os.path.normpath(os.path.join(PROJECT_DIR, path))
