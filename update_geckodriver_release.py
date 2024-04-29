"""
更新geckodriver.json
"""

from common import RequestBase, JsonParser

url = 'https://api.github.com/repos/mozilla/geckodriver/releases'
json_parser = JsonParser('./GeckodriverLastVersion.json')

data = RequestBase(url).get
_data = [i['tag_name'] for i in data]
_new_data = {
    'latest': _data[0],
    'versions': _data
}

if json_parser.data != _new_data:
    json_parser.set(_new_data)
    print('Update GeckodriverLastVersion.json Succeed!')
