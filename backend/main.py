from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text 

db = SQLAlchemy()

#create the app
app = Flask(__name__)

db_name = 'testMH.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = True

#initialize app with Flask-SQLAlchemy
db.init_app(app)

@app.route('/')
def testdb(): 
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__': 
    app.run(debug=True)