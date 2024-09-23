from pathlib import Path
import json
import re

print("MedScript\n=========")

def pretty(data):
    return json.dumps(data, indent=True)

pages = []
for page_number in range(1, 12):
    path = Path(__file__).parent / f"../data/page{page_number}.json"
    with open(path) as f:
        page_str = f.read()
        page = json.loads(page_str)
        pages.append(page)

programmes = []
for page in pages:
    programmes += page["Data"]

max_speciality_length = 8 # Hardcoded because easy

for programme in programmes:
    job_code = programme["ProgrammePreference"]
    deanery = programme["Deanery"]
    programme_type = programme["ProgrammeType"]

    full_title = programme["ProgrammeTitle"]
    title_pattern = r"(F1 ?:(?P<f1>[^F]+))?(?:F2 ?:(?P<f2>.+))?"
    title_regex = re.compile(title_pattern)
    title = title_regex.match(full_title)
    f1_hospital_trust = (title.group('f1') or "").strip()
    f2_hospital_trust = (title.group('f2') or "").split()

    specialities = programme["Specialties"].split(", ")
    specialities_length = len(specialities)
    if specialities_length > max_speciality_length:
        raise Exception(f"Exceeded max speciality length")
