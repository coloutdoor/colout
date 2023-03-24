from sqlalchemy import Column, Integer, ForeignKey, String

from model.crud import base


class Projects(base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    contractor_id = Column(Integer, ForeignKey('contractors.id', onupdate='SET NULL', ondelete='SET NULL'),
                           nullable=False)
    project_type_id = Column(Integer, ForeignKey('project_types.id', onupdate='SET NULL', ondelete='SET NULL'),
                           nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id', onupdate='SET NULL', ondelete='SET NULL'),
                         nullable=False)
    description = Column(String)

    def __repr__(self):
        return "<id(id='{}', contractor_id='{}', customer_id='{}')>" \
            .format(self.id, self.contractor_id, self.customer_id)
