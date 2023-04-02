import os
import csv
from flask import Flask, request
from dotenv import load_dotenv
import openai
load_dotenv()

app = Flask(__name__)

drug_list = [
    'Abilify Maintena'
]

full_drug_list = []

input_file = 'finaldrugs2.csv'


@app.route("/getmydrugs", methods=['GET'])
def getMyDrugs():
    if request.method == 'GET':
        return drug_list
    return "error"


@app.route('/addmydrug', methods=['POST'])
def addMyDrug():
    drug = request.form['drug']
    if drug not in drug_list:
        drug_list.append(drug)
    return f"{drug} added to drug list."


@app.route("/summary", methods=['GET'])
def getSummary():
    if request.method == 'GET':
        params = request.args
        print('Getting information for: ' + params['drug'])
        return prompt_chatbot(generate_prompt(params['drug'], getDrug(params['drug'])))['content']
    return "error"


@app.route('/fulldrug', methods=['GET'])
def getFullDrug():
    if request.method == 'GET':
        params = request.args
        os.getenv('OPENAI_APIKEY')
        print(params['drug'])
        return getDrug(params['drug'])
    return "error"


def generate_prompt(drug_name, drug_info):
    # this will basically grab the drug info and then generate a prompt with it so that the chatbot can use
    # it to answer questions
    return """
	The drug's name is {}. Here are the side effects: {}.
	""".format(drug_name, drug_info)


def prompt_chatbot(prompt):
    openai.organization = os.getenv('OPENAI_ORG')
    openai.api_key = os.getenv('OPENAI_API_KEY')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Given the following description of the side effects of this drug, please provide a concise summary of the most important information."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
        temperature=0.7,
    )
    return completion.choices[0].message


def getDrug(drug):
    file = open(input_file)
    csvreader = csv.reader(file)

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

    return info[1]


@app.route('/druglist', methods=['GET'])
def getDrugList():
    if request.method == 'GET':
        if len(full_drug_list) == 0:
            return drugList()
        else:
            return full_drug_list
    return "error"


def drugList():
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        first_column = [row[0] for row in reader]
        full_drug_list = first_column[1:]
    return full_drug_list
