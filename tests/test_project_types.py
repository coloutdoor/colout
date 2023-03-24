import unittest

from model.crud import session
from model.project_types import ProjectTypes
from model.projects import Projects
from tests import ordered


def get_project_type_id():
    with session() as s:
        project_type = ProjectTypes(
            name='Construction of a ramp',
            description='Construction of a ramp for wheelchair',
            materials='Cement, steel, etc.',
        )

        s.add(project_type)
        s.commit()

        return project_type.id


class TestProjectTypes(unittest.TestCase):

    @ordered
    def test_add(self):
        project_type_id = get_project_type_id()
        print("After Commit... my new ID is: ", project_type_id)

    # This will delete all rows !!! Be Careful
    @ordered
    def test_del_all(self):
        s = session()
        count = s.query(Projects).delete()
        count = s.query(ProjectTypes).delete()
        s.commit()
        print(f"Deleted {count} rows from ProjectTypes Table!!! ")
