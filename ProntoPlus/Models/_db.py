import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as sa_ext
import configparser as cfg

config = cfg.ConfigParser()
config.read('../config.ini')

engine = sa.create_engine(config['db']['connstring'])
db_session = orm.scoped_session(orm.sessionmaker(autocommit=False, autoflush=False, bind=engine))


Model = sa_ext.declarative_base(name='Model')
Model.query = db_session.query_property()
