import unittest

from model.crud import session
from model.subprojects import SubProjects
from tests import ordered
from tests.test_projects import get_project_id


def get_sub_project_id():
    with session() as s:
        project_id = get_project_id()

        subproject = SubProjects(
            project_id=project_id,
            name="Sub Project 1",
            length=100,
            height=100,
            width=100,
            project_type="Construction"
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
