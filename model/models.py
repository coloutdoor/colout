### models.py ###
from sqlalchemy import Column, Integer, String, Date
from crud import engine, session, base
import datetime
from contractor import Contractor

class Book(base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)
    
    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>"\
                .format(self.title, self.author, self.pages, self.published)

## Recreate the database - DELETE ALL
def recreate_database():
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
    print ("******* This needs some work!! DATABASE MAY BE RECREATED *****************")
    

book = Book(
    title='Deep Learning',
    author='Ian Goodfellow',
    pages=775,
    published=datetime.date(2016, 11, 18)
)

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

### START ################
recreate_database()
s = session()

##
s.add(book)
s.add(contractor)
s.commit()

# print ("Book is added!")

firstBook = s.query(Book).first()
print("The Author's name is: ", firstBook.author)

firstContractor = s.query(Contractor).first()
print("The Contractor's is: ", firstContractor.business_name)

## Close when complete
s.close()
