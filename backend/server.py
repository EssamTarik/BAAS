from flask import Flask

from Routes.insert import insert
from Routes.update import update
from Routes.findCondition import findCondition
from Routes.delete import delete


app=Flask(__name__)


app.route('/insert')(insert)
app.route('/delete')(delete)

app.route('/update')(update)

app.route('/find')(findCondition)



app.run(host='localhost',debug=True)