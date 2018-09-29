from sqlalchemy import (
    Table, Text, Integer, VARCHAR, MetaData, Column
)

__all__ = ('post', )

meta = MetaData()

post = Table(
    'post', meta,
    Column('id', Integer, primary_key=True),
    Column('title', VARCHAR, nullable=True),
    Column('body', Text,)
)
