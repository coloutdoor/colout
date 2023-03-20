from sqlalchemy import Column, Integer, String, ForeignKey, Double

from model.crud import base


class SubProjects(base):
    __tablename__ = 'subprojects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    length = Column(Double)
    width = Column(Double)
    height = Column(Double)
    project_type = Column(String)

    def __repr__(self):
        return "<id(id='{}', name='{}', project_id='{}', length={}, width={}, height={}, project_type={})>" \
            .format(self.id, self.name, self.project_id, self.length, self.width, self.height, self.project_type)
