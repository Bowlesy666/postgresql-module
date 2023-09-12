from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# setting up tables before setting up files but after base is declared

# create a class-based model for the "Artist" table
class ArtistTable(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class AlbumTable(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class TrackTable(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)

#  setting up the files

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
# capital S in session var
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declerative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")
