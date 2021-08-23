import requests
import os

from flask import (
    Blueprint, redirect, request, url_for, render_template
)

ftasks = Blueprint('ftasks',__name__)

@ftasks.route('/', methods=('GET','POST'))
def index():
    context={}
    if request.method == 'POST':
        print("[*] received post request ...")
        project_id = request.form['project_id']
        #due to networking we can access the docker tools container simply by typing "tools", we do not need any ip-adress
        url = 'http://tools:5001/' + str(project_id) + '/test_receiver'
        print("\t[+] constructed url: {}".format(url))
        print("\t[*] trying to redirect request ...")
        return requests.get(url).content
    else:
        project_folders = os.listdir('data')
        context['project_folders'] = project_folders
        return render_template('ftasks/index.html', content=context)


#requests.get('http://172.20.0.2:5001/mafft_info').content
