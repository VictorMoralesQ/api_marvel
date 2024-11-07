import httpx
import json
import os
from dotenv import load_dotenv
from utils.Params import Params
import pandas as pd

class Series:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('URL_BASE')
        self.endpoints = json.loads(os.getenv('ENDPOINTS'))
        self.params = Params.get_params()

    def getSeries(self):
        response = httpx.get(f'{self.url}/{self.endpoints[3]}', params=self.params)
        if response.status_code == 200:
            list_series = []
            print("Series retrieved successfully")
            data = response.json()
            for serie in data['data']['results']:
                id = serie['id']
                title = serie['title']
                description = serie['description']
                start_year = serie['startYear']
                end_year = serie['endYear']
                rating = serie['rating']
                list_series.append({
                    'id': id,
                    'title': title,
                    'description': description,
                    'start_year': start_year,
                    'end_year': end_year,
                    'rating': rating
                })

            df_series = pd.DataFrame(list_series, columns=['id', 'title', 'description', 'start_year', 'end_year', 'rating'])
            return df_series
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()

    def getSeriesbyCharacter(self, character_id):
        response = httpx.get(f'{self.url}/{self.endpoints[0]}/{character_id}/series', params=self.params)
        if response.status_code == 200:
            list_series = []
            print("Series retrieved successfully")
            data = response.json()
            for serie in data['data']['results']:
                id = serie['id']
                title = serie['title']
                description = serie['description']
                start_year = serie['startYear']
                end_year = serie['endYear']
                rating = serie['rating']
                list_series.append({
                    'id': id,
                    'title': title,
                    'description': description,
                    'start_year': start_year,
                    'end_year': end_year,
                    'rating': rating
                })

            df_series = pd.DataFrame(list_series, columns=['id', 'title', 'description', 'start_year', 'end_year', 'rating'])
            return df_series
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()