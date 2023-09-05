
from flask import render_template, request
from app.models import Graph
from app import app
import pandas as pd
from app.logic import bubble_files, posts, patient_names, patient_list

obj = patient_list[patient_names.index('KCL725')]
print(obj.patient_id) 

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='TCR Analysis Home')

@app.route("/overview")
def overview():
    return render_template('overview.html', posts=posts, title='Overview')

@app.route("/patients", methods=['GET', 'POST'])
def patients():
    patient = request.form.get('comp_select')
    obj = "hi"
    if(patient is not None): obj = patient_list[patient_names.index(patient)]
    if(patient is None): patient = "        "
    patient_bubble_files=[i for i in bubble_files if patient in i]
    return render_template('patients.html', patient=patient, obj = obj, patient_files=patient_bubble_files, title='Patients', data=[{'name':'KCL710'}, {'name':'KCL717'}, {'name':'KCL725'}])



# obj = patient_list[patients.index('KCL717')]
# print(obj.patient_id)
