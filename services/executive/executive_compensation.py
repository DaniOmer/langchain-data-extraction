import json

def get_executive_compensations(results, output_path):
    data = []
    for executive in results.executive_compensations:
        data.append({
            'name': executive.name,
            'position': executive.position,
            'gender': executive.gender,
            'salary': executive.salary, 
            'bonus': executive.bonus, 
            'stock_awards': executive.stock_awards,
            'other_compensation': executive.other_compensation,
            'total_compensation': executive.total_compensation
        })
        
    with open(output_path, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(data))