from sqlalchemy import Column, Integer, String

from model.crud import base


class Customers(base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    addr = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)

    def __repr__(self):
        return "<id(id='{}', name='{}', phone='{}', addr='{}', city='{}', state='{}', zip='{}')>"\
            .format(self.id, self.name, self.phone, self.addr, self.city, self.state, self.zip)
