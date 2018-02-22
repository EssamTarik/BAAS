from flask import Flask
from Auth.AuthMiddleware import AuthMiddleware

app=Flask(__name__)

app.wsgi_app = AuthMiddleware(app.wsgi_app)

@app.route('/')
def index():
	return 'hello'


app.run(host='localhost',debug=True)