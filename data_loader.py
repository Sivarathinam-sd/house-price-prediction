import pandas as pd
import numpy as np

class CSV_Loader:
    def __init__(self):
        self.df = pd.read_csv('datasets/combined_housing_data.csv')
    
    def get_location(self, city):
        city_data = self.df[self.df['city'] == city]
        location = city_data['location'].unique()
        
        return list(location)

    def get_coordinates(self, city, location):
        city_data = self.df[self.df['city'] == city]
        coordinates = city_data[city_data['location'] == location]
        lat = coordinates['latitude'].unique()
        lon = coordinates['longitude'].unique() 
        return {'lat' : float(sum(lat)/len(lat)) , 'lon' : float(sum(lon)/len(lon)) }


