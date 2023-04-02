from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def getProfile():
    if request.method == 'POST':
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        dob = request.form.get('dob')
        sex = request.form.get('sex')
        insurance = request.form.get('insurance')
        bloodtype = request.form.get('bloodtype')
        height = request.form.get('height')
        weight = request.form.get('weight')
        meds = request.form.get('meds')

