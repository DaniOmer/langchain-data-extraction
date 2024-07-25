import json

def get_person_data(results, output_path):
    data = []
    for person in results:
        data.append({
            'name': person.name,
            'gender': person.gender,
            'date_birth': person.date_birth, 
            'resume': person.resume, 
        })
        
    with open(output_path, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(data))