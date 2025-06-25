# we may write our own microservice server using 'socket'
# if we want an html web server we use Flask
# for a full-blown database-driven, authentication cms use django
# we would need to install flask: python -m pip install flask
from flask import Flask

# in Python we are permitted ot declare functions inside functions...
def main():
    '''declare and run a Flask web server'''
    app = Flask(__name__)
    # we declare http routes
    @app.route('/') # this is the root of our web server
    def root():
        return 'Welcome to this Flask server'
    
    # we need our serer to run endlessly
    app.run()


if __name__ == '__main__':
    main()