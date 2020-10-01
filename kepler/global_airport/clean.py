# %% import os
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/global_airport'))
    print(os.getcwd())
except:
    pass

# %%
import pandas as pd
# %% flights data
flights = pd.read_csv('./data/Cleaned_2018_Flights.csv')
flights.head()
# %% airport data
airports = pd.read_csv('./data/GlobalAirportDatabase.csv', names=[
    'Airport ID',
    'Name', 'City',
    'Country', 'IATA',
    'ICAO', 'Latitude',
    'Longitude', 'Altitude',
    'Timezone', 'DST',
    'Tz database time zone', 'Type',
    'Source'
    ])
airports.head()

# %%
airports.to_csv('./data/formatted_airports.csv')