import datetime
import unittest

from model.contractor import Contractor
from model.project_types import ProjectTypes
from model.crud import session
from model.customers import Customers
from model.projects import Projects
from tests import ordered


def get_contractor_id():
    with session() as s:
        contractor = Contractor(business_name='Columbia Outdoor',
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
                                added_date=datetime.datetime.now())
        s.add(contractor)
        s.commit()
        return contractor.id


def get_customer_id():
    with session() as s:
        customer = Customers(
            name='Columbia Outdoor Test Customer',
            phone='360-355-1111',
            addr='123 anywhere lane',
            city='Woodland',
            state='WA',
            zip='98674',
        )
        s.add(customer)
        s.commit()
        return customer.id

def get_project_type_id():
    with session() as s:
        project_type = ProjectTypes(
            name='Deck Project',
            description='Test Deck Project',
            materials='Azek',
        )

        s.add(project_type)
        s.commit()

        return project_type.id

def get_project_id():
    with session() as s:
        project = Projects(
            contractor_id=get_contractor_id(),
            customer_id=get_customer_id(),
            project_type_id=get_project_type_id(),
        )
        s.add(project)
        s.commit()
        return project.id


class TestProjects(unittest.TestCase):
    contractor_id = get_contractor_id()
    customer_id = get_customer_id()

    @ordered
    def test_add(self):
        project_id = get_project_id()
        print(f"After Commit... my new project ID is: {project_id}")

    @ordered
    def test_del_all(self):
        s = session()
        count = s.query(Projects).delete()
        s.commit()
        print(f"Deleted {count} rows from Projects Table!!!")
