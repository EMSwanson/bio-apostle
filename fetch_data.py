import requests

# base request - http://climatedataapi.worldbank.org/climateweb/rest/v1/country/type/var/start/end/ISO3[.ext]

class ClimateBank(object):
    def __init__(self, type, var, start, end, ISO3):
        self.type = "annualavg"
        self.var = "pr"
        self.start = 1980
        self.end = 2020
        self.ISO3 = "USA"

    def get_data():
        pass


response = requests.get("http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/pr/1980/1999/USA.json")
print(response.status_code)
print(response.content)    
