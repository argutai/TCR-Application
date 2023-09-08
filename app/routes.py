
from flask import render_template, request
from app.models import Graph
from app import app
import pandas as pd
from app.logic import bubble_files, posts, patient_names, patient_list


@app.route("/")
@app.route("/home")
def home():
    client_ip = request.remote_addr
    print(client_ip)
    return render_template('home.html', ip=client_ip, title='TCR Analysis Home')

@app.route("/overview")
def overview():
    return render_template('overview.html', posts=posts, title='Overview')

@app.route("/patients", methods=['GET', 'POST'])
def patients():
    patient = request.form.get('comp_select')
    patient_obj = [] # needs an initialised value ...
    if(patient is not None): patient_obj = [patient_list[patient_names.index(patient)]]
    if(patient is None): patient = "        "
    return render_template('patients.html', patient_obj = patient_obj, patient_names = patient_names)


# obj = patient_list[patient_names.index('KCL717')]
# print(obj.figures[0].expanded.split(",")[0])