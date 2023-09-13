from app import db


    
class IpView(db.Model):
    id = db.Column("id", db.Integer, primary_key=True) #, db.ForeignKey(date.id)
    date_id = db.Column('date_id', db.Integer, db.ForeignKey('date.id'))
    ip = db.Column("ip", db.String(20))
    # dates = db.relationship('Date', backref='ip_diffname', lazy=True)

    def __init__(self, ip, date_id):
        self.ip = ip
        self.date_id = date_id

class Date(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    day = db.Column('day', db.String)
    patients = db.Column('patients', db.String)
    home = db.Column('home', db.String)
    prj_landscape = db.Column('prj_landscape', db.String)
    # ip_id = db.Column('ip_id', db.Integer, db.ForeignKey('ip_view.id'))
    ip2 = db.relationship('IpView', backref='date_diffname', lazy=True)

    def __init__(self, day, home, patients, prj_landscape):
        self.day = day
        # self.ip_id = ip_id
        self.home = home
        self.patients = patients
        self.prj_landscape = prj_landscape

# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()
# >>> from app.models import Hit
# >>> new_IP = Hit(IP_address='1.00.390.98', Date='2023-09-11')
# >>> db.session.add(new_IP)
# >>> Hit.query.all() 
# >>> db.drop_all() # clears all data from db