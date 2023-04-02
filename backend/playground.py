import csv
import openai
import os
from dotenv import load_dotenv
load_dotenv()


def getDrug(drug):
    file = open('finaldrugs2.csv')
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

    return info


def longest_line(file_path):
    with open(file_path, 'r') as f:
        return max(len(line) for line in f)


def find_longest_entry(file_path):
    max_row = None
    max_col = None
    max_len = 0
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for col, value in row.items():
                if len(value) > max_len:
                    max_row = row
                    max_len = len(value)
                    max_col = col
    return max_col, max_len, max_row[max_col]


def print_headers(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        print(headers)


def create_new_csv(old_file_path, new_file_path):
    with open(old_file_path, 'r') as old_file, open(new_file_path, 'w', newline='') as new_file:
        reader = csv.DictReader(old_file)
        fieldnames = ['drug_name', 'side_effects',
                      'generic_name', 'medical_condition_description']
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            new_row = {k: v.split('your doctor')[0]
                       for k, v in row.items() if k in fieldnames}
            writer.writerow(new_row)


def create_extra_new_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['drug_name', 'side_effects',
                      'generic_name']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            side_effects = row['side_effects']
            # side_effects = side_effects[:2000]
            writer.writerow({
                'drug_name': row['drug_name'],
                'side_effects': side_effects,
                'generic_name': row['generic_name'],
            })


def cap_all_columns(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            for column_name in fieldnames:
                row[column_name] = row[column_name][:2000]
            writer.writerow(row)


def remove_blank_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            if any(field.strip() for field in row):
                writer.writerow(row)


def generate_prompt(drug_name, drug_info):
    # this will basically grab the drug info and then generate a prompt with it so that the chatbot can use
    # it to answer questions
    return """
	The drug's name is {}. Here are the side effects: {}.
	""".format(drug_name, drug_info)


def getDrug(drug):
    file = open('finaldrugs2.csv')
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


if __name__ == '__main__':
    # cap_all_columns('minidrugs.csv', 'simplified_drugs.csv')
    # create_extra_new_csv('simplified_drugs.csv', 'finaldrugs.csv')
    # remove_blank_lines('finaldrugs.csv', 'finaldrugs2.csv')
    # os.remove('simplified_drugs.csv')
    # os.remove('finaldrugs.csv')

    # print(getDrug('Abilify Maintena'))
    print(prompt_chatbot(generate_prompt(
        'Abilify Maintena', getDrug('Abilify Maintena'))))
