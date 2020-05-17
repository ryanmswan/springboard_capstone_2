from sqlalchemy import create_engine, Table, Column
from sqlalchemy import Integer, String, Text, MetaData

engine = create_engine('sqlite:///lyrics.db', echo=False)

meta = MetaData()

artists = Table('artists', meta,
                Column('artist', String, primary_key=True),
                Column('artist_url', String))

lyrics = Table('lyrics', meta,
               Column('artist', String),
               Column('song_title', String),
               Column('year', Integer),
               Column('song_url', String, primary_key=True),
               Column('lyrics', Text))

genres = Table('genre', meta,
               Column('id', Integer, primary_key=True, autoincrement=True),
               Column('song_url', String),
               Column('genre', String))

styles = Table('style', meta,
               Column('id', Integer, primary_key=True, autoincrement=True),
               Column('song_url', String),
               Column('style', String))

if __name__ == '__main__':
    meta.create_all(engine)
