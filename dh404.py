import requests
import csv
import re
from urlextract import URLExtract

with open('dh_conferences_data/works.csv', 'r', encoding="UTF-8") as file_in:
    text = file_in.read()
    extractor = URLExtract()
    urls = extractor.find_urls(text)

    with open('dhabstracts_urls.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        headers = ['url','status_code']
        writer.writerow(headers)
        for url in urls:
            row = [url]
            writer.writerow(row)