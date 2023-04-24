# Fake Data Generator and Geocoding Tool

This program generates fake data and uses an `API` to geocode the addresses, creating a concatenated `Pandas DataFrame`. It also includes functions to count the number of occurrences of each domain name and job title and to create a map with markers for each address.

## Installation

To use this program, you will need to have Python 3 installed, as well as the following libraries:

- `pandas`
- `faker`
- `numpy`
- `requests`
- `folium`

You can install these libraries using pip:

```
pip install pandas faker numpy requests folium
```

## Usage

To use the program, run the script `fake_data_generator.py`. The script will generate three dataframes with five rows each, concatenate them into a single dataframe, and perform some analysis on the data. 

You can modify the `generate_multiple_dataframes` function to generate a different number of dataframes and rows per dataframe. You will also need to replace the `api_key` variable in the `get_lat_lng` function with your own `API` key.

## Functions

This program includes the following functions:

### get_lat_lng(address)

This function takes an address as input and uses the `OpenCage Geocoder API` to retrieve the latitude and longitude of the address.

### generate_multiple_dataframes(num_dataframes, num_rows)

This function generates multiple dataframes with fake data and geocodes the addresses. It concatenates all dataframes into a single dataframe and returns it.

### domain_counts

This variable is a `Pandas Series` that contains the number of occurrences of each domain name in the concatenated dataframe.

### job_counts

This variable is a `Pandas Series` that contains the number of occurrences of each job title in the concatenated dataframe.

### m

This variable is a `Folium map` that displays markers for each address in the concatenated dataframe.

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request. 

## License

This program is licensed under the MIT License. See `LICENSE` for more information.
