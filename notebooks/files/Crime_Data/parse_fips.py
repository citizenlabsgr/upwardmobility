
from unittest import skip
import pandas as pd
import json

state_name_abbreviation_df = pd.read_csv('data/state_name_abbreviations.csv')

state_county_dict = {}

def set_values(row):
    county_state_name = row['NAME'].split(',')

    county_name = county_state_name[0].replace('County','').upper().strip()
    state_name =  county_state_name[1].strip() 

    row['County_Name'] = county_name.replace('.','') #there are no periods in the FBI data
    row['State_Name'] = state_name

    try:
        row['State_Abbreviation'] = state_name_abbreviation_df[state_name_abbreviation_df['Name']==state_name].iloc[0]['Abbreviation']
    except:
        row['State_Abbreviation'] = state_name

    
    state_county = row['State_Abbreviation']+'-'+row['County_Name']

    fips = row['state']+row['county']

    state_county_dict[state_county] = fips

    return row

# downloaded from https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*
df = pd.read_json('data/FIPS_info.json')

df.drop(index=0,axis=0,inplace=True)

df.columns = ['NAME','state','county']

df['County_Name'] = ''
df['State_Name'] = ''
df['State_Abbreviation'] = ''
df['State_Abbreviation_County'] = ''
df['FIPS'] = ''

df.apply(set_values,axis=1)

state_county_fips_json = json.dumps(state_county_dict, indent=4)

# save the results for the state
with open(f"data/state_county_fips.json", "w") as outfile:
    outfile.write(state_county_fips_json)

print('done')