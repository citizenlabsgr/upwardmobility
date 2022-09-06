import json
import requests
from datetime import datetime

# sign up for a free api key at https://api.data.gov/signup/
my_key = 'OzhpxZstJJTH21JVSav2auQxFIYOKAYsobOE9yQ8'

def get_violent_crime(ori):
    violent_crime_url = 'https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/{}/violent-crime/{}/{}?API_KEY={}&size=100' #need more than 100?
    url = violent_crime_url.format(ori, 1985, 2020, my_key)

    response = requests.get(url)

    crimes = response.json()['results']

    list_of_tuples = []

    def add_to_list(c):
        tuple = (c['data_year'], c['actual'])
        list_of_tuples.append(tuple)

    [add_to_list(c) for c in crimes]

    return list_of_tuples

def get_state_info(state):

    print(f'starting {state} at {datetime.now()}')

    agency_url = 'https://api.usa.gov/crime/fbi/sapi/api/agencies/byStateAbbr/{}?API_KEY={}'
    url = agency_url.format(state, my_key)

    response = requests.get(url)
    agency_details = response.json()['results']

    agencies_dict = {}
    county_dict = {}

    def add_to_dict(a):
        #ori is the Originating Agency Identifier
        ori = a['ori']

        a['violent_crime_counts'] = get_violent_crime(ori) 
        
        agencies_dict[ori] = a
        
        county_name = a['county_name']

        if len(county_name) > 0:
            if county_name in county_dict:
                l = county_dict[county_name]
                l.append(a['ori'])
                county_dict[county_name] = l
            else:
                county_dict[county_name] = [a['ori']]

    [add_to_dict(a) for a in agency_details]

    # Serializing json
    state_ori_json = json.dumps(agencies_dict, indent=4)
    state_county_ori_json = json.dumps(county_dict, indent=4)
    
    # save the results for the state
    with open(f"data/{state}_ori_counties.json", "w") as outfile:
        outfile.write(state_county_ori_json)

    with open(f"data/{state}_ori_violentcrimes.json", "w") as outfile:
        outfile.write(state_ori_json)

    print(f'Done with {state} at {datetime.now()}')

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

print(datetime.now())

[get_state_info(s) for s in states]

print(datetime.now())