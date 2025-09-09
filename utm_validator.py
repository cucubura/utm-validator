import requests
import pandas as pd

contents = pd.read_csv("../utm_urls.csv")
valid = 0
invalid = 0
url = []
status = []
working = []
for row in contents.itertuples():
    if "utm_source=" in row.url and "utm_medium=" in row.url and "utm_campaign=" in row.url:
        urlcheck = requests.get(row.url)
        if urlcheck.status_code == 200:
            print("The URL is working and URL contains valid UTM parameters: ")
        else:
            print("The URL is not working but URL contains valid UTM parameters: ")
        print(row.url)
        valid += 1
        url.append(row.url)
        status.append("UTM Present")
    else:
        urlcheck = requests.get(row.url)
        if urlcheck.status_code == 200:
            print("The URL is working and URL does not contains valid UTM parameters: ")
        else:
            print("The URL is not working but URL does not contains valid UTM parameters: ")
        print(row.url)
        invalid += 1
        url.append(row.url)
        status.append("UTM Missing")
data = {'URL': url, 'Status': status}
    
df = pd.DataFrame(data)
df.to_csv('utm_report.csv', index=False)
print(f"Total valid URLs: {valid}")
print(f"Total invalid URLs: {invalid}")
