from schema.Executive.ExecutiveCompensation import ExtractionData as ExecutiveExtrationSchema
from schema.Mandatary.MandataryCompensation import ExtractionData as MandatoryExtractionSchema
from services.executive.executive_compensation import get_executive_compensations
from services.mandatary.mandatary_compensation import get_mandatary_compensations
from services.extract_data import extract_data

def handler(event):
    company_name = event['company_name']
    role = event['role']
    file_path = (
        event['file_path']
    )

    executive_output_path = f"data/{company_name}/{role}/Compensation/compensation.json"
    mandatary_output_path = f"data/{company_name}/{role}/Compensation/compensation.json"

    invoke_prompt_for_executive = "Key informations associated with executive officers."
    invoke_prompt_for_mandatary = "Key informations associated with non-employee directors also known as board committees."

    chat_prompt = "You are an expert at identifying key information about the company and his members in the text."

    if role == 'Mandatary':
        mandatary_compensation_data = extract_data(MandatoryExtractionSchema, invoke_prompt_for_mandatary, chat_prompt, file_path, search_type="mmr")
        get_mandatary_compensations(mandatary_compensation_data, mandatary_output_path)
    elif role == 'Comex':
        executive_compensations_data = extract_data(ExecutiveExtrationSchema, invoke_prompt_for_executive, chat_prompt, file_path, search_type="mmr")
        get_executive_compensations(executive_compensations_data, executive_output_path)

event = {
    'file_path' : './filings/ROKU-INC-DEF-14-PROXY.pdf',
    'role' : 'Mandatary',
    'company_name': "ROKU-INC"
}

handler(event)
