from flask import Flask
from Auth.AuthMiddleware import AuthMiddleware

from Routes.Auth.login import login
from Routes.Auth.signup import signup
from Routes.insert import insert
from Routes.update import update
from Routes.updateById import updateByID
from Routes.findCondition import findCondition
from Routes.findId import findId
from Routes.delete import delete


app=Flask(__name__)


@app.after_request
def after_request(response):
	response.headers['Access-Control-Allow-Origin'] = '*'
	return response
app.wsgi_app = AuthMiddleware(app.wsgi_app)

app.route('/login', methods=['GET', 'POST'])(login)
app.route('/signup', methods=['GET', 'POST'])(signup)

app.route('/insert', methods=['GET', 'PUT'])(insert)
app.route('/delete', methods=['GET', 'DELETE'])(delete)

app.route('/updateid', methods=['GET', 'POST'])(updateByID)
app.route('/update', methods=['GET', 'POST'])(update)

app.route('/findCondition', methods=['GET'])(findCondition)
app.route('/findId', methods=['GET'])(findId)

@app.route('/admin/test')
def test():
	import json
	return json.dumps({"name": "essam"})


app.run(host='localhost',debug=True)