   
from flask import render_template, request
from app.models import Date, IpView, Overview_legend
from app import app, db
from app.logic import patient_names, patient_list, fig_list
import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

def get_current_day():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d")

#initialise
try:
    app.app_context().push()
    db.create_all()
    app.logger.info("DB created")
except Exception:
    app.logger.info("DB error from db init")

def page_hit_to_db(page):
    try:
        day=get_current_day()
        client_ip = request.remote_addr

        day_entry = Date.query.filter_by(day=day).first()
        if not bool(day_entry):
            day_entry = Date(day, 0, 0, 0)
            db.session.add(day_entry)
        setattr(day_entry,page, int(getattr(day_entry,page)) + 1)

        ip_entry = IpView.query.filter_by(ip=client_ip, date=day).first()
        if not bool(ip_entry):
            ip_entry = IpView(client_ip, day_entry.id, day)
            db.session.add(ip_entry)
        db.session.commit()
    except Exception:
        app.logger.info("DB error from page_hit_to_db")

def add_edit(entry, colour_by):
    legend = Overview_legend(entry, colour_by)
    db.session.add(legend)
    db.session.commit()

@app.route("/")
@app.route("/home")
def home():
    page_hit_to_db('home')
    return render_template('home.html', title='TCR Analysis Home')

@app.route("/overview", methods=['GET', 'POST'])
def overview():
    file_name = request.form.get('colour_by_select')
    if file_name is None:
        file_name = 'bubble_overlay'
    fig = [fig for fig in fig_list if fig.file_name == file_name][0]
    print(fig)

    # entry = request.form.get('legend')
    # try:
    #     legend_obj = list(Overview_legend.query.filter_by(colour_by=colour_by))[-1]
    #     legend = legend_obj.legend
    #     colour_by = legend_obj.colour_by
    # except:
    #     legend = "No legend yet"
    # if colour_by is None:
    #     colour_by = "bubble_overlay"
    # if not entry == None:
    #     add_edit(entry, colour_by)
 
    return render_template('overview.html', fig=fig, fig_list=fig_list)

@app.route("/cb-project-landscape")
def project_landscape():
    page_hit_to_db('prj_landscape')
    return render_template('project-landscape.html')

@app.route("/patients", methods=['GET', 'POST'])
def patients():
    page_hit_to_db('patients')

    patient = request.form.get('patient_select')
    patient_obj = [] # needs an initialised value ...
    if(patient is not None): patient_obj = [patient_list[patient_names.index(patient)]]
    if(patient is None): patient = "        "
    return render_template('patients.html', patient_obj = patient_obj, patient_names = patient_names)

@app.route("/hits")
def hits():
    try:
        day_hits = Date.query.all()
        return render_template('hits.html', day_hits=day_hits)
    except Exception:
        app.logger.info("DB error from hit route")