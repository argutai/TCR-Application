   
from flask import render_template, request, render_template_string
from app.models import Date, IpView, Overview_legend
from app.render_doc import docx_as_html
from app import app, db
from app.logic import fig_list, autoSampleList, filter_attributes
import datetime
import logging
import pandas as pd
import os

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
            day_entry = Date(day, 0, 0, 0, 0, 0)
            db.session.add(day_entry)
        setattr(day_entry,page, int(getattr(day_entry,page)) + 1)

        ip_entry = IpView.query.filter_by(ip=client_ip, date=day).first()
        if not bool(ip_entry):
            ip_entry = IpView(client_ip, day_entry.id, day)
            db.session.add(ip_entry)
        db.session.commit()
    except Exception:
        app.logger.info("DB error from page_hit_to_db")

@app.route("/")
@app.route("/home")
def home():
    page_hit_to_db('home')
    return render_template('home.html', title='TCR Analysis Home')

@app.route("/doc-of-truth")
def doc_of_truth():
    page_hit_to_db('docs')
    docx_as_html()
    return render_template('TCR-doc-of-truth.html')  

@app.route("/bubbles", methods=['GET', 'POST'])
def bubbles():    
    page_hit_to_db('bubbles')
    file_name = request.form.get('colour_by_select')
    if file_name is None:
        file_name = 'bubble_overlay'
    fig = [fig for fig in fig_list if fig.file_name == file_name][0]
 
    return render_template('bubbles.html', fig=fig, fig_list=fig_list)

@app.route("/TCRdist", methods=['GET', 'POST'])
def TCRdist():    
    file_name = request.form.get('colour_by_select')
    if file_name is None:
        file_name = 'none'
    return render_template('TCRdist.html', file_name=file_name)

@app.route("/library", methods=['GET', 'POST'])
def library(): 
    # Define attribute to filter by - any column from metadata
    filtered_sample_list = autoSampleList; search_query = []
    
    dictionary = {}
    for attribute in filter_attributes:
        dictionary[attribute] = list(set(getattr(fsample, attribute) for fsample in autoSampleList))
        filter = request.form.get(attribute)
        if filter is not None:
            search_query.append(filter)
            filtered_sample_list = [fsample for fsample in filtered_sample_list if getattr(fsample, attribute) == filter]

    search_query = ', '.join(search_query)
    return render_template('library.html', search_query=search_query, filtered_sample_list=filtered_sample_list, dictionary=dictionary)
   
@app.route("/sample", methods=['GET', 'POST'])
def sample():
    sample_name = request.form.get('sample_button')
    sample = [sample for sample in autoSampleList if sample.id == sample_name ][0]
    absolute_path = os.path.dirname(__file__)
    file = os.path.join(absolute_path, 'static/KCL-content/summary_stats/' + sample.id + '.tsv')
    df = pd.read_csv(file, delimiter='\t')
    return render_template('sample.html', sample = sample, df=df, table_len=len(df))

@app.route("/hits")
def hits():
    try:
        day_hits = Date.query.all()
        return render_template('hits.html', day_hits=day_hits)
    except Exception:
        app.logger.info("DB error from hit route")   