from sqlalchemy import Column, Integer, String, Date, ForeignKey
from model.crud import base


class Estimates(base):
    __tablename__ = 'estimates'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    location = Column(String)
    date = Column(Date)

    def __repr__(self):
        return "<id(estimate id='{}', project_id='{}', location='{}', date={})>" \
            .format(self.id, self.project_id, self.location, self.date)
