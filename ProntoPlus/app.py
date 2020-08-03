from ProntoPlus.ViewHandlers import start
import ProntoPlus.Models.db as db

if __name__ == '__main__':
    if db.config['DB']['connstring'][:8] == 'sqlite://':
        db.metadata.create_all(db.engine)
    start()
