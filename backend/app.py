import os
import csv
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/summary", methods=['GET'])
def getSummary():
    if request.method == 'GET':
        params = request.args
        os.getenv('OPENAI_APIKEY')
        print(params['drug'])
        return getDrug(params['drug'])
    return "<p>error</p>"


def generate_prompt(drug_name, drug_info):
    # this will basically grab the drug info and then generate a prompt with it so that the chatbot can use
    # it to answer questions
    return """
    The following is a conversation with a doctor about a patient's prescription. The doctor is you.
    Patient: I have a prescription for a drug called {}, here is the information about the drug: {}.
    Patient: Could you please answer some questions about the drug for me? Doctor: Sure, what would you like to know?
    Patient: What is a summary of the side effects? 
    """.format(drug_name, drug_info)


def prompt_chatbot(prompt):
    # this will take the prompt and then use the chatbot to generate a response
    # this will return a string of the response
    return "This is the response"


def getDrug(drug):
    file = open('simplified_drugs.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)

    rows = []
    for r in csvreader:
        rows.append(r)

    file.close()

    info = []
    # if client submitted a drug name
    # get all of the info about the drug
    for drugInfo in rows:
        if drugInfo[0] == drug:
            info = drugInfo
            break

    return header, info

# @app.route("/", methods=['POST'])
# def getData():
#     # info needed by hospital/doctor
#     hospInfo = ["f_name", "mi", "l_name", "dob", "phone_num",
#                 "ss", "address", "city", "state", "zip", "sex"]

#     # get the info from the client
#     if request.method == 'POST':
#         f_name = request.form.get('f_name')
#         mi = request.form.get('MI')
#         l_name = request.form.get('l_name')
#         dob = request.form.get('dob')
#         phone_num = request.form.get('phone_num')
#         ss = request.form.get('SS')
#         address = request.form.get('address')
#         city = request.form.get('city')
#         state = request.form.get('state')
#         zip = request.form.get('zip')
#         sex = request.form.get('sex')

#     clientInfo = [f_name, mi, l_name, dob, phone_num,
#                   ss, address, city, state, zip, sex]

#     # information not provided by client but still needed by hospital
#     infoNeeded = []

#     # check that hospital has all of the info they need
#     for item in hospInfo:
#         if item not in clientInfo.keys():
#             infoNeeded.append(item)
