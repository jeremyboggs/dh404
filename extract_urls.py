import requests
import csv
import re
from urlextract import URLExtract # https://urlextract.readthedocs.io/en/latest/

with open('dh_conferences_data/works.csv', 'r', encoding="UTF-8") as works, open('dh_conferences_data/conferences.csv', 'r', encoding="UTF-8") as conferences, open('dhabstracts_urls.csv', 'w', newline='') as csvfile:

    # Read in the 'conferences.csv' dataset, and skip the header row.
    conferences_in = csv.reader(conferences, delimiter=",")
    next(conferences_in, None)  # skip the headers

    # Create a dictionary for conference ids/years, to use later!
    conference_years = {}
    for conference_row in conferences_in:
        conference_years[conference_row[0]] = conference_row[1]

    # Write a CSV file named 'dhabstracts_urls.csv' and insert a header
    writer = csv.writer(csvfile, delimiter=',')
    headers = ['url','work_id','conference_id','conference_year']
    writer.writerow(headers)

    # Read in the 'works.csv' dataset, and skip the header row.
    works_in = csv.reader(works, delimiter=",")
    next(works_in, None)  # skip the headers

    # Loops over the works data, extract URLs, and write to the
    # 'dhabstracts_urls.csv' file.
    for row in works_in:
        work_id = row[0]
        conference_id = row[1]
        conference_year = conference_years[conference_id]

        raw_text = row[4]
        lines = raw_text.splitlines()
        work_text = "".join(lines)
        extractor = URLExtract()
        urls = extractor.find_urls(work_text, only_unique=True, with_schema_only=True)

        for url in urls:
            if 'et.al' in url:
                 continue
            url_row = [url, work_id, conference_id, conference_year]
            writer.writerow(url_row)