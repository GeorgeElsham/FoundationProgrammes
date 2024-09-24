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

output_data = [[
    "ID",
    "Job Code",
    "Deanery",
    "Programme Type",
    "F1 Hospital Trust",
    "F2 Hospital Trust",
    "F1 Title",
    "F2 Title",
    "Description",
    "Speciality 1",
    "Speciality 2",
    "Speciality 3",
    "Speciality 4",
    "Speciality 5",
    "Speciality 6",
    "Speciality 7",
    "Speciality 8",
]]

for programme in programmes:
    id = programme["FoundationProgrammesId"]
    job_code = programme["ProgrammePreference"]
    deanery = programme["Deanery"]
    programme_type = programme["ProgrammeType"]

    trusts = programme["EmployerTrust"].split(", ")
    f1_hospital_trust = trusts[0]
    f2_hospital_trust = trusts[1] if len(trusts) > 1 else ""

    title = programme["ProgrammeTitle"]
    title_pattern = r"(F1 ?:(?P<f1>(?:(?!F2 ?:).)+))?(?:F2 ?:(?P<f2>.+))?"
    title_regex = re.compile(title_pattern)
    title_match = title_regex.match(title)
    f1_title = (title_match.group('f1') or "").strip()
    f2_title = (title_match.group('f2') or "").strip()

    description = programme["ProgrammeDescription"]

    specialities = programme["Specialties"].split(", ")

    row = [
        id,
        job_code,
        deanery,
        programme_type,
        f1_hospital_trust,
        f2_hospital_trust,
        f1_title,
        f2_title,
        description,
    ]
    for speciality in specialities:
        row.append(speciality)
    output_data.append(row)

output_path = Path(__file__).parent / f"../output/med.csv"
with open(output_path, "w") as file:
    writer = csv.writer(file)
    writer.writerows(output_data)

print("Done!")
