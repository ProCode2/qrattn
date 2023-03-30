from .base import Base
from db import db

class Class(Base):
    name = db.Column(db.String(128))

    def __init__(self, name):
      self.name = name

    def __repr__(self):
      return self.name
