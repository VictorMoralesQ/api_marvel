import httpx
import json
import os
from dotenv import load_dotenv
from utils.Params import Params
import pandas as pd

class Comics:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('URL_BASE')
        self.endpoints = json.loads(os.getenv('ENDPOINTS'))
        self.params = Params.get_params()

    def getComics(self):
        response = httpx.get(f'{self.url}/{self.endpoints[1]}', params=self.params)
        if response.status_code == 200:
            list_comics = []
            print("Comics retrieved successfully")
            data = response.json()
            for comic in data['data']['results']:
                id = comic['id']
                digital_id = comic['digitalId']
                title = comic['title']
                description = comic['description']
                list_comics.append({
                    'id': id,
                    'digital_id': digital_id,
                    'title': title,
                    'description': description
                })

            df_comics = pd.DataFrame(list_comics, columns=['id', 'digital_id', 'title', 'description'])
            return df_comics
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()

    def getComicsbyCharacter(self, character_id):
        response = httpx.get(f'{self.url}/{self.endpoints[0]}/{character_id}/comics', params=self.params)
        if response.status_code == 200:
            list_comics = []
            print("Comics retrieved successfully")
            data = response.json()
            for comic in data['data']['results']:
                id = comic['id']
                digital_id = comic['digitalId']
                title = comic['title']
                description = comic['description']
                list_comics.append({
                    'id': id,
                    'digital_id': digital_id,
                    'title': title,
                    'description': description
                })

            df_comics = pd.DataFrame(list_comics, columns=['id', 'digital_id', 'title', 'description'])
            return df_comics
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()
