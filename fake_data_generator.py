import pandas as pd
from faker import Faker
import numpy as np
import requests
import folium

fake = Faker()

def get_lat_lng(address):
    """
    Get the latitude and longitude of an address using the OpenCage Geocoder API.
    
    Parameters:
    address (str): the address to geocode
    
    Returns:
    lat_lng (tuple): a tuple containing the latitude and longitude of the address
    """
    api_key = 'YOUR_API_KEY_HERE' # replace with your API key
    url = f'https://api.opencagedata.com/geocode/v1/json?q={address}&key={api_key}'
    response = requests.get(url).json()
    lat = response['results'][0]['geometry']['lat']
    lng = response['results'][0]['geometry']['lng']
    lat_lng = (lat, lng)
    return lat_lng

def generate_multiple_dataframes(num_dataframes, num_rows):
    """
    Generate multiple dataframes with fake data.
    
    Parameters:
    num_dataframes (int): the number of dataframes to generate
    num_rows (int): the number of rows per dataframe
    
    Returns:
    concatenated_dataframe (pd.DataFrame): a concatenated dataframe containing all generated dataframes
    """
    # create list of dictionaries containing fake data
    dataframes = []
    for i in range(num_dataframes):
        fake_data = [{"date": fake.date(),
                      "name": fake.name(),
                      "email": fake.email(),
                      "address": fake.address()} for _ in range(num_rows)]
        # create dataframe from list of dictionaries
        fake_dataframe = pd.DataFrame(fake_data)
        # add a new column with a fake job title for each row
        fake_dataframe['job_title'] = fake_dataframe.apply(lambda x: fake.job(), axis=1)
        # use a geocoding API to get the latitude and longitude of each address
        fake_dataframe['lat_lng'] = fake_dataframe['address'].apply(get_lat_lng)
        # extract the latitude and longitude from the lat_lng column
        fake_dataframe['latitude'] = fake_dataframe['lat_lng'].apply(lambda x: x[0])
        fake_dataframe['longitude'] = fake_dataframe['lat_lng'].apply(lambda x: x[1])
        # extract the domain name from the email column
        fake_dataframe['domain'] = fake_dataframe['email'].str.split('@').str[1].str.split('.').str[0]
        # add a new column with a random score between 0 and 100
        fake_dataframe['score'] = np.random.randint(0, 101, size=len(fake_dataframe))
        # sort the dataframe by the score column to see who has the highest score
        fake_dataframe = fake_dataframe.sort_values(by='score', ascending=False)
        # append the dataframe to the list of dataframes
        dataframes.append(fake_dataframe)
    # concatenate all dataframes into a single dataframe
    concatenated_dataframe = pd.concat(dataframes, ignore_index=True)
    return concatenated_dataframe

# generate 3 dataframes with 5 rows each
fake_dataframe = generate_multiple_dataframes(3, 5)

# group the dataframe by domain name and count the number of occurrences of each domain name
domain_counts = fake_dataframe.groupby('domain')['name'].count()

# group the dataframe by job title and count the number of occurrences of each job title
job_counts = fake_dataframe.groupby('job_title')['name'].count()

# create a folium map centered at the mean of the latitude and longitude columns
map_center = [fake_dataframe['latitude'].mean(), fake_dataframe['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=10)

# add markers to the map for each row in the dataframe
for index, row in fake_dataframe.iterrows():
    marker = folium.Marker([row['latitude'], row['longitude']], popup=row['name'] + ': ' + row['address'])
    marker.add_to(m)

# display the map
m





