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

    years = []
    for i in range(1985,2021):
        years.append(i)

    f1 = open(f"data/state_county_fips.json")
    state_county_fips = json.load(f1)

    state_county_crimes = {}

    cols = []
    cols.append('STATE')
    cols.append('COUNTY')
    cols.append('FIPS')
    [cols.append(y) for y in years]

    records = []

    for state in states:
        f2 = open(f"data/{state}_ori_violentcrimes.json")
        state_ori_json = json.load(f2)

        counties = {}
        
        for ori in state_ori_json.keys():
            agency = state_ori_json[ori]

            # there can be 2 or more counties for a reporting agency
            # there isnt a great way to split it
            # so lets just split it evenly among them
            agency_counties = agency['county_name'].split(';')

            for c in agency_counties:

                agency_county_name = c.strip()



                county_crime_stats = {}

                if agency_county_name in counties:
                    county_crime_stats = counties[agency_county_name]
                else:
                    [county_crime_stats.setdefault(y,0) for y in years]

                    counties[agency_county_name] = county_crime_stats

                violent_crime_counts = agency['violent_crime_counts']

                for y in violent_crime_counts:
                    county_crime_stats[y[0]] += (y[1]/len(agency_counties))

        for c in counties.keys():
            values = []

            county = counties[c]
            values.append(state)
            values.append(c)

            fips_key = state+'-'+c

            if fips_key in state_county_fips:
                values.append(state_county_fips[fips_key])
            else:
                values.append('NOFIPS')

            [values.append(v) for v in county.values()]

            records.append(values)

    df = pd.DataFrame(records, columns=cols)

    df.to_csv('data/crime_data_fips_split.csv')

    print('done')