from app import app, db
from app.data import register_tables


if __name__ == '__main__':
    register_tables(db)
    app.run()
