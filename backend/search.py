from flask import Flask, request
import csv

app = Flask(__name__)

@app.route("/", methods=['POST'])
def getDrug():
    file = open('drugs.csv')
    csvreader = csv.reader(file)
    header = next(csvreader)

    rows = []
    for r in csvreader:
        rows.append(r)

    file.close()

    info = []
    # if client submitted a drug name
    if request.method == 'POST':
        drug = request.form.get('drug')
        # get all of the info about the drug
        for drugInfo in rows:
            if drugInfo[0] == drug:
                info = drugInfo
                break
    
    return header, info