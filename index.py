from flask import Flask
from Auth.AuthMiddleware import AuthMiddleware

from Routes.Auth.login import login
from Routes.Auth.signup import signup

app=Flask(__name__)

app.wsgi_app = AuthMiddleware(app.wsgi_app)

@app.route('/')
def index():
	return 'hello'

app.route('/login', methods=['GET', 'POST'])(login)
app.route('/signup', methods=['GET', 'POST'])(signup)

app.run(host='localhost',debug=True)