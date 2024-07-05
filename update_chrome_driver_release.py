"""
更新ChromeDriver版本
"""

from common import RequestBase, JsonParser

url = 'https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json'
url2 = 'https://googlechromelabs.github.io/chrome-for-testing/latest-patch-versions-per-build.json'
json_parser = JsonParser('./ChromeDriverLastVersion.json')
json_parser2 = JsonParser('./ChromeDriverLatestPatchVersion.json')

data = RequestBase(url).get

if json_parser.get('timestamp', '') != data['timestamp']:
    json_parser.set(data)
    print(data)
    print('Update ChromeDriverLastVersion.json Succeed!')

data2 = RequestBase(url2).get
if json_parser2.get('timestamp', '') != data2['timestamp']:
    json_parser2.set(data2)
    print(data2)
    print('Update ChromeDriverLatestPatchVersion.json Succeed!')
