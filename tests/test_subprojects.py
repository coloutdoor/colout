import unittest

from model.crud import session
from model.subprojects import SubProjects
from model.subproject_types import SubProjectTypes
from tests import ordered
from tests.test_projects import get_project_id

def get_subproject_type_id():
    with session() as s:

        subproject_type = SubProjectTypes(
            name="Deck Framing Test",
            description="Frame with premium pressure treated lumber",
            materials="PT",
            units = "Sq Ft",
        )
        s.add(subproject_type)
        s.commit()

        return subproject_type.id


def get_sub_project_id():
    with session() as s:
        project_id = get_project_id()
        subproject_type_id = get_subproject_type_id()
        subproject = SubProjects(
            project_id=project_id,
            name="Sub Project 1",
            length=100,
            height=100,
            width=100,
            subproject_type_id=subproject_type_id
        )

        s.add(subproject)
        s.commit()

        return subproject.id


class TestSubProjects(unittest.TestCase):
    @ordered
    def test_add(self):
        subproject_id = get_sub_project_id()
        print("After Commit... my new ID is: ", subproject_id)

    # This will delete all rows !!! Be Careful
    @ordered
    def test_del_all(self):
        s = session()
        count = s.query(SubProjects).delete()
        s.commit()
        print(f"Deleted {count} rows from subprojects Table!!! ")
