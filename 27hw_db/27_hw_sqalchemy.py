from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///27datab_alchemy.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    producer = Column(String)

    def __repr__(self):
        return f'<User(id={self.id}, title={self.title}, year={self.year}, producer={self.producer})>'


Base.metadata.create_all(engine)
#
# new_film = Movie(title='Barbie', year=2023, producer='David Heyman')
# session.add(new_film)

# new_2 = Movie(title='The Forgotten', year=2004, producer='Bruce Cohen')
# session.add(new_2)

# new_3 = Movie(title='The Beekeeper', year=2024, producer='David Ayer')
# session.add(new_3)
#
# new_4 = Movie(title='Wrath of Man', year=2021, producer='Ivan Atkinson')
# session.add(new_4)
#
# new_5 = Movie(title='One Shot', year=2021, producer='Sarah Gabriel')
# session.add(new_5)

# new_6 = Movie(title='Another Man', year=2022, producer='Ivan Atkinson')
# session.add(new_6)

res = session.query(Movie).all()
myres = session.query(Movie).filter_by(producer='Ivan Atkinson').all()
# print(myres)


year_barb_to_update = session.query(Movie).filter_by(title='Barbie').first()
year_barb_to_update.year = 2024
# session.commit()

updated_barb = session.query(Movie).filter_by(title='Barbie').first()
# print(updated_barb)


film_3_to_delete = session.query(Movie).filter_by(title='The Beekeeper').all()
for info in film_3_to_delete:
    session.delete(info)
session.commit()

results = session.query(Movie).all()
print('All: ', results)


# session.commit()