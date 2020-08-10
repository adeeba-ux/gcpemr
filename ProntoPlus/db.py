import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as sa_ext
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')


def make_engine():
    return sa.create_engine(cfg['DB']['connstring'], echo=False)


def make_session(engine):
    return orm.sessionmaker(engine)()

metadata = sa.MetaData()

#
# metadata.create_all(engine)
# session = orm.sessionmaker(engine)()
#
# metadata.create_all(engine)
