from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#create the app
app = Flask(__name__)

db_name = 'testMH.db'

from routes import register_routes
register_routes(app, db) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#initialize app with Flask-SQLAlchemy
db.init_app(app)







if __name__ == '__main__': 
    app.run(debug=True)