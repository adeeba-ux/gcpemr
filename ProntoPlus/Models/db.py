import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as sa_ext
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')


metadata = sa.MetaData()
engine = sa.create_engine(cfg['DB']['connstring'], echo=False)
metadata.create_all(engine)
session = orm.sessionmaker(engine)()

metadata.create_all(engine)
