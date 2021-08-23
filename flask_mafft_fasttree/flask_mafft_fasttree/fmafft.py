import subprocess
import os

from flask import (
    Blueprint, redirect, request, url_for, render_template
)

fmafft = Blueprint('fmafft',__name__)

@fmafft.route('/mafft_info',methods=['GET'])
def index():
    print("[*] Trying to perform a Popen call with mafft ...")
    process = subprocess.getoutput('mafft --help')
    return render_template('fmafft/index.html',content=process)

@fmafft.route('/<int:project_id>/test_receiver', methods=["GET"])
def receiver(project_id):
    context = {}
    print("[+] Redirection suceeded ...")
    greeting = 'Hello, now we can work on your project with project_id : {}'.format(project_id)
    context['greeting'] = greeting
    context['project_id'] = project_id
    files = os.listdir('data/'+str(project_id))
    context['files'] = files
    return render_template('fmafft/index.html',content=context)

@fmafft.route('/multialigner', methods=["POST"])
def perform_multi_alignment():
    filename = request.form['filename']
    project_id = request.form['project_id']
    print("[*] Trying to perform multiple sequence alignment with : {}".format(filename))
    path_to_inputfile = "data/"+str(project_id)+'/'+str(filename)
    path_to_outputfile = "data/"+str(project_id)+'/mafft_multiple_alignment.msa'
    command = "mafft --quiet --auto {} > {}".format(path_to_inputfile,path_to_outputfile)
    #['mafft','--quiet','--auto',path_to_inputfile,'>','path_to_outputfile']
    process = subprocess.Popen(command,shell=True)
    returncode = process.wait(timeout=800)
    return redirect(url_for('fmafft.receiver',project_id=int(project_id)))
