from sqlalchemy import Column, Integer, String, ForeignKey

from model.crud import base


class Prices(base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    contractor_id = Column(Integer, ForeignKey('contractors.id'), nullable=False)
    subproject_type_id = Column(Integer, ForeignKey('subproject_types.id'), nullable=False)
    price_per_unit = Column(String)

    def __repr__(self):
        return "<id(id='{}', contractor_id='{}', project_type_id='{}', price_per_unit={})>" \
            .format(self.id, self.contractor_id, self.project_type_id, self.price_per_unit)
