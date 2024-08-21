import json

def test(countries):
    return json.loads(countries)

countries = "[\"Australia\", \"Canada\", \"Germany\", \"United Kingdom\", \"United States\"]"
list = test(countries)

print(len(list))