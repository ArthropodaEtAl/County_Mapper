import pandas as pd
import numpy as np
import re
import os

cwd = os.getcwd()
inat_export = "observations-644823.csv"
observations_csv = pd.read_csv(os.path.join(cwd,inat_export))

observations_csv =observations_csv[observations_csv['place_country_name'] == 'United States']
observations_csv= observations_csv.drop_duplicates(subset=['place_county_name','place_state_name'])

state_abbreviation ={'Alabama': 'AL',
 'Alaska': 'AK',
 'Arizona': 'AZ',
 'Arkansas': 'AR',
 'California': 'CA',
 'Colorado': 'CO',
 'Connecticut': 'CT',
 'Delaware': 'DE',
 'District of Columbia':'DC',
 'Florida': 'FL',
 'Georgia': 'GA',
 'Hawaii': 'HI',
 'Idaho': 'ID',
 'Illinois': 'IL',
 'Indiana': 'IN',
 'Iowa': 'IA',
 'Kansas': 'KS',
 'Kentucky': 'KY',
 'Louisiana': 'LA',
 'Maine': 'ME',
 'Maryland': 'MD',
 'Massachusetts': 'MA',
 'Michigan': 'MI',
 'Minnesota': 'MN',
 'Mississippi': 'MS',
 'Missouri': 'MO',
 'Montana': 'MT',
 'Nebraska': 'NE',
 'Nevada': 'NV',
 'New Hampshire': 'NH',
 'New Jersey': 'NJ',
 'New Mexico': 'NM',
 'New York': 'NY',
 'North Carolina': 'NC',
 'North Dakota': 'ND',
 'Ohio': 'OH',
 'Oklahoma': 'OK',
 'Oregon': 'OR',
 'Pennsylvania': 'PA',
 'Rhode Island': 'RI',
 'South Carolina': 'SC',
 'South Dakota': 'SD',
 'Tennessee': 'TN',
 'Texas': 'TX',
 'Utah': 'UT',
 'Vermont': 'VT',
 'Virginia': 'VA',
 'Washington': 'WA',
 'West Virginia': 'WV',
 'Wisconsin': 'WI',
 'Wyoming': 'WY'}

observations_csv = observations_csv.replace({'place_state_name': state_abbreviation})

#District of columnbia nomenclature 
dc_excepttion = {'District of Columbia':'Washington'}
observations_csv = observations_csv.replace({'place_county_name': dc_excepttion})
#Add exception for counties with names that have a space in them using regex
observations_csv['Add Text'] = observations_csv['place_county_name']+ "__" +observations_csv['place_state_name']
#convert to string to insert into the .txt file
add_string = np.array2string(observations_csv['Add Text'].unique(), separator=",")
add_string= add_string.replace("'",'"')
add_string= re.sub(r'(\w+)(\s)(\w+)',r'\1_\3',add_string)

text_file_name = os.path.join(cwd,"mapchartSave__usa_counties__.txt")
text_file_out = os.path.join(cwd,"mapchartSave__usa_counties__1.txt")

with open(text_file_name, 'r') as file:
    data = file.read()
    data = data.replace('"paths":[]', '"paths":'+add_string)

with open(text_file_out, 'w') as file:
    file.write(data)
