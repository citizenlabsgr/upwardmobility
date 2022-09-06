from this import s
import pandas as pd
import json

# need to get all the crime data into the format
# <state>,<county>,<year1>,<year2>,..
# and later the fips data

# some agencies are split over two counties

# not all agencies have data back to 1985, and not all go to 2020

if __name__ == '__main__':
    states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

    state_county_crimes = {}

    total_agencies = 0

    for state in states:
        f2 = open(f"data/{state}_ori_violentcrimes.json")
        state_ori_json = json.load(f2)

        num_agencies = len(state_ori_json.keys()) 

        total_agencies += num_agencies

        print(f'{state} as {num_agencies} agencies') 
            
    print(f'There are {total_agencies} total agencies')