from pathlib import Path
import csv
import json
import re

print("MedScript\n=========")

def pretty(data):
    return json.dumps(data, indent=True)

pages = []
for page_number in range(1, 12):
    path = Path(__file__).parent / f"../data/page{page_number}.json"
    with open(path) as file:
        page_str = file.read()
        page = json.loads(page_str)
        pages.append(page)

programmes = []
for page in pages:
    programmes += page["Data"]

output_data = [["Job Code", "Deanery", "Programme Type", "F1 Hospital Trust", "F2 Hospital Trust", "Specialities"]]

for programme in programmes:
    job_code = programme["ProgrammePreference"]
    deanery = programme["Deanery"]
    programme_type = programme["ProgrammeType"]

    full_title = programme["ProgrammeTitle"]
    title_pattern = r"(F1 ?:(?P<f1>[^F]+))?(?:F2 ?:(?P<f2>.+))?"
    title_regex = re.compile(title_pattern)
    title = title_regex.match(full_title)
    f1_hospital_trust = (title.group('f1') or "").strip()
    f2_hospital_trust = (title.group('f2') or "").strip()

    specialities = programme["Specialties"].split(", ")

    row = [
        job_code,
        deanery,
        programme_type,
        f1_hospital_trust,
        f2_hospital_trust,
    ]
    for speciality in specialities:
        row.append(speciality)
    output_data.append(row)

output_path = Path(__file__).parent / f"../output/med.csv"
with open(output_path, "w") as file:
    writer = csv.writer(file)
    writer.writerows(output_data)
