from sqlalchemy import Column, Integer, String, ForeignKey

from model.crud import base

class SubProjectTypes(base):
    __tablename__ = 'subproject_types'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    materials = Column(String)
    units = Column(String)        # Sq Ft, Ln Ft, ...
    project_type_id = Column(Integer, ForeignKey('project_types.id', onupdate='SET NULL', ondelete='SET NULL'),
                           nullable=False)

    def __repr__(self):
        return "<id(id='{}', name='{}', description='{}', materials={}, units={})>" \
            .format(self.id, self.name, self.description, self.materials, self.units)
