from sqlalchemy import Table, Column, Integer, Date, MetaData, create_engine, VARCHAR, Double, ForeignKey, text
from sqlalchemy.orm import sessionmaker

from model.config import DATABASE_URI

########################################################################################
# Dev Env
#
#  psql -h $DBSERVER -U $DBUSER -d $DB -p 5432
# export DBSERVER="localhost"
# export DBUSER="postgres"
# export DB="colout"
# export DBPASS="colout"
########################################################################################

def create_database(engine):
    meta = MetaData()

    contractors = Table(
        'contractors', meta,
        Column('id', Integer, primary_key=True),
        Column('business_name', VARCHAR(255, collation='default')),
        Column('contact_name', VARCHAR(255, collation='default')),
        Column('phone', VARCHAR(255, collation='default')),
        Column('addr', VARCHAR(255, collation='default')),
        Column('city', VARCHAR(255, collation='default')),
        Column('state', VARCHAR(255, collation='default')),
        Column('zip', VARCHAR(255, collation='default')),
        Column('email', VARCHAR(255, collation='default')),
        Column('logo', VARCHAR(255, collation='default')),
        Column('license_number', VARCHAR(255, collation='default')),
        Column('license_state', VARCHAR(255, collation='default')),
        Column('added_date', Date),
    )

    customers = Table(
        'customers', meta,
        Column('id', Integer, primary_key=True),
        Column('name', VARCHAR(255, collation='default')),
        Column('phone', VARCHAR(255, collation='default')),
        Column('addr', VARCHAR(255, collation='default')),
        Column('city', VARCHAR(255, collation='default')),
        Column('state', VARCHAR(255, collation='default')),
        Column('zip', VARCHAR(255, collation='default')),
        Column('email', VARCHAR(255, collation='default')),
    )

    estimates = Table(
        'estimates', meta,
        Column('id', Integer, primary_key=True),
        Column('project_id', ForeignKey("projects.id", ondelete='NO ACTION', onupdate='NO ACTION')),
        Column('date', Date),
        Column('location', VARCHAR(255, collation='default')),
    )

    prices = Table(
        'prices', meta,
        Column('id', Integer, primary_key=True),
        Column('contractor_id', ForeignKey("contractors.id", ondelete='NO ACTION', onupdate='NO ACTION')),
        Column('project_type_id', ForeignKey("project_types.id", ondelete='NO ACTION', onupdate='NO ACTION')),
        Column('price_per_unit', VARCHAR(255, collation='default')),
    )

    project_types = Table(
        'project_types', meta,
        Column('id', Integer, primary_key=True),
        Column('name', VARCHAR(255, collation='default')),
        Column('description', VARCHAR(255, collation='default')),
        Column('materials', VARCHAR(255, collation='default')),
        Column('units', VARCHAR(255, collation='default')),
    )

    projects = Table(
        'projects', meta,
        Column('id', Integer, primary_key=True),
        Column('contractor_id', ForeignKey("contractors.id", ondelete='NO ACTION', onupdate='NO ACTION')),
        Column('customer_id', ForeignKey("customers.id", ondelete='NO ACTION', onupdate='NO ACTION')),
        Column('description', VARCHAR(255, collation='default')),
    )

    subprojects = Table(
        'subprojects', meta,
        Column('id', Integer, primary_key=True),
        Column('name', VARCHAR(255, collation='default')),
        Column('project_id', ForeignKey("projects.id", ondelete='NO ACTION', onupdate='NO ACTION')),
        Column('length', Double),
        Column('width', Double),
        Column('height', Double),
        Column('project_type', VARCHAR(255, collation='default')),
    )

    meta.create_all(engine)


def drop_database(session):
    session.execute(text("DROP TABLE IF EXISTS "
                         "contractors, customers, estimates, prices, project_types, projects, subprojects CASCADE;"))
    session.commit()
    session.close()


def recreate_database():
    engine = create_engine(DATABASE_URI, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    drop_database(session)

    create_database(engine)


if __name__ == '__main__':
    recreate_database()
