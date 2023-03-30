from .base import Base
from db import db
import datetime

class Attendance(Base):
    professor_id = db.Column(db.Text)
    student_id = db.Column(db.Text)
    class_id = db.Column(db.Text)
    # date_time = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    def __init__(self, pid, sid, cid, date):
      self.professor_id = pid
      self.student_id = sid
      self.class_id = cid



    def __repr__(self):
      return self.name
