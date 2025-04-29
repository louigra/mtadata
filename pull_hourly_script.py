from sodapy import Socrata
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# Set up the authenticated client
client = Socrata(
    "data.ny.gov",
    "81XwdXsf7zfPYg3IjlWOLj45o",
    username="glouis6@me.com",
    password="TheMobkilledJFKin1963!"
)

def compare_months(year1, month1, year2, month2, station):
    month1_results = client.get(
        "wujg-7c2s",
        limit=50000,  # adjust as needed
        station_complex_id=station,
        select="date_trunc_ymd(transit_timestamp) as day, sum(ridership) as total_ridership",
        where="transit_timestamp >= '{year1}-{month1}-01T00:00:00' AND transit_timestamp < '{year1}-{month1 + 1}-01T00:00:00'",
        group="day",
        order="day ASC",
        
        

# Filter for Manhattan and select only the needed columns
results = client.get(
    "wujg-7c2s",
    limit=50000,  # adjust as needed
    borough="Manhattan",
    station_complex_id="313",
    select="date_trunc_ymd(transit_timestamp) as day, sum(ridership) as total_ridership",
    where="transit_timestamp >= '2024-01-01T00:00:00' AND transit_timestamp < '2024-02-01T00:00:00'",
    group="day",
    order="day ASC",
)

# Convert to DataFrame
df = pd.DataFrame.from_records(results)

# Drop duplicates to get unique combinations
# seventysecond = df.drop_duplicates()

print(df)