from bottle import default_app, run, route, get, post, request, template

import sqlite3

@route('/')
def hello_world():
    return 'Hello from Bottle! ;)'

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print (username)
    print (password)
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(username, password):
    if username == 'cs':
        return True
    else:
        return False

if __name__ == '__main__':
    run()
else:
    application = default_app()
