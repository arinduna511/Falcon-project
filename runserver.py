from main import app
from werkzeug.serving import run_simple

if __name__ == '__main__':
    run_simple('localhost', 5000, app, use_reloader=True)
