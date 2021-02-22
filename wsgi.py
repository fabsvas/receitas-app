import sys
from src.main import app, initialize_db

if __name__ == '__main__':
    if 'create_db' in sys.argv:
        initialize_db(app)
    app.run(debug=False)

# TODO: implement gunicorn for start project
