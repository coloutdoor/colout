from sqlalchemy import Column, Integer, String

from model.crud import base


class ProjectTypes(base):
    __tablename__ = 'project_types'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    materials = Column(String)

    def __repr__(self):
        return "<id(id='{}', name='{}', description='{}', materials={}, units={})>" \
            .format(self.id, self.name, self.description, self.materials, self.units)
