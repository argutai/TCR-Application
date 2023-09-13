from app import db


class Hit(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    IP_address = db.Column('IP_address', db.String(20))
    Page = db.Column('Page', db.String(20))
    Date = db.Column('Date', db.String())
    
    def __repr__(self):
        return f"IP address: {self.IP_address},  Page: {self.Page},  Date: {self.Date}"
        
# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()
# >>> from app.models import Hit
# >>> new_IP = Hit(IP_address='1.00.390.98', Date='2023-09-11')
# >>> db.session.add(new_IP)
# >>> Hit.query.all() 
# >>> db.drop_all() # clears all data from db