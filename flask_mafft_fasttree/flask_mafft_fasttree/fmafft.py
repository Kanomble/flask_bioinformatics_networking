import subprocess
import os

from flask import (
    Blueprint, redirect, request, url_for, render_template
)

fmafft = Blueprint('fmafft',__name__)

@fmafft.route('/mafft_info')
def index():
    print("[*] Trying to perform a Popen call with mafft ...")
    process = subprocess.getoutput('mafft --help')
    return render_template('fmafft/index.html',content=process)

@fmafft.route('/<int:project_id>/test_receiver')
def receiver(project_id):
    context = {}
    print("[+] Redirection suceeded ...")
    greeting = 'Hello, now we can work on your project with project_id : {}'.format(project_id)
    context['greeting'] = greeting
    files = os.listdir('data/'+str(project_id))
    context['files'] = files
    return render_template('fmafft/index.html',content=context)
