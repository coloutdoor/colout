### contractor.py ###

from sqlalchemy import Column, Integer, String, Date
from crud import session, base
import datetime
import unittest

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
    license_state= Column(String)
    added_date = Column(Date)
    
    def __repr__(self):
        return "<id(businss_name='{}', contact_name='{}', phone='{}', email={}, license_number={})>"\
                .format(self.business_name, self.contact_name, self.phone, self.email, self.license_number)

# python -m unittest test_module1 test_module2
# python -m unittest test_module.TestClass
# python -m unittest test_module.TestClass.test_method    
###############################################################################
## 
class TestContractor(unittest.TestCase):
    
    contractor = Contractor(
        business_name = 'Columbia Outdoor',
        contact_name = 'DDog',
        phone = '360-355-1111',
        addr = '123 anywhere lane',
        city = 'Woodland',
        state = 'WA',
        zip = '98674',
        email = 'bob@columbiaoutdoor.com',
        logo = '/path/to/logo',
        license_number = 'ABC123',
        license_state= 'WA',
        added_date = datetime.datetime.now()
    )

    def test_del_all(self):
        self.s = session()
        count = self.s.query(Contractor).delete()
        self.s.commit()
        print (f"Deleted {count} rows from Contractor Table!!! ")

    def test_add(self):
        self.s.add(self.contractor)
        print("My new ID is: ", self.contractor.id)
        self.s.commit()
        print("After Commit... my new ID is: ", self.contractor.id)

'''
    def test_del(self):
        current_s = self.s.object_session(self.contractor)
        .delete(self.contractor)
        self.s.commit()
    
    def test_update(self):
        s = session()
        s
'''

