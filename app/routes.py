
from flask import render_template, request
from app.models import Date, IpView
from app import app, db
from app.logic import posts, patient_names, patient_list
import datetime
 


def get_current_day():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d") 

#initialise
app.app_context().push()
db.create_all()

def page_hit_to_db(page):
    day=get_current_day()
    client_ip = request.remote_addr

    day_entry = Date.query.filter_by(day=day).first()
    if not bool(day_entry):
        day_entry = Date(day, 0, 0, 0)
        db.session.add(day_entry)
    setattr(day_entry,page, int(getattr(day_entry,page)) + 1)

    ip_entry = IpView.query.filter_by(ip=client_ip).first()
    if not bool(ip_entry):
        ip_entry = IpView(client_ip, day_entry.id)
        db.session.add(ip_entry)
    db.session.commit()

    print(Date.query.all())
    print(IpView.query.all())

@app.route("/")
@app.route("/home")
def home():
    page_hit_to_db('home')
    return render_template('home.html', title='TCR Analysis Home')

@app.route("/overview")
def overview():
    return render_template('overview.html', posts=posts, title='Overview')

@app.route("/cb-project-landscape")
def project_landscape():
    page_hit_to_db('prj_landscape')
    return render_template('project-landscape.html')
 
@app.route("/patients", methods=['GET', 'POST'])
def patients():
    page_hit_to_db('patients')

    patient = request.form.get('comp_select')
    patient_obj = [] # needs an initialised value ...
    if(patient is not None): patient_obj = [patient_list[patient_names.index(patient)]]
    if(patient is None): patient = "        "
    return render_template('patients.html', patient_obj = patient_obj, patient_names = patient_names)
 
@app.route("/hits")
def hits():
    day_hits = Date.query.all() 
    return render_template('hits.html', day_hits=day_hits) #, IpView=IpView)