from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def getData():
    # info needed by hospital/doctor
    hospInfo = ["f_name", "mi", "l_name", "dob", "phone_num", "ss", "address", "city", "state", "zip", "sex"]

    # get the info from the client
    if request.method == 'POST':
        f_name = request.form.get('f_name')
        mi = request.form.get('MI')
        l_name = request.form.get('l_name')
        dob = request.form.get('dob')
        phone_num = request.form.get('phone_num')
        ss = request.form.get('SS')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        zip = request.form.get('zip')
        sex = request.form.get('sex')

    clientInfo = [f_name, mi, l_name, dob, phone_num, ss, address, city, state, zip, sex]

    # information not provided by client but still needed by hospital
    infoNeeded = []

    # check that hospital has all of the info they need
    for item in hospInfo:
        if item not in clientInfo.keys():
            infoNeeded.append(item)