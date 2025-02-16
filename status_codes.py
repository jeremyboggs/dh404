import requests
import csv
from requests.adapters import HTTPAdapter, Retry
import urllib3


with open('dhabstracts_urls.csv', 'r') as data_in, open('dhabstracts_status.csv', 'a', newline='') as data_out:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
    reader = csv.reader(data_in, delimiter=',')
    next(reader, None)  # skip the headers

    writer = csv.writer(data_out, delimiter=',')
    headers = ['url','status_code']
    writer.writerow(headers)

    s = requests.Session()

    retries = Retry(total=0,
                   backoff_factor=0.1,
                   status_forcelist=[ 500, 502, 503, 504 ])

    s.mount('http://', HTTPAdapter(max_retries=retries))
    s.mount('https://', HTTPAdapter(max_retries=retries))

    # for i in range(2502): next(reader)
    for row_number, row in enumerate(reader):
        url = row[0]
        try:
            response = s.get(url, timeout=8, verify=False)
            status = response.status_code
            message = str(status)
        except requests.exceptions.Timeout:
            status = 'timeout'
            message = 'timed out.'
        except requests.exceptions.RequestException as e:
            status = e
            message = 'failed'
        
        print('Row '+ str(row_number+1) + ' ' + url + ' ' + message)
        writer.writerow([url,str(status)])
