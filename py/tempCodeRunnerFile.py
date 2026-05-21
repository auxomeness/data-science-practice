import requests

url = "https://www.payscale.com/research/PH/Industry=Information_Technology_(IT)_Services/Salary"
r = requests.get(url)

print(r.text[:1000])