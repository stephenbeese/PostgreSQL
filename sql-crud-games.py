from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Games(base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    release_date = Column(String)
    console = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# create new instances of games

tetris = Games(
    name="Tetris",
    release_date="November 1989",
    console="NES"
)

super_mario_bros = Games(
    name="Super Mario Bros.",
    release_date="13th September 1985",
    console="NES"
)

# Update "Games" table
# session.add(tetris)
# session.add(super_mario_bros)


# commit the session
# session.commit()

# print table
games = session.query(Games)
for game in games:
    print(
     game.id,
     game.name,
     game.release_date,
     game.console,
     sep=" | "
    )
