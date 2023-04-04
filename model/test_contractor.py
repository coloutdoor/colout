###############################################################################
# python -m unittest test_contractor
# python -m unittest test_contractor.TestContractor
# python -m unittest test_contractor.TestContractor.test_del_all
###############################################################################
from sqlalchemy import select

from model.crud import session
from model.contractor import *
import datetime
import unittest

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

    # This will delete all rows !!! Be Careful
    def test_del_all(self):
        s = session()
        count = s.query(Contractor).delete()
        s.commit()
        print (f"Deleted {count} rows from Contractor Table!!! ")

    def test_add(self):
        s = session()
        s.add(self.contractor)
        s.commit()
        print("After Commit... my new ID is: ", self.contractor.id)

    def test_update(self):
        s=session()
        statement = select(Contractor).filter_by(license_number = 'ABC123')
        conts= s.scalars(statement).all()
        count = len(conts)
        print(f"I found {count} Contractors matching lic ABC123")
        for c in conts:
            c.contact_name = "DDigity Dog"
            s.add(c)
        s.commit()

    def test_del_by_license(self):
        s = session()
        statement = select(Contractor).filter_by(license_number = 'ABC123')
        conts= s.scalars(statement).all()
        count = len(conts)
        print(f"I found {count} Contractors matching lic ABC123")
        for c in conts:
            s.delete(c)
        s.commit()

'''
    def test_del(self):
        current_s = self.s.object_session(self.contractor)
        .delete(self.contractor)
        self.s.commit()
    
    def test_update(self):
        s = session()
        s
'''