import requests
import csv
import re
from urlextract import URLExtract

with open('dh_conferences_data/works.csv', 'r', encoding="UTF-8") as file_in, open('dhabstracts_urls.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    headers = ['url','status_code']
    writer.writerow(headers)

    reader = csv.reader(file_in, delimiter=",")
    next(reader, None)  # skip the headers

    for row in reader:
        full_text = row[4]
        full_text = ''.join(full_text.splitlines())
        extractor = URLExtract()
        urls = extractor.find_urls(full_text)

        for url in urls:
            row = [url]
            writer.writerow(row)