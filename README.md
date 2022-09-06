Project Upward Mobility
==============================

Communities can foster environments for citizens to thrive and boost their upward mobility. The conditions most local to a family are also most critical to achieve mobility from poverty. Mobility from poverty includes economic success, power and autonomy, and being valued in a community.  
To measure how upwardly mobile a community is, there are three key drivers tied to the definition: 

* Strong and health families
* Supportive communities
* Opportunities to learn and earn

Each driver has evidence-based metrics associated with it that can highlight the strengths and weaknesses of a community, and track progress on goals to improve the lives of its residents. These metrics can then inform community leaders where priorities should be to ensure that citizens have the opportunity to reach their full potential and be well-rounded individuals. 

This project was inspired and has intended to follow the research report [Boosting Upward Mobility: Metrics to Inform Local Action](https://www.urban.org/research/publication/boosting-upward-mobility-metrics-inform-local-action).
This report detailed what metrics to gather and what government agency or other source to obtain them from, however, no technical details were provided. The original intention was that these would be collected by one city or region for their own upward mobility analysis, and therefore would not be a large lift to manually go to each source and gather the data. 

### Summary 

This project contains a way to programmatically collect data for all counties in the US from multiple disparate sources and bring them together in one dataframe. This data is then used to calculate 16 Upward Mobility Metrics as laid out by the Urban Institute, and present them on a web front end for users. This is a reproducible method to retrieve many of these metrics, so that less-technical organizations will find them more accessible, and they can be updated as new data becomes available each year.  

Getting Started
------------
### Setting up your environment in a command prompt:

1. Clone the repo:
    - `git clone https://github.com/laurenrwolf/project-upward-mobility.git`
2. Set up a virtual environment: 
    - `python -m venv myvenv`
3. Activate virtual environment:
    - (Linux and "OS X): `source myvenv/bin/activate`
	- (Windows): `myvenv\Scripts\activate`
4. Install requirements to run notebooks: 
    - `pip install -r requirements.txt`


------------
### Census API Key
An API key is required to pull data via the Census API in the following notebook:

* acs.ipynb

Sign up for a key at this [link](https://api.census.gov/data/key_signup.html) and be sure to insert it in to the specified location in the notebook.

### Requirements

There are three parts to this project:
* Data collection, manipulation and analysis
* django website front end - contained in sub repo 'djangosite @ d6e6e8f' 
* Streamlit data visualization app - contained in sub repo 'streamlitapp @ a48cd17'

Each part has its own requirements.txt

### Notebook Execute Order

1. acs.ipynb
2. The following notebooks can be ran in any order, as long as they are all completed by before running step #3
	* acs_expose_poverty.ipynb
	* air_quality.ipynb
	* debt.ipynb
	* education.ipynb
	* health_shortages.ipynb
	* juvenile_arrests.ipynb
	* low_birth_weight.ipynb
	* transportation.ipynb
	* violent_crime.ipynb
	* voter_turnout.ipynb
3. counties_merged.ipynb

Project Organization
------------

    ├── README.md          <- The top-level README for using this project.
    │
    ├── notebooks          <- Jupyter notebooks.
    |   └── data
    │       ├── external       <- Data from third party sources.
    │       ├── interim        <- Intermediate data that has been transformed.
    │       ├── processed      <- The final data sets
    │       └── raw            <- The original, immutable data dump.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment. The django site and Streamlit app have their own requirements.txt files within those subrepos

	 
Project Structure
--------
Notebooks must be ran in a specific order, first pulling all of the metrics from their various sources using specific notebooks, before joining them together in one final dataframe.

![Project Structure](https://github.com/laurenrwolf/project-upward-mobility/blob/main/references/capstone%20pipeline.png?raw=true)

Ways to Explore the Data 
------------

There are three main functions on the project [website](https://upwardmobility.pythonanywhere.com/)

### US National View

Explore a national overview of a single metric

<img src="https://github.com/laurenrwolf/project-upward-mobility/blob/main/references/NationalView.gif" width="75%" height="75%"/>

### County Finder

Find top ranking counties in the metrics that matter to you

<img src="https://github.com/laurenrwolf/project-upward-mobility/blob/main/references/CountyFinder.gif" width="75%" height="75%"/>

### County Details

View detailed metrics for a specific county

<img src="https://github.com/laurenrwolf/project-upward-mobility/blob/main/references/CountyDetails.gif" width="75%" height="75%"/>
