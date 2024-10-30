import requests
import csv

with open('dhabstracts_urls.csv', 'r') as data_in, open('dhabstracts_status.csv', 'w') as data_out:
    reader = csv.reader(data_in, delimiter=',')
    writer = csv.writer(data_out, delimiter=',')
    headers = ['url','status_code']
    writer.writerow(headers)
    next(reader, None)  # skip the headers
    for row in reader:
        url = row[0]
        try:
            response = requests.get(url, verify=False)
            status = response.status_code
            print(url + ' ' + str(status))
            writer.writerow([url,str(status)])
        except requests.exceptions.RequestException as e:
            print(url + ' did not work')
            writer.writerow([url,str(e)])
