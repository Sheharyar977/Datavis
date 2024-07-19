from sqlalchemy.sql import text 



def register_routes(app, db): 

    class MHdb(db.Model): 
        __tablename__ = 'MH2'
        
        id = db.Column(db.Integer, primary_key=True)
        Location = db.Column(db.String)
        Total_Mental_Health_Care_HPSA_Designations = db.Column(db.Integer)
        Population_of_Designated_HPSA = db.Column(db.Integer)
        Percent_of_Need_Met = db.Column(db.Float)
        Practioners_Needed_to_Remove_HPSA_Designation = db.Column(db.Integer)


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
            locations = db.session.execute(text(MHdb.Location)).distinct()
            ltext = "<p>locations:" + str(locations) + "</p>"
            return ltext
        except Exception as e:
            # e holds description of the error
            error_text = "<p>The error:<br>" + str(e) + "</p>"
            hed = '<h1>Something is broken.</h1>'
            return hed + error_text

