# we may write our own microservice server using 'socket'
# if we want an html web server we use Flask
# for a full-blown database-driven, authentication cms use django
# we would need to install flask: python -m pip install flask
from flask import Flask

# in Python we are permitted to declare functions inside functions...
def main():
    '''declare and run a Flask web server'''
    app = Flask(__name__)
    # we declare http routes
    @app.route('/') # this is the root of our web server
    def root():
        return 'Welcome to this Flask server'
    @app.route('/greet')
    def greet():
        return('greeting')
    # we may have common mis-spellings or alternative brand names...
    @app.route('/aluminum')
    @app.route('/aluminium')
    def al():
        return('it is spelled "aluminium"')
    # we might use flask as a microservice proxy to other services
    @app.route('/data')
    # we could make DB, API or file access requests to retrieve some data
    def data():
        response = '<h2>data goes here</h2>'
        return response

    # we need our serer to run endlessly
    app.run()


if __name__ == '__main__':
    main()