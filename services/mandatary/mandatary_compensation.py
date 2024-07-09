import json

def get_mandatary_compensations(results, output_path):
    data = []
    for mandatary in results.mandatary_compensations:
        data.append({
            'name': mandatary.name, 
            'year': mandatary.year, 
            'salary': mandatary.salary, 
            'bonus': mandatary.bonus, 
            'stock_awards': mandatary.stock_awards,
            'other_compensation': mandatary.other_compensation,
            'total_compensation': mandatary.total_compensation
        })
        
    with open(output_path, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(data))