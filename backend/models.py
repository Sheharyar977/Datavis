from main import db


class MHdb(db.Model): 
    __tablename__ = 'MH2'
    
    id = db.Column(db.Integer, primary_key=True)
    Location = db.Column(db.String)
    Total_Mental_Health_Care_HPSA_Designations = db.Column(db.Integer)
    Population_of_Designated_HPSA = db.Column(db.Integer)
    Percent_of_Need_Met = db.Column(db.Float)
    Practioners_Needed_to_Remove_HPSA_Designation = db.Column(db.Integer)






