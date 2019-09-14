'''
make_zone_facts.py
------------------

This file creates the zone_facts table in the database, which is sent to
the front-end via /api/zone_facts/. It depends on the census data, crime
data, and the geograpic boundaries. The output columns for this file are:

    - zone_type:                Tract, neighborhood, or ward.
    - zone:                     Tract, neighborhood, or ward number.
    - poverty_rate
    - fraction_black
    - income_per_capita
    - labor_participation
    - fraction_foreign
    - fraction_single_mothers
    - acs_median_rent
    - crime_rate
    - violent_crime_rate
    - non_violent_crime_rate
    - building_permits_rate
    - construction_permits_rate
'''

import pandas as pd
from sources import get_acs_data, get_crime_data

acs = get_acs_data()
crime = get_crime_data()

#permits = get_permit_data()


df = acs.merge(crime, left_on='tract', right_on='census_tract')
