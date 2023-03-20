import unittest

from sqlalchemy import select

from model.crud import session
from model.customers import *
from tests import ordered


class TestCustomers(unittest.TestCase):
    customer1 = Customers(
        name='Columbia Outdoor Test Customer',
        phone='360-355-1111',
        addr='123 anywhere lane',
        city='Woodland',
        state='WA',
        zip='98674',
    )

    customer2 = Customers(
        name='Columbia Outdoor Test Customer 2',
        phone='360-355-1111',
        addr='123 anywhere lane',
        city='Woodland',
        state='WA',
        zip='12345',
    )

    @ordered
    def test_add(self):
        s = session()
        s.add(self.customer1)
        s.add(self.customer2)
        s.commit()
        print("After Commit... my new ID is: ", self.customer1.id, self.customer2.id)

    @ordered
    def test_update(self):
        s = session()
        test_name = 'Columbia Outdoor Test Customer'
        statement = select(Customers).filter_by(name=test_name)
        customers = s.scalars(statement).all()
        count = len(customers)
        print(f"I found {count} Customers with name={test_name}, updating...")
        for c in customers:
            c.city = 'Updated'
            s.add(c)
        s.commit()

    @ordered
    def test_del_by_zip(self):
        s = session()
        test_zip = '12345'
        statement = select(Customers).filter_by(zip=test_zip)
        customers = s.scalars(statement).all()
        count = len(customers)
        print(f"I found {count} Customers matching zip={test_zip}, deleting...")
        for c in customers:
            s.delete(c)
        s.commit()

    # This will delete all rows !!! Be Careful
    @ordered
    def test_del_all(self):
        s = session()
        count = s.query(Customers).delete()
        s.commit()
        print(f"Deleted {count} rows from Customers Table!!! ")
