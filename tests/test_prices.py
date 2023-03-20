import unittest

from model.crud import session
from model.prices import Prices
from tests import ordered
from tests.test_contractor import get_contractor_id
from tests.test_project_types import get_project_type_id


class TestPrices(unittest.TestCase):

    @ordered
    def test_add(self):
        s = session()
        contractor_id = get_contractor_id()
        project_type_id = get_project_type_id()
        prices = Prices(
            contractor_id=contractor_id,
            project_type_id=project_type_id,
            price_per_unit="25"
        )

        s.add(prices)
        s.commit()
        print("After Commit... my new ID is: ", prices.id)

    # This will delete all rows !!! Be Careful
    @ordered
    def test_del_all(self):
        s = session()
        count = s.query(Prices).delete()
        s.commit()
        print(f"Deleted {count} rows from Prices Table!!! ")
