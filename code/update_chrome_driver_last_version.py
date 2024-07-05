"""
更新ChromeDriver版本
"""

from code.common import RequestBase, JsonParser

url = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json'
json_parser = JsonParser('../ChromeDriverLastVersion.json')

data = RequestBase(url).get

if json_parser.get('timestamp', '') != data['timestamp']:
    json_parser.set(data)
    print(data)
    print('Update ChromeDriverLastVersion.json Succeed!')
