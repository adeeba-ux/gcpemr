import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as sa_ext
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')



metadata = sa.MetaData()
# metadata.create_all(engine)
# engine = sa.create_engine(cfg['DB']['connstring'])
# session = orm.sessionmaker(engine)()