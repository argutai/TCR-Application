
from flask import render_template, request
from app.models import Hit
from app import app, db
from app.logic import posts, patient_names, patient_list
import datetime
 
def get_current_day():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d") 

app.app_context().push()
db.create_all()

@app.route("/")
@app.route("/home")
def home():
    # client_ip = request.remote_addr 
    # new_IP = Hit(IP_address=client_ip, Page='Home', Date=get_current_day())
    # db.session.add(new_IP); db.session.commit()

    return render_template('home.html', title='TCR Analysis Home')

@app.route("/overview")
def overview():
    # client_ip = request.remote_addr 
    # new_IP = Hit(IP_address=client_ip, Page='Overview', Date=get_current_day())
    # db.session.add(new_IP); db.session.commit()

    return render_template('overview.html', posts=posts, title='Overview')

@app.route("/cb-project-landscape")
def project_landscape():
    return render_template('project-landscape.html')
 
@app.route("/patients", methods=['GET', 'POST'])
def patients():
    client_ip = request.remote_addr 
    new_IP = Hit(IP_address=client_ip, Page='Patients', Date=get_current_day())
    db.session.add(new_IP); db.session.commit()

    patient = request.form.get('comp_select')
    patient_obj = [] # needs an initialised value ...
    if(patient is not None): patient_obj = [patient_list[patient_names.index(patient)]]
    if(patient is None): patient = "        "
    return render_template('patients.html', patient_obj = patient_obj, patient_names = patient_names)
 
@app.route("/hits")
def hits():
    hits = "hi" #Hit.query.all() 
    return render_template('hits.html', hits = hits)

# obj = patient_list[patient_names.index('KCL717')]
# print(obj.figures[0].expanded.split(",")[0])