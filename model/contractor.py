from sqlalchemy import Column, Integer, String, Date

from model.crud import base


class Contractor(base):
    __tablename__ = 'contractors'
    id = Column(Integer, primary_key=True)
    business_name = Column(String)
    contact_name = Column(String)
    phone = Column(String)
    addr = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    email = Column(String)
    logo = Column(String)
    license_number = Column(String)
    license_state = Column(String)
    added_date = Column(Date)

    def __repr__(self):
        return "<id(business_name='{}', contact_name='{}', phone='{}', email={}, license_number={})>" \
            .format(self.business_name, self.contact_name, self.phone, self.email, self.license_number)
