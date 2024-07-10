from models import MHdb
from sqlalchemy.sql import text 



def register_routes(app, db): 


    @app.route('/a')
    def testdb(): 
        try:
            db.session.query(text('1')).from_statement(text('SELECT 1')).all()
            return '<h1>It works.</h1>'
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text

    @app.route('/')
    def index(): 

        try:
            locations = db.session.execute(MHdb.Location).distinct()
            print("Generated Query:", locations)
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text

