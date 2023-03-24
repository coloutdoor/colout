import datetime
import unittest
import os
import sys

from sqlalchemy import select

# getting the name of the directory
# where the this model dir is present.
# model_dir = os.path.dirname(os.path.realpath("../model"))
# sys.path.append(model_dir)

from model.contractor import Contractor
from model.projects import Projects
from model.crud import session
from tests import ordered

def get_contractor_id(business_name='Columbia Outdoor'):
    with session() as s:
        contractor = Contractor(
            business_name=business_name,
            contact_name='DDog',
            phone='360-355-1111',
            addr='123 anywhere lane',
            city='Woodland',
            state='WA',
            zip='98674',
            email='bob@columbiaoutdoor.com',
            logo='/path/to/logo',
            license_number='ABC123',
            license_state='WA',
            added_date=datetime.datetime.now()
        )
        s.add(contractor)
        s.commit()

        return contractor.id


class TestContractor(unittest.TestCase):

    @ordered
    def test_add(self):
        contractor_id_1 = get_contractor_id()
        contractor_id_2 = get_contractor_id(business_name='Columbia Outdoor 2')
        print(f"After Commit... my new IDs are: {', '.join(map(str, (contractor_id_1, contractor_id_2)))}")

    @ordered
    def test_update(self):
        s = session()
        test_license = 'ABC123'
        statement = select(Contractor).filter_by(license_number=test_license)
        contractors = s.scalars(statement).all()
        count = len(contractors)
        print(f"I found {count} Contractors matching lic {test_license}, updating")
        for c in contractors:
            c.contact_name = "DDigity Dog"
            s.add(c)
        s.commit()

    @ordered
    def test_del_by_license(self):
        s = session()
        test_license = 'ABC123_DELETE'
        statement = select(Contractor).filter_by(license_number=test_license)
        contractors = s.scalars(statement).all()
        count = len(contractors)
        print(f"I found {count} Contractors matching lic {test_license}, deleting...")
        for c in contractors:
            s.delete(c)
        s.commit()

    # This will delete all rows !!! Be Careful
    @ordered
    def test_del_all(self):
        s = session()
        count = s.query(Projects).delete()
        count = s.query(Contractor).delete()
        s.commit()
        print(f"Deleted {count} rows from Contractor Table!!! ")
