import httpx
import json
import os
from dotenv import load_dotenv
from utils.Params import Params
import pandas as pd

class Stories:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('URL_BASE')
        self.endpoints = json.loads(os.getenv('ENDPOINTS'))
        self.params = Params.get_params()

    def getStories(self):
        response = httpx.get(f'{self.url}/{self.endpoints[4]}', params=self.params)
        if response.status_code == 200:
            list_stories = []
            print("Stories retrieved successfully")
            data = response.json()
            for story in data['data']['results']:
                id = story['id']
                title = story['title']
                description = story['description']
                list_stories.append({
                    'id': id,
                    'title': title,
                    'description': description
                })

            df_stories = pd.DataFrame(list_stories, columns=['id', 'title', 'description'])
            return df_stories
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()

    def getStoriesbyCharacter(self, character_id):
        response = httpx.get(f'{self.url}/{self.endpoints[0]}/{character_id}/stories', params=self.params)
        if response.status_code == 200:
            list_stories = []
            print("Stories retrieved successfully")
            data = response.json()
            for story in data['data']['results']:
                id = story['id']
                title = story['title']
                description = story['description']
                list_stories.append({
                    'id': id,
                    'title': title,
                    'description': description
                })

            df_stories = pd.DataFrame(list_stories, columns=['id', 'title', 'description'])
            return df_stories
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()