import hashlib
from dotenv import load_dotenv
import time
import os

class Params:
    load_dotenv()
    ts = str(int(time.time()))
    public_key = os.getenv('PUBLIC_KEY')
    private_key = os.getenv('PRIVATE_KEY')
    
    @staticmethod
    def get_params():
        hash_data = hashlib.md5(f'{Params.ts}{Params.private_key}{Params.public_key}'.encode()).hexdigest()
        return {
            'ts': Params.ts,
            'hash': hash_data,
            'apikey': Params.public_key
        }