import json
from schema.Person.Person import ExtractionData as PersonSchema
from services.person.person import get_person_data
from services.extract_data import extract_data


def handler(event):
    company_name = event['company_name']
    file_path = (
        event['file_path']
    )

    with open(f"data/{company_name}/Comex/Compensation/compensation.json") as comex_file:
        comex = json.load(comex_file)

    with open(f"data/{company_name}/Mandatary/Compensation/compensation.json") as mandatary_file:
        mandatary = json.load(mandatary_file)

    comex_names = [person['name'] for person in comex]
    mandatary_names = [person['name'] for person in mandatary]

    company_persons = comex_names + mandatary_names

    output_path = f"data/{company_name}/Person/person.json"
    persons = []
    
    for person in company_persons:
        invoke_prompt = f"Key informations associated to {person}."
        chat_prompt = f"You are an expert at identifying key information about {person} in the text."

        results = extract_data(PersonSchema, invoke_prompt, chat_prompt, file_path)
        person = results.person[0]
        persons.append(person)

    print(persons)
    get_person_data(persons, output_path)

event = {
    'file_path' : './filings/ROKU-INC-DEF-14-PROXY.pdf',
    'company_name': "ROKU-INC"
}

handler(event)

