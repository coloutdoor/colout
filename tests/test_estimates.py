import datetime
import unittest

from model.crud import session
from model.estimates import *
from tests import ordered
from tests.test_projects import get_project_id


class TestEstimates(unittest.TestCase):

    @ordered
    def test_add(self):
        s = session()
        estimate = Estimates(
            project_id=get_project_id(),
            location='123 anywhere lane',
            date=datetime.datetime.now()
        )
        s.add(estimate)
        s.commit()
        print("After Commit... my new ID is: ", estimate.id)

    # This will delete all rows !!! Be Careful
    @ordered
    def test_del_all(self):
        s = session()
        count = s.query(Estimates).delete()
        s.commit()
        print(f"Deleted {count} rows from Estimates Table!!! ")
