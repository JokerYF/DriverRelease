import json
import os.path

import requests


class RequestBase:
    def __init__(self, url):
        self.url = url

    @property
    def get(self):
        return requests.get(url=self.url).json()


class JsonParser:
    def __init__(self, path):
        self.path = os.path.abspath(path)

    @property
    def exist(self):
        return os.path.exists(self.path)

    @property
    def data(self):
        if not self.exist:
            return {}
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get(self, key, default=''):
        return self.data.get(key, default)

    def set(self, data):
        with open(self.path, 'w+', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
