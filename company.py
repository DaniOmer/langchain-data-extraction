from schema.Company.Company import ExtractionData as CompanySchema
from services.company.company import get_company_data
from services.extract_data import extract_data

def handler(event):
    company_name = event['company_name']
    file_path = (
        event['file_path']
    )

    output_path = f"data/{company_name}/Company/company.json"
    invoke_prompt = "Key informations associated to the company."
    chat_prompt = "You are an expert at identifying key information about the company in the text."

    data = extract_data(CompanySchema, invoke_prompt, chat_prompt, file_path)
    get_company_data(data, output_path)


event = {
    'file_path' : './filings/ROKU-INC-DEF-14-PROXY.pdf',
    'company_name': "ROKU-INC",
}

handler(event)

