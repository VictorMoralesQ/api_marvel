import httpx
import json
import os
from dotenv import load_dotenv
from utils.Params import Params
import pandas as pd

class Character:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('URL_BASE')
        self.endpoints = json.loads(os.getenv('ENDPOINTS'))
        self.params = Params.get_params()

    def get_characters(self):
        response = httpx.get(f'{self.url}/{self.endpoints[0]}', params=self.params)
        if response.status_code == 200:
            list_characters = []
            print("Characters retrieved successfully")
            data = response.json()
            for character in data['data']['results']:
                id = character['id']
                name = character['name']
                description = character['description']

                list_characters.append({
                    'id': id,
                    'name': name,
                    'description': description
                })

            df_characters = pd.DataFrame(list_characters, columns=['id', 'name', 'description'])

            return df_characters
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()

    def getCharacterbyId(self, id):
        response = httpx.get(f'{self.url}/{self.endpoints[0]}/{id}', params=self.params)
        if response.status_code == 200:
            data = response.json()
            name = data['data']['results'][0]['name']
            description = data['data']['results'][0]['description']
            df_character = pd.DataFrame({
                'id': id,
                'name': name,
                'description': description
            }, index=[0], columns=['id', 'name', 'description'])
            print("Character retrieved successfully")
            return df_character
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()

