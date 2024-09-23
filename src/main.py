from pathlib import Path
import json

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

programs = []
for page in pages:
    programs += page["Data"]
