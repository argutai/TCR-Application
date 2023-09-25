from app import db

class IpView(db.Model):
    id = db.Column("id", db.Integer, primary_key=True) #, db.ForeignKey(date.id)
    date_id = db.Column('date_id', db.Integer, db.ForeignKey('date.id'))
    ip = db.Column("ip", db.String(20))
    date = db.Column("date", db.String(20))

    def __init__(self, ip, date_id, date):
        self.ip = ip
        self.date_id = date_id
        self.date = date
 
class Date(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    day = db.Column('day', db.String)
    patients = db.Column('patients', db.String)
    home = db.Column('home', db.String)
    prj_landscape = db.Column('prj_landscape', db.String)
    ip2 = db.relationship('IpView', backref='date_diffname', lazy=True)

    def __init__(self, day, home, patients, prj_landscape):
        self.day = day
        self.home = home
        self.patients = patients
        self.prj_landscape = prj_landscape

class Overview_legend(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    legend = db.Column('legend', db.String)
    colour_by = db.Column('colour_by', db.String)
    def __init__(self, legend, colour_by):
        self.legend = legend
        self.colour_by = colour_by
         