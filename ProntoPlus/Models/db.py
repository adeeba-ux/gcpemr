import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as sa_ext
import configparser as cfg

config = cfg.ConfigParser()
config.read('../config.ini')

metadata = sa.MetaData()
engine = sa.create_engine("sqlite:///", echo=False)
metadata.create_all(engine)
session = orm.sessionmaker(engine)()

