from flask import Flask
from Auth.AuthMiddleware import AuthMiddleware

from Routes.Auth.login import login
from Routes.Auth.signup import signup
from Routes.insert import insert
from Routes.update import update
from Routes.updateById import updateByID
from Routes.findCondition import findCondition
from Routes.findId import findId


app=Flask(__name__)

app.wsgi_app = AuthMiddleware(app.wsgi_app)

app.route('/login', methods=['GET', 'POST'])(login)
app.route('/signup', methods=['GET', 'POST'])(signup)

app.route('/insert', methods=['GET'])(insert)

app.route('/updateid', methods=['GET'])(updateByID)
app.route('/update', methods=['GET'])(update)

app.route('/findCondition', methods=['GET'])(findCondition)
app.route('/findId', methods=['GET'])(findId)



app.run(host='localhost',debug=True)