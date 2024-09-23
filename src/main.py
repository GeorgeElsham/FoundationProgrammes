from pathlib import Path

print("MedScript\n=========")

pages = []
for page_number in range(1, 12):
    path = Path(__file__).parent / f"../data/page{page_number}.json"
    with open(path) as f: pages.append(f.read())
