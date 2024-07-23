import json
import pandas as pd
import os

companies = [
    "APPLE",
    "ABBVIE",
    "ABBOTT-LABORATORIES",
    "AGILENT-TECHNOLOGY",
    "AMAZON",
    "AMERICAN-TOWER-CORP",
    "CLEAR-CHANNEL-OUTDOOR",
    "DOLBY-LABORATORIES",
    "MATTEL-INC",
    "ROKU-INC",
    "SKECHERS-USA",
    "TESLA"
]

dataframes = []

for company in companies:
    file_path = os.path.join("data", company, "Mandatary", "Compensation", "compensation.json")
    with open(file_path) as f:
        data = json.load(f)
        for person in data:
            person['company'] = company
    df = pd.json_normalize(data)
    dataframes.append(df)

df = pd.concat(dataframes, ignore_index=True)

output_file = "excel/mandatary.xlsx"
df.to_excel(output_file, index=False)
