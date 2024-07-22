import json

def get_company_data(results, output_path):
    data = results.company[0]

    company = {}
    company['denomination'] = data.denomination
    company['since'] = data.since
    company['site'] = data.site
    company['address'] = data.address
    company['effective'] = data.effective
    company['auditors'] = data.auditors
    company['resume'] = data.resume
    company['capitalisation'] = data.capitalisation
    company['market'] = data.market
        
    with open(output_path, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(company))