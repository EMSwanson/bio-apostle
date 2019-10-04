import requests

base_request = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/"

class ClimateBank(object):
    def __init__(self, type, var, start, end, country):
        self.type = type
        self.var = var
        self.start = start
        self.end = end
        self.country = country

    def fetch(self):
        return requests.get(f"{base_request}/{self.type}/{self.var}/{self.start}/{self.end}/{self.country}.json")



annual_average_rainfall = ClimateBank("annualavg", "pr", 1980, 1999, "USA")
data = annual_average_rainfall.fetch()
print(data.status_code)
print(data.content)
print(data.text)
