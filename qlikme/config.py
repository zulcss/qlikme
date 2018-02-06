import os
import logging

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('/', 'app.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join('/', 'db_repository')

LOG_FILE = os.getenv('LOG_FILE', None)
LOG_LEVEL = getattr(logging, os.getenv("LOG_LEVEL", "debug").upper())
