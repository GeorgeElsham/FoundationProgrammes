# Foundation Programmes

## What is this

This is a Python script to generate a CSV for [NHS Foundation Programmes 2025](https://www.oriel.nhs.uk/Web/Programme/GetProgramme/L085MXN4K1NSeFI3cnBEYTVWM24zeUpOSUJmaGRqZXhlVDVySXNrZytOVUpRdXRQK0dpWFZGWXoxVkIvSmNPRg) containing 10,350 programmes. The script is specialised for the input data and is not designed to be robust for any input—it just needed to work.

## What can I do with this

Use the outputted `med.csv`. You can import it into Microsoft Excel like so:

1) Create a new spreadsheet.
2) File > Import > CSV file.
3) Select `med.csv`.
4) Choose "Delimited" and only "Comma" as the delimiter.
5) Finish import.
6) Select whole table (control/command + A).
7) Insert > Table.
8) Select "My table has headers".
9) Ignore warnings and finish.
10) Complete.

## Quirks

The input data isn't formatted the best, so there are many inconsistencies.

You may see "`[SHORTENED]:`" in the description column for some programmes. This means that the F1 & F2 titles have been extracted from this description, and not displayed in the description anymore for readability.

## Running

The `med.csv` file is already committed in this repository. You shouldn't need to run this script unless you change the code.

Use Python 3 and execute by running `main.py` with `python3 src/main.py` or equivalent.
