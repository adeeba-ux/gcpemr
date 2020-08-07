# begin prod import compatibility
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
# end prod import compatibility

from ProntoPlus.ViewHandlers import start
import ProntoPlus.Models.db as db
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')

if __name__ == '__main__':
    if cfg['DB']['connstring'] == 'sqlite://':
        db.metadata.create_all(db.engine)
    start(cfg)
