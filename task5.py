import csv

percent = float(input())

with open("vps.csv", "r", encoding='utf8') as infile:
    data = csv.DictReader(infile, delimiter=";", quotechar='"')
    for x in data:
        if float(x['соответствует в %']) >= percent:
            print(x['Специальность'])
