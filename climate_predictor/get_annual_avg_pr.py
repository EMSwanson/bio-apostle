import requests


class DataFetcher(object):

    def __init__(self):
        pass

    def get(self):
        return requests.get(self.request_to_format)

    def dask(self):
        pass
        #Call  self.get(request_to_format) then convert to dask df

    def pandas(self):
        pass
        #Call self.get(request_to_format) then convert to pandas df


class ClimateBank(DataFetcher):

    def __init__(self, type, var, start, end, country):
        DataFetcher.__init__(self)
        self.type = type
        self.var = var
        self.start = start
        self.end = end
        self.country = country
        self.base_request = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/"
        self.request_to_format = f"{self.base_request}/{self.type}/{self.var}/{self.start}/{self.end}/{self.country}.json"


annual_average_rainfall = ClimateBank(type = "annualavg", var = "pr", start = 1980, end = 1999, country = "USA")
data = annual_average_rainfall.get()
print(data.status_code)
print(data.content)
print(data.text)
