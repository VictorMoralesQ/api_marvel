import httpx
import json
import os
from dotenv import load_dotenv
from utils.Params import Params
import pandas as pd

class Events:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('URL_BASE')
        self.endpoints = json.loads(os.getenv('ENDPOINTS'))
        self.params = Params.get_params()


    def getEvents(self):
        response = httpx.get(f'{self.url}/{self.endpoints[2]}', params=self.params)
        if response.status_code == 200:
            list_events = []
            print("Events retrieved successfully")
            data = response.json()
            for event in data['data']['results']:
                id = event['id']
                title = event['title']
                description = event['description']
                list_events.append({
                    'id': id,
                    'title': title,
                    'description': description
                })

            df_events = pd.DataFrame(list_events, columns=['id', 'title', 'description'])
            return df_events
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()

    def getEventsbyCharacter(self, character_id):
        response = httpx.get(f'{self.url}/{self.endpoints[0]}/{character_id}/events', params=self.params)
        if response.status_code == 200:
            list_events = []
            print("Events retrieved successfully")
            data = response.json()
            for event in data['data']['results']:
                id = event['id']
                title = event['title']
                description = event['description']
                list_events.append({
                    'id': id,
                    'title': title,
                    'description': description
                })

            df_events = pd.DataFrame(list_events, columns=['id', 'title', 'description'])
            return df_events
        else:
            print("Error creating order with error code: ", response.status_code)
            return response.json()