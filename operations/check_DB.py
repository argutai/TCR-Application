import sys, os

absolute_path = os.path.dirname(__file__)
path = os.path.join(absolute_path, '..')
sys.path.insert(0, path)

from app import app
from app.models import Date
 
app.app_context().push()

def get_today_ips():
    days = Date.query.all()
    today = days[-1]

    for ip in today.ip2:
        print(ip.ip)

def get_day_ips(day):
    day = list(Date.query.filter_by(day=day))[0]

    for ip in day.ip2:
        print(ip.ip)

get_today_ips()
get_day_ips('2023-10-19')
