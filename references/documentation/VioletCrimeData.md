# About Violent Crime Data
<a href="https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/topic-pages/violent-crime">Violent crime</a> is composed of four offenses: murder and nonnegligent manslaughter, rape, robbery, and aggravated assault.

The data was obtained from 18,616 agencies across the United States via the API for usa.gov, the same source that powers the FBI's <a href="https://crime-data-explorer.app.cloud.gov/pages/home">Crime Data Explorer</a>. API keys can be obtained for free from <a href="https://api.data.gov/signup/">https://api.data.gov/signup/</a>.

It took over 17 hours to perform the API calls to 18,616 agencies to obtain violent crime data from 1985-2020. Not all agencies report in these data ranges. The `crime_parsing.py` file performs the API calls and saves the data to JSON files using the `{state}_ori_violentcrimes.json` naming convention for faster parsing during the merge process.

# Merging Violent Crime Data
Each agency that provides crime data has a unique identifier, called an Originating Agency Identifier (ori). You can <a href="https://crime-data-explorer.fr.cloud.gov/pages/home">explore</a> the agency participation for each state on the FBI's Crime Data Explorer site.

Agency are associated with at least one county. Over 300 of them are associated with multiple counties. For example, the East Lansing Police Department in Lansing, MI is split between Clinton and Ingham counties. There is no perfect way to split the data between counties. Therefore, an even split of the data is assumed. If there are 100 violent crimes from this agency across two counties, then 50 crimes are counted toward each county. This is because the reporting is done on the county's Federal Information Processing Standard (FIPS) code. 

The FIPS code for counties across United States can be obtained from <a href="https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*">https://api.census.gov/data/2010/dec/sf1?get=NAME&for=county:*</a>. The `parse_fips.py` file parses the result of this call and formats it so the two-letter state abbreviation and county name can be used as a lookup for the county FIPS code. This is then saved to the `data/state_county_fips.json` file. 

Finally, `format_crime_data.py` combines the violent crime data from each agency across the counties, performing the split outlined above in the case of an agency across multiple counties. It then  merges the FIPS code data with the county information to build `data/crime_data_fips_split.csv`, which is what is used for reporting. 