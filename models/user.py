from flask_login import UserMixin

from .base import Base
from db import db
import json

class User(UserMixin, Base):
    name = db.Column(db.String(128))
    password = db.Column(db.String(100))
    class_ids = db.Column(db.Text)
    role = db.Column(db.String(10)) # professor | student

    def __init__(self, name, password, role):
      self.name = name
      self.class_ids = json.dumps({"ids":[]})
      self.password = password
      self.role = role

    def update(self, name, role, class_ids):
      self.name = name
      self.role = role
      self.class_ids = class_ids


    def __repr__(self):
      return self.name
